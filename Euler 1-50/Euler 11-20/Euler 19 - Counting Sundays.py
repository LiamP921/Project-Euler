""" calculates the no. of Sundays that fell on the first of the month during the years 'n-m'. """
def firstSundays(starting_day, n, m):
    week_code = {0:"Sunday", 1:"Monday", 2:"Tuesday",3: "Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
    """ day of 1/1/'n' """
    week_code = starting_day
    """ days/month on non-leap years. """
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    sunday_count = 0
    
    for current_year in range(n, m + 1):
        """ update day count of Feb. according to leap years. """
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            months[1] = 29
        else:
            months[1] = 28
    
        for y in months:
            if week_code == 0:
                sunday_count += 1
            """ reflects the no. of current month days; 'week_code' will now be the correct day for the 1st of next month. """
            week_code = (week_code + y) % 7
    
    print(sunday_count)

""" '1/1/1901' was a Tuesday. """
firstSundays(2, 1901, 2000)
