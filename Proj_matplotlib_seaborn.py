import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_one = pd.DataFrame(
    {
        "Year": [2021, 2022, 2023, 2024, 2025],
        "Apple": [40, 30, 50, 70, 60],
        "Samsung": [45, 45, 60, 75, 60],
        "Moto": [100, 70, 55, 80, 85],
        "Realme": [10, 20, 20, 20, 20]
    }
)

print(df_one)

# plt.figure(figsize=(12,4),facecolor="lightblue")
# plt.plot(df_one["Year"], df_one["Apple"], label="Apple")
# plt.plot(df_one["Year"], df_one["Samsung"], label="Samsung")
# plt.plot(df_one["Year"], df_one["Moto"], label="Moto")
# plt.title("Mobile Phone Sales Report")
# plt.xlabel("Sales Year")
# plt.ylabel("Sales count")
# plt.legend()
# plt.show()


total = df_one[["Apple","Samsung","Moto","Realme"]].sum()
print(total.index)
plt.pie(total, labels=total.index, autopct="%1.1f%%", explode=(0.1,0,0,0), shadow=True)
plt.title("Mobile Phone Sales Report")
plt.show()

#df_one.plot(kind="bar", x="Year")
#plt.show()

#sns.histplot(data=df_one, x=df_one["Apple"], kde=True )
#sns.scatterplot(data=df_one, x=df_one["Year"], y=df_one["Apple"])
#sns.barplot(data=df_one, x=df_one["Year"], y=df_one["Samsung"])
# plt.xlabel("Year")
# plt.ylabel("Sales")
# plt.show()