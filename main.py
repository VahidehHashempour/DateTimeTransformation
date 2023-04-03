# CS 5103 Course Project: Software Engineering Practice
# By Vahideh Hashempour
# Data Time Transformation
# Program will transform the given datetime string to different formats.

from datetime import datetime

# Function to return current date and time
def current_date_time():
    return datetime.now()
  
# Function to return datetime string format 1 from a datetime object
# New feature name of day in the week added
def datetime_string_1(datetime_object):
    return datetime_object.strftime("%d/%m/%Y %A %H:%M:%S")
  
# Function to return datetime string format 2 from a datetime object
# New feature name of day in the week added
def datetime_string_2(datetime_object):
    return datetime_object.strftime("%d-%m-%Y %A %H:%M:%S") 
  
# Function to return datetime string format 3 from a datetime object
# New feature name of day in the week added
def datetime_string_3(datetime_object):
    return datetime_object.strftime("%d/%m/%Y %A %I:%M:%S %p")  
  
# Function to return datetime string format 4 from a datetime object
# New feature name of day in the week added
def datetime_string_4(datetime_object):
    return datetime_object.strftime("%d-%m-%Y %A %I:%M:%S %p")  
  
# Function to print date and time in 4 different formats
def print_datetime(datetime_object):
    print('Date and Time String 1:', datetime_string_1(datetime_object))
    print('Date and Time String 2:', datetime_string_2(datetime_object))
    print('Date and Time String 3:', datetime_string_3(datetime_object))
    print('Date and Time String 4:', datetime_string_4(datetime_object))

now = current_date_time()
print_datetime(now)

