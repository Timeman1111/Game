


class Scene:
    def __init__(self,properties={},trace = None):
        # Initalize Scene and set class variables
        
        self.trace = trace
        self.properties = properties

    def set_location_text(self,text):
        #Set scene location text

        self.properties["location_setting_text"] = text

        
        return True


    def get_scene(self):

        # Get location setting from class property variable
        location_setting = self.properties["location_setting_text"]

        #Get shop data from class property variable and then get the names
        shops = self.properties["shops"]

        shops_names = [x["name"] for x in shops]

Library = Scene()
