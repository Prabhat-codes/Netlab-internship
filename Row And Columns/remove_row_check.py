import pandas as pd
import numpy as np
from Remove import Remove_Row #Remove is the class where we have to store the data
#RemoveRow is the class

class RemoveRow:
    df = "" #will store the dataframe
    details = "" #will store json config

    def __init__(self, df, details):
        self.details = details
        self.df = df

    def remove_row(self,df):
        r=Remove_Row()
        # To choose whichever config isnt empty and call the respective funciton. 
        cond=self.details["config"]["all_blanks"]
        if cond=="NA":
            cond=self.details["config"]["selected_blanks"]["column_list"]
            if cond=="NA":
                cond=self.details["config"]["condition"]
                df=r.conditional_removing_blanks(cond,df)
            else:
                df=r.remove_selected_blanks(cond,df)
        else:
            df=r.fully_blank_rows(df)
            #check the fullyblank rows and add the file path if that suggestion doesnt work out here. 


    
    {
	"group" : "row operations",
	"type" : "remove",
	"config" : {
		"all_blanks" : {
			"remove_all" : "True"  #if all elements of one row are empty
		},
		"selected_blanks" : "NA",
		"condition" : "NA"
        }
    }
    


    {
        "group" : "row operations",
        "type" : "remove",
        "config" : {
            "all_blanks" : "NA",
            "selected_blanks" : {
                "column_list" : [""] #even if one blank remove
            },
            "condition" : "NA"
        }
    }

    {
	"group" : "row operations",
	"type" : "remove",
	"config" : {
		"all_blanks" : "NA",
		"selected_blanks" : "NA"
		"condition" : {
			"left_cond":0, #which can also be a column
			"left_sign":"<", # can take values : <, <=, NA
			"column" : "Column name",
			"right_sign":"<=", #can take values : <, <=, NA
			"right_cond":10, #can be column too
			"remove" : True #will be false if they want to remove everything except the condition
		}
	}
