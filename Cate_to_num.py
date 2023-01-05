import pandas as pd
dataset=pd.read_csv("cate_to_num.csv")
df=pd.DataFrame(dataset)
print("***************Original Data******************\n",df)

df['Education'].replace(["Degree","PG","Diploma"],[10,20,30],inplace=True)

print("***************Resulted Data******************\n",df)


 