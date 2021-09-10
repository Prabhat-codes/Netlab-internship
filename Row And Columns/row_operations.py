import pandas as pd
import numpy as np
from .utilities import *
from .msg import Message

class AddRow:
    df = "" #will store the dataframe
    details = "" #will store json config
    math_utility = MathUtilities() #utilities object
    m = Message()
    
    def __init__(self, df, details):
        self.details = details
        self.df = df
        

    

'''
JSON EXAMPLES

'''


