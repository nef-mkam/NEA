import csv

#lateness = scheduled_time - actual_time
#time_stopped = out_time - in_time
#time_next_stop = in_time+1 - out_time

def timetable_calculation():
    with open("21 TimeTable - Newcastle Weekdays.csv") as gne_21:
        gne_21_list = list(csv.reader(gne_21))
        for y in range(1,80):
            for i in range (2,20):
                gne_result = gne_21_list[83+i][1+y]
                print((gne_result))
        gne_21.close()

timetable_calculation()