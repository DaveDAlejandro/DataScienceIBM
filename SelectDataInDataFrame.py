import pandas as pd
import numpy as np

'''
    x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
        'Salary':[100000, 80000, 50000, 60000]}


    df = pd.DataFrame(x)

    print(df)

    x = df[["ID"]]
    print(x)
    print(type(x))

    z = df[["Department", "Salary", "ID"]]
    print(z)
'''
#EXCERCISE's from LAB IBM
#Excercise 1
#Problem 1: Create a dataframe to display the result as below:

studentDic = {"Studendt":("David", "Samule", "Terry", "Evan"), 
             "Age":(27, 24, 22, 32), 
             "Country":("UK", "Canada", "China", "USA"), 
             "Course":("Python", "Data Structures", "Machine Learning", "Web Development"),
             "Marks":(85, 72, 89, 76) 
            }

studentDF = pd.DataFrame(studentDic)
print(studentDF) #Correct. Completed

#Problem 2: Retrieve the Marks column and assign it to a variable

marksColumn = studentDF[["Marks"]]
print(marksColumn)

#Problem 3: Retrieve the Country and Course columns and assign it to a variable 

column3 = studentDF[["Country", "Course"]]
print(column3)



#Excercise 2:
#Problem 1: Use the loc() function,to get the Department of Jane in the newly created dataframe df2.

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 
     'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)

#That's pretty much all the important exercises of the lab. 
