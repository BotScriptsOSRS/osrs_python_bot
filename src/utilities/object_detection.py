import cv2
import pyautogui
import numpy as np
from .window_capture import WindowCapture
from typing import Any, List
from PIL import Image
from time import sleep

class ObjectDetection(WindowCapture):

    def __init__(self):
        WindowCapture.__init__(self)

    def find_object_contour(self, color: int) -> List[int]:
        """Returns the contour of color marked objects on screen."""
        # define the list of boundaries
        # purple/cyan
        boundaries = [[[240, 0, 240], [255, 10, 255]],[[254, 0, 0], [255, 1, 0]]]
        lower = boundaries[color][0]
        upper = boundaries[color][1]
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply the mask
        image = self.get_screenshot()
        mask = cv2.inRange(image, lower, upper)
        _ = cv2.bitwise_and(image, image, mask=mask)
        _, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return contours

    def find_closest_object(self, color: int) -> List[int]:
        """Returns the coordinates of the center of the closest object."""
        contours = self.find_object_contour(color)    
        if contours == []:
            return [0, 0]
        distance = []
        # Compute distance
        for c in contours:
            x, y ,w ,h = cv2.boundingRect(c)
            distance.append(np.sqrt((x-self.center_screen[0])**2+(y-self.center_screen[1])**2))
        # Find the closest tree
        min_value = min(distance)
        index_min = distance.index(min_value)
        x, y, w, h = cv2.boundingRect(contours[index_min])
        x_center = round(x+w/2) 
        y_center = round(y+h/2)
        # Dont want to use for minimap
        distance = np.sqrt((x-self.center_minimap[0])**2+(y-self.center_minimap[1])**2)
        if distance < 100:
            return []
        return [x_center, y_center]

    def click_closest_object(self, color: int) -> None:
        """Clicks the marked object that is closest to the player."""
        x,y = self.find_closest_object(color)
        if x !=0 and y !=0:
            pyautogui.moveTo(x, y, 0.2)
            pyautogui.click()

    def open_inv(self,image_url, confidence=0.9) -> None:
        """Opens the inventory if it is closed."""
        coords = self.locate_image_on_screen(image_url, confidence)
        while coords == []:
            pyautogui.press('esc')
            coords = self.locate_image_on_screen(image_url, confidence)
            sleep(0.5)

    def locate_image_on_screen(self,image_path: str, confidence: float = 0.9) -> List[int]:
        """Returns the coordinates of the center of an image if the image can be found on the screen."""
        # Locate all objects on screen
        objects = list(pyautogui.locateAllOnScreen(image_path, confidence = confidence))
        # Create a list with the center of all objects
        center_coords = []
        for object in objects:
            center_coords.append(pyautogui.center(object))
        # If centers are too close, delete one of them
        try:
            center_coords = self.edit_list(center_coords,len(center_coords),10)
        except:
            return []
        return center_coords
        
    def click_image_on_screen(self,image_path: str, confidence: float = 0.9) -> None:
        """Clicks an image if it can be found on the screen."""
        coords = self.locate_image_on_screen(image_path, confidence)
        if coords != []:
            pyautogui.moveTo(coords[0], duration=0.2)
            pyautogui.click()

    @staticmethod
    def get_screenshot() -> Image:
        """Returns a screenshot with BGR colors"""
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        return image
    
    @staticmethod
    def not_satisfy2(a,k,critical) -> bool:
        """Helper function for edit_list()"""
        flag=False
        cx2,cy2 = k
        for i in a:
            cx1,cy1 = i
            if(abs(cx1-cx2) < critical and abs(cy1-cy2) < critical):
                flag=True
                break
        return flag

    def edit_list(self, a,length_of_a,critical) -> List[Any]:
        """Removes coordinates that are close to each other, except one."""
        l = []
        l.append(a[0])
        i=1
        while(i < length_of_a):
            if(self.not_satisfy2(l,a[i],critical)==True):
                i+=1
            else:
                l.append(a[i])
                i+=1
        return l
