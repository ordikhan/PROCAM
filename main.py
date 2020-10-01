from ProcamFunction import Procam
import pandas

# load data set
df = pandas.read_excel('D:\\....xlsx')
print(df.head())

# set column
age = df.iloc[:, 0]
diabetes = df.iloc[:, 0]
smoker = df.iloc[:, 0]
bloodPersore = df.iloc[:, 0]
familyHistory = df.iloc[:, 0]
Ldl = df.iloc[:, 0]
triglycerides = df.iloc[:, 0]

# call function
procam = Procam()
risk = procam.ProcamRisk(age, diabetes, smoker, bloodPersore, Hdl, familyHistory, Ldl, triglycerides)
print(risk)