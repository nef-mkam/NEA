
#lateness = scheduled_time - actual_time
#time_stopped = out_time - in_time
#time_next_stop = intime+1 - out_time

def timetable_calculation():
    with open("21 TimeTable - Newcastle Weekdays.csv") as gne_21:
        print(gne_21.read([2,2]))
        gne_21.close()

    print(("This is here"))



timetable_calculation()