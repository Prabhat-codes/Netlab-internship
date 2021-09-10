import pandas as pd
import numpy as np
from .utilities import FilterUtilities
from .msg import Message

##################### Create  a filter #####################
class Filter:
    df = "" #will store the dataframe
    details = "" #will store json config
    m = Message()
    
    def __init__(self, df, details):
        self.details = details
        self.df = df
    
    def filter(self):
        a=FilterUtilities()
        msg=a.filter_data(self.details,self.df)
        return msg
    