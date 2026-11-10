import csv
import datetime

#lateness = scheduled_time - actual_time
#time_stopped = out_time - in_time
#time_next_stop = in_time+1 - out_time

def timetable_calculation():
    with open("21 TimeTable - Newcastle Weekdays.csv") as gne_21:
        gne_21_list = list(csv.reader(gne_21))
        for y in range(1,115):
            for i in range (1,80):
                gne_result = gne_21_list[83+i][1+y]
                Start = datetime.datetime.strptime(gne_21_list[83+i][1+y], "%H,%M")
                Next = datetime.datetime.strptime(gne_21_list[83+i][2+y], "%H:%M")
                difference = Next - Start
                print(difference)
                print((gne_result))
            else:
                print("")

timetable_calculation()