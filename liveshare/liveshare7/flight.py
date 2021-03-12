"""
A program to use dictionary entries to return the most approximate values.
File: flight.py

Authors: Cary Jeffery, Jacob Ledbetter, Riley Wayne

Date: March, 10.

Assignment: Prelab 7.
"""
def closest_time(dict, time):
    """This function finds the closest time to the user's input.
    The inputs are 'dict', the entry dictionary, and 'time', the user's input.
    The output should be the dictionary entry closest to the input."""
    dif = 2400
    j = []
    for i in range(1,len(dict)+1):                  # Range that tests for the smallest difference in departures
        b = abs(time - int(dict[i]))
        if b < dif:
            dif = b
            j.append(i)                             # Builds lists of index for the smallest difference
    a = "".join(str(j))
    return a[-2:-1]                                 # Returns index of closest departure

def main():
    """The main function takes the input time and executes the closest time function
     to call on closest departure and arrival time"""
    ltime = str(input("Enter a 24-hour time: "))            # User Input for the 24 hour time
    a = ltime.split(":")
    time = int(a[0])*60 + int(a[1])                         # Building of the usable time format
    depart_dict = {1:'480', 2:'583', 3:'679', 4:'767', 5:'840', 6:'945', 7:'1140', 8:'1305'}   # Time In Minutes
    ariv_dict = {1:'10:16 a.m.', 2:'11:52 a.m.', 3:'1:31 p.m.', 4:'3:00 p.m.',
                     5:'4:08 p.m.', 6:'5:55 p.m.', 7:'9:20 p.m.', 8:'11:58 p.m.'} # 12 Hour Timescale

    tuple_num = int(closest_time(depart_dict,time))            # Closest Index Return
    mins = depart_dict[tuple_num]
    mins = int(mins)                    # Dictionary Index Call
    if mins >= 720:                     # Am vs Pm If else loop
        g = str("p.m.")
        if mins >= 780:
            mins = mins - 720
    else:
        g = str("a.m.")
    q = int(mins % 60)
    w = int(mins - q)
    e = w/60
    if q <=9:                           # Unique Double Zero correction
        q = str("0") + str(q)
    else:
        q = str(q)
    fe = str(int(e)) + ":" + str(q)+ " " + g            # Final Departure Time (Minute to 12-Hour timescale)
    print("The closest departure time is "+ fe + " arriving at "+ ariv_dict[tuple_num])     # Result Print Statement 


if __name__ == "__main__":                               # Main Function Execution
    """To Actually Run This Program"""
    main()
