import pandas as pd
df = pd.read_csv('students_performance.csv')
#print(df.columns)
#print(df[['StudentName','Attendance']])
#print(df.iloc[0:5, [0, 1, 2]])
#print(df)
#students=df[df['Course'].isin(['MCA','BTECH'])]
#print(students)
#student_with_a_name=df[df['StudentName'].str.contains('a')]
#print(student_with_a_name)
#top_students=df.sort_values(by='FinalMarks', ascending=False)
#print(top_students)
x=df.sort_values(by=['Result','FinalMarks'], ascending=[True, False])
print(x)    