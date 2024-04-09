"""
Counting Sundays
------------------
1 Jan 1900 was a Monday. September, April, June and November all have thirty days. All 
the rest have thirty-one, saving February alone, which has twenty-eight. And on leap years, 
twenty-nine. A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it's divisible by 400. 
Calculate how many Sundays fell on the first of the month during the twentieth century.
"""

def sundays_count(start_year, end_year):
    """ adaptation of Zeller's Congruence to find the day on which January 1st fell in 
    the given start year. This considers leap years and the number of years that have passed since 
    1 AD. """
    start_day_code = (start_year + (start_year - 1) // 4 - (start_year - 1) // 100 + (start_year - 1) // 400) % 7 # % 7 ensures a day corresponds with a 7 day week
    """ number of days per month on a non-leap year. """
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sunday_count = 0
  
    for current_year in range(start_year, end_year + 1):
        """ update day count of February if it's a leap year. """
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            months[1] = 29
        else:
            months[1] = 28
  
        for days_in_month in months:
            if start_day_code == 0:
                sunday_count += 1
            """ update for the next month. """
            start_day_code = (start_day_code + days_in_month) % 7
  
    return sunday_count

if __name__ == "__main__":
  print(sundays_count(1901, 2000))

""" '1/1/1901' was a Tuesday. """
firstSundays(2, 1901, 2000)
