import pandas as pd
dataset=pd.read_csv("null_value.csv")
df=pd.DataFrame(dataset)
print("*****************Display original Data ********************\n",df)                        #display original Data
print("*****************display NULL data as true*********************\n",df.isnull())           #display ISNULL data as true                  
print("***********display how many null value shown in numeric************\n",df.isnull().sum())  #display how many null value in numeric
print("**************remove null value display resulted output****************\n",df.dropna())   #drop null value display resulted output