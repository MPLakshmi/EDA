
# %%
import pandas as pd
 
# %%
df = pd.read_csv("HRDataset_v14.csv")
 
# %%
df
 
# %%
df.head()
 
# %%
df.shape
 
# %%
df.tail()
 
# %%
df.sample(5)
 
# %%
df.dtypes
 
# %%
df.describe()
 
# %%
df.describe(include = 'all')
 
# %%
df[df.duplicated()]
 
# %%
df.columns
 
# %%
df['Sex']
 
# %%
df['Salary']
 
# %%
df['Salary'].dtype
 
# %%
 
 
# %%
df['State']
 
# %%
df['State'].dtype
 
# %%
df['Salary'].unique()[:1000]
 
# %%
df.head()
 
# %%
df
 
# %%
df['Salary'].dtype
 
# %%
df[~df.Employee_Name.str.isnumeric()]
 
# %%
df[df.Employee_Name.str.isnumeric()]
 
# %%
type(df['Employee_Name'].str)
 
# %%
df['Employee_Name'].str
 
# %%
df_copy  = df.copy()
 
# %%
df_copy
 
# %%
df_cal_salary= df_copy[df_copy["Salary"] > 25000]
 
# %%
df_cal_salary["Employee_Name"]
 
# %%
df_copy.drop(df_copy.index[0])
 
# %%
df_copy
 
# %%
df_copy.drop(df_copy.index[0], inplace = True)
 
# %%
df_copy
 
# %%
df_copy['ManagerName']
 
# %%
df_copy['EngagementSurvey'] = df_copy['EngagementSurvey'].astype(int)
 
# %%
df_copy['EngagementSurvey']
 
# %%
df_copy
 
# %%
df['Salary'].unique()
 
# %%
df["ManagerName"] = df["ManagerName"].str.replace("Roup", "Test Mgr")
 
# %%
df["ManagerName"]
 
# %%
df
 
# %% [markdown]
#
 
# %%
df_copy["RecruitmentSource"]
 
# %%
import numpy as np
 
df_copy["RecruitmentSource"] = df_copy["RecruitmentSource"].str.replace("Employee Referral", str(np.nan))
 
# %%
df_copy
 
# %%
df_copy['Salary'] = df_copy['Salary'].astype(float)
 
# %%
df_copy
 
# %%
df_copy['Salary']
 
# %%
df_copy['Employee_Name'][5:305]
 
# %%
df_copy['Employee_Name'] = df_copy['Employee_Name'].str.replace(",", "")
 
# %%
df_copy
 
# %%
df_copy['ManagerName'].unique()
 
# %%
df_copy
 
# %%
df_copy["LastPerformanceReview_Date"] = df_copy["LastPerformanceReview_Date"].str.replace("/","-")
 
# %%
df_copy["LastPerformanceReview_Date"]
 
# %%
df_copy
 
# %%
df_copy["LastPerformanceReview_Date"].unique()
 
# %%
df_copy["Absences"] = df_copy["Absences"].astype(float)
 
# %%
df_copy["Absences"]
 
# %%
df_copy
 
# %%
df_copy.dtypes
 
# %%
df_copy
 
# %%
df_copy.columns
 
# %%
object_columns= [data_column for data_column in df_copy.columns if df_copy[data_column].dtype == 'O']
 
# %%
object_columns
 
# %%
numerical_columns = [num_column for num_column in df.columns if df[num_column].dtype != 'O']
 
# %%
numerical_columns
 
# %%
df_copy['Salary'].value_counts(normalize=True)
 
# %%
import seaborn as sns
sns.countplot(x = df['Salary'])
 
# %%
sns.countplot(x = df_copy["Absences"])
 
# %%
sns.distplot(x = df_copy["Absences"])
 
# %%
sns.histplot(x = df_copy["Absences"])
 
# %%
sns.histplot(x = df_copy["Salary"])
 
# %%
 
 
# %%
df_copy
 
# %%
sns.histplot(x = df_copy["EngagementSurvey"])
 
# %%
sns.kdeplot(x = df_copy["EngagementSurvey"])
 
# %%
df_copy
 
# %%
df_copy["GenderID"].value_counts().plot.pie(y = df_copy["GenderID"], autopct = "%1.1f%%", figsize= (12,13))
 
# %%
df_copy.value_counts()[:10]
 
# %%
 
 
# %%
 
 
# %%
df_copy.reset_index(inplace =True)
 
# %%
df_copy["GenderID"].value_counts()[:10]
 
# %%
df_copy
 
# %%
df_copy.groupby(["Employee_Name"])['Salary'].sum().sort_values(ascending=False).reset_index()
 
# %%
df_copy.groupby(["Employee_Name"])['Salary'].sum().sort_values(ascending=True).reset_index()
 
# %%
df_copy
 
# %%
df_copy[df_copy["ManagerName"] == "David Stanley"]
 
# %%
df_copy[df_copy["GenderID"] == 1]
 
# %%
df_copy
 
 
 