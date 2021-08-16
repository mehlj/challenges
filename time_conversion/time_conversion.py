#!/usr/bin/env python3

def hour_conversion(hour, suffix):
  """
  Accepts an hour integer and a string defining AM or PM, and returns the 24-hour equivalent
  Ex: hour_conversion(06, "PM") -> 18
  @param hour: An integer defining the hour at that time
  @param suffix: A string defining AM or PM at that time
  @return: An integer converted to the 24 hour format 
  """
  if (hour < 12) and (suffix == "PM"):
    return hour + 12
  elif (hour < 12) and (suffix == "AM"):
    return "%02d" % (hour,)
  elif hour == 12 and (suffix == "PM"):
    return hour
  else:
    return "%02d" % (hour - 12,) # include leading zero
    
  

def time_conversion(time):
  """
  Accepts a string containing a 12-hour AM/PM format time and returns the 24 hour format equivalent
  Ex: time_conversion("07:05:45PM") --> 19:05:45
  @param time: A string containing the time in 12 hour format
  @return: A string containing the time in a 24 hour format
  """
  # split up time string for parsing
  time_split = time.split(":")

  # determine AM/PM
  if (time_split[2].find('AM') != -1):
    suffix = "AM"
  else:
    suffix = "PM"

  military_time = str(hour_conversion(int(time_split[0]), suffix)) + ":" + time_split[1] + ":" + time_split[2]

  # remove AM/PM
  return military_time.replace(suffix, '')
    
  
if __name__ == '__main__':
  print(time_conversion("06:40:03AM"))
