import pandas as pd

df_friends = pd.DataFrame(
    data={
        "Name" : ["Karthik", "Arun", "Bhoopathi", "Logu"],
        "City" : ["Vanavasi", "Salem", "Salem", "Elampillai"],
        "Age" : [35, 36, 34, 32],
        "Company" : ["Zensar", "Virtusa", "Verison", "HCL"]
    }
)


df_friends["Salary"]=[20000, 30000, 40000, 50000]
df_friends["Salary"]+=2000
#print(df_friends[["Name","City"]])

#df_friends.add({"Name":"Murali", "City":"Salem", "Age":32, "Company":"TCS", "Salary":54000})
df_friends.loc[len(df_friends)]={"Name":"Murali", "City":"Salem", "Age":32, "Company":"TCS", "Salary":54000}


df_new = pd.DataFrame(
    data=[{
        "Name":"SK", 
        "City":"Elampillai", 
        "Age":37, 
        "Company":"TCS", 
        "Salary":51000
        }]
    )

df_friends=pd.concat([df_friends, df_new], ignore_index=True)


df_new = pd.DataFrame(
    data=[{
        "Name":"Mana", 
        "City":"Madurai", 
        "Age":43, 
        "Company":"DXC", 
        "Salary":59000
        }]
    )

df_friends = pd.concat([df_friends.iloc[0:1], df_new, df_friends.iloc[1:]]).reset_index(drop=True)
#df_friends = df_friends.set_index("Name")
#print(df_friends)

#df_csv = pd.read_csv("Sample.csv", na_values=["N/A","n.a"])

# def replace_val(val):
#     return 1000 if (val == "N/A" or val == "n.a") else val

#df_csv = pd.read_csv("Sample.csv", converters={"Salary":replace_val})

df_csv = pd.read_csv("Sample.csv")
df_csv = df_csv.replace({"Salary":[-8000,-9000]}, 1000)
#print(df_csv)

df_new = pd.DataFrame(
    data=[{
        "Name":"GR", 
        "City":"Salem", 
        "Age":35, 
        "Company":"Zensar", 
        "Salary":90000
        }]
    )

df_new.to_csv("New.csv", index=False)
df_friends.to_csv("New.csv", mode='a', index=False, header=False)

df_new = pd.read_csv("New.csv")
#print(df_new)

# df_g = df_new.groupby("City")
# print(df_g)

# for key, data in df_g:
#     print("Group:", key)
#     print("Data: ", data.Salary.max())

def by_sal_rang(df, i , col):
    if df[col].iloc[i] <= 50000:
        return "Less than 50K"
    else:
        return "More than 50K"
    
df_g = df_new.groupby(lambda i: by_sal_rang(df_new, i, "Salary"))

for key, data in df_g:
    print("Group:", key)
    print("Data:", data)
