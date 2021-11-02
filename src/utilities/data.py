import json

class Data():

    def __init__(self):
        data = Data.get_live_info(self)
        if data != None:
            self.position = [data['worldPoint']['x'], data['worldPoint']['y']]
            self.inventory = data['inventory']
            self.run_energy = data['runEnergy']
            self.camera_angle = data['camera']['yaw']

    def get_live_info(self) -> dict:
        '''Returns specific live information from the game client via the Status Socket plugin.'''
        try:
            f = open('live_data.json',)
            data = json.load(f)
            return data
        except:
            pass

    def update_inventory(self) -> None:
        """Updates the current inventory."""
        data = self.get_live_info()
        if data != None:
            self.inventory = data['inventory']

    def update_positon(self) -> None:
        """Updates the current position of the player."""
        data = self.get_live_info()
        if data != None:
            self.position = [data['worldPoint']['x'], data['worldPoint']['y']]

    def update_run_energy(self) -> None:
        """Updates the current run energy."""
        data = self.get_live_info()
        if data != None:
            self.run_energy = data['runEnergy']
    
    def update_camera_angle(self) -> None:
        """Updates current camera angle."""
        data = self.get_live_info()
        if data != None:
            self.camera_angle = data['camera']['yaw']