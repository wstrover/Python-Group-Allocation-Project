import pandas as pd
#Reading the excel file
df = pd.read_excel(r'C:\Users\vinae\Documents\pythonProject\Book1.xlsx', sheet_name='Sheet1')
#Printing the selected sheet from the excdl file
print (df)