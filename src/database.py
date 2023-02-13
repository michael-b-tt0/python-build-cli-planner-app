import csv

from src.deadlined_reminders import DeadlinedReminder

def list_reminders():
    f = open("/home/work/Documents/vs_code_projects/python-build-cli-planner-app/reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text, date, ReminderClass):
    reminder = ReminderClass(text, date)
    

    with open("/home/work/Documents/vs_code_projects/python-build-cli-planner-app/reminders.csv", 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(reminder)


        
