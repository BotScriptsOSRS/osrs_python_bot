import json

class Data():

    def get_live_info(self, category: str) -> dict:
        '''Returns specific live information from the game client via the Status Socket plugin.'''
        try:
            f = open('live_data.json',)
            data = json.load(f)
            return data[category]
        except:
            pass