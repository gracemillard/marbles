import re
import sys
from common.logging import get_logger
from common.filter_params import FilterParams

# import numpy as np
# import pytz



class MarbleProcessor(FilterParams):

    def __init__(self):
        self._logger = get_logger()
        
    def process_marbles(self,collection):

        self._set_params("resources/filters.json")

        print(f"this is the color patern {self.color_pattern}")

        ###maybe start by restructuring the json input
        self._logger.info(f"this is the input {collection}")

       # self._logger.info(f"this is the input {collection[0]}")

       self._logger.info(f"Starting processing for marbles")

        to_be_sorted=[]
       
       for m in range(len(collection)):
           unit=collection[m]

            #filter out small marbles
           if self.size:
                if _check_weight(unit):
                   pass
                else:
                    continue
            else:
                continue

            #filter out marbles that dont have palendrome names
            
            if self.name:
                if _check_name(unit):
                    pass
                else:
                    continue
            else:
                continue

            to_be_sorted.append(unit)

        #sort the marbles tht were collected

        if self.color:
            sorted_marbles = _sort_marbles_by_colors(to_be_sorted)
            return sorted_marbles

        else:
            print("I havent decided what should be returned if the config is empty")

    def _filter_by_weight(self, marble):

        return True

    def _filter_by_names(self, marbles):
        
        return True

    def _sort_marbles_by_colors(self, marbles):

        return marbles_sorted


