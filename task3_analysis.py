import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns

#load data from cleaned data
df=pd.read_csv("Level1/cleaned_quotes.csv")

#Statistics
numerical_cols=["Author_Encoded","Tag_Encoded","Quote_Length","Quote_Length_Scaled"]
stats=df[numerical_cols].describe().transpose()

stats["median"]=df[numerical_cols].median()
stats["skewness"]=df[numerical_cols].skew()

print("\n"+"="*50)
print("Summary Statistics: ")
print("="*50)
print(stats[["count","mean","std","min","median","max","skewness"]])
print("-"*50)
print(f"\nTotal Quotes Analyzed:{len(df)}")
print(f"Average   Quote Length: {df['Quote_Length'].mean(): .2f} characters")
print("="*50)

#setting visual style
sns.set_theme(style="whitegrid")
fig,axes=plt.subplots(2,2,figsize=(15,12))

#distribution of quote lengths
sns.histplot(df["Quote_Length"],bins=8,kde=True,color="teal",ax=axes[0,0])
axes[0,0].set_title("Distribution of Quote Lengths",fontsize=14,fontweight="bold")

#quote count per author
author_counts=df["Author"].value_counts().reset_index()
author_counts.columns=["Author","Count"]
sns.barplot(data=author_counts,x="Count",y="Author",palette="viridis",ax=axes[0,1])
axes[0,1].set_title("Quote count by Author",fontsize=14,fontweight="bold")

#Quote length per author
sns.boxplot(data=df,x="Author",y="Quote_Length",hue="Author",palette="Set2",ax=axes[1,0])
axes[1,0].tick_params(axis="x",rotation=45)
axes[1,0].set_title("Quote Length Variability per Author",fontsize=14,fontweight="bold")

#Correlation Heat Map
numerical_cols=["Author_Encoded","Tag_Encoded","Quote_Length","Quote_Length_Scaled"]
corr=df[numerical_cols].corr()
sns.heatmap(corr,annot=True,cmap="coolwarm",fmt=".2f",linewidths=0.5,ax=axes[1,1])
axes[1,1].set_title("Feature Correlation Matrix",fontsize=14,fontweight="bold")



plt.tight_layout()
plt.savefig("task3_visual_report.png")
print("\n[Success] Diagram saved as 'task3_visual_report.png'")
plt.show()