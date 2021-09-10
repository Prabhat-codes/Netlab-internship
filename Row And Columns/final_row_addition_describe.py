cond={
	"group" : "row operations",
	"task" : "add",
	"config" : {
		"column_list" : ["Pending Qty","Unit Amt","Total Amt"],
		"function" : "sum" #can contain mean, mode, median, variance, std deviation, unique count #assuming we get in quotes
	}
}


def row_addition_utility(self,cond,df):
	
	function=cond["config"]["function"]
	if function=="mean":
		function=="average"
	
	col=cond["config"]["column_list"]
	
	#Checks the columns ka existence.
	s = SelectedUtilities()
	msg = s.column_exists_validator(col, self.df)
	if not msg["val"]:
		return msg

	col=cond["config"]["column_list"]
	b=list(df.index)
	for i in range(len(b)):
		if b[i]=="count" or b[i]=="distinct count" or b[i]=="sum" or b[i]=="average" or b[i]=="mode" or b[i]=="median" or b[i]=="mean" or b[i]=="variance" or b[i]=="mean":
			leng=i
			break
	
	

	for i in col:
		try:
			a=df.iloc[0:leng].describe(include='all').loc[function][i]
		except:
			print(" ")
			if function=="sum":
				a=df.iloc[0:leng][i].sum()
			if function=="variance":
				a=df.iloc[0:leng][i].var()
			if function=="mode":
				a=df.iloc[0:leng][i].mode(dropna=True)[0]
			if function=="median":
				a=df.iloc[0:leng][i].median(skipna = True)
			if function=="distinct count":
				a=len(pd.unique(df.iloc[0:leng][i]))
           
		if str(function) not in df.index:
			df=df.append(pd.Series(name=function))
		df.loc[function,i]=a
    return df