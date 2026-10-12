import pandas as pd

#lateness = scheduled_time - actual_time
#time_stopped = out_time - in_time
#time_next_stop = in_time+1 - out_time

def timetable_calculation():
    gne_21 = pd.read_csv('21 TimeTable - Newcastle Weekdays.csv')
    with open("21 TimeTable - Newcastle Weekdays.csv") as gne_21:
        gne_21.close()
        temp = list(csv.reader(gne_21))
        print(("This is here"))

timetable_calculation()