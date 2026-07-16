# Low attendance report
'''
[
[
    "StudentName",
    "Attendance",
    "FinalMarks",
    "Result"
]]
'''
import pandas as pd
df = pd.read_csv('students_performance.csv')

#df1 = df[df["Attendance"] < 75]

report=df[df["Attendance"] < 75][['StudentName','Attendance','FinalMarks','Result']]

print(report)

report.to_csv('low_attendance_report.csv', index=False)

