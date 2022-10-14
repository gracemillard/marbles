import json

class FilterParams():

    def __init__(self):
        self.size = None
        self.color = None
        self.name = None
        self.color_pattern = None
        self.size_constraint = None

    def _read_json_config(self, json_config_path):
        with open(json_config_path) as f:
            configurations = json.load(f)

            return  configurations

    def _is_size(self,configurations):
        if not configurations['filter_type']:
            raise ValueError(f"no ilters selected config might not be configred right")
        elif "size" in configurations['filter_type']:
            print("size was selected in config")
            self.size=True

            if configurations['size_constraint']:
                self.size_constraint=configurations['size_constraint']
            else:
                raise ValueError(f"no size_constraint selected config might not be configred right")

    def _is_color(self, configurations):
        if not configurations['filter_type']:
            raise ValueError(f"no ilters selected config might not be configred right")
        elif "color" in configurations['filter_type']:
            print("color was selected in config")
            self.color=True
            if configurations['color_pattern']:
                self.color_pattern=configurations['color_pattern']
            else:
                raise ValueError(f"no color pattern selected config might not be configred right")
            

    def _is_name(self, configurations):
        if not configurations['filter_type']:
            raise ValueError(f"no ilters selected config might not be configred right")
        elif "name" in configurations['filter_type']:
            print("name was selected in config")
            self.name=True


    def _set_params(self,json_config_path):
        configurations = self._read_json_config(json_config_path)

        self._is_color(configurations)
        
        self._is_name(configurations)

        self._is_size(configurations)

        print(f"everthing set , here is a look {self.color_pattern}")



