from TASKS.Dasaolu_Samuel_task9.TASK2.task9 import month

dictionary = {
    "ongoing_tasks": {
        "TASK 1": "gjhagsd hjgsdgj",
        "TASK 2": "task1",
        "TASK 3": "task2",
        "TASK 4": "task3"
    },
    "completed_tasks": {}
}
# del dictionary['ongoing_tasks']
# print(dictionary)
import datetime
today = str(datetime.datetime.today().date())

dob = '2003-06-17'
dob_yy_mm_dd = dob.split('-')
today_yy_mm_dd = today.split('-')

age_in_years = int(today_yy_mm_dd[0]) - int(dob_yy_mm_dd[0])
# age_in_months =