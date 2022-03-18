import time

# print(time.ctime(100))    # convert a time expressed in seconds since epoch to a readable string
#                         epoch = when your computer thinks time began (reference point)

# print(time.time())      # return current seconds since epoch

# print(time.ctime(time.time()))    # today's time, from epoch

# time_object = time.localtime()  # localtime
# time_object = time.gmtime()     # UTC time
# local_time = time.strftime("%B %D %Y %H:%M:%S", time_object)
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y") convert a time string to a time object
# print(time_object)

# (year, month, day, hours, minutes, seconds, #day of the week, day of the year, dst)
# time_tuple = (2021, 6, 1, 15, 22, 44, 0, 0, 0)
# time_string = time.asctime(time_tuple) -- accept a tuple or time object representation
# print(time_string)


# time_tuple = (2021, 6, 1, 15, 22, 44, 0, 0, 0)
# time_string = time.mktime(time_tuple) # represent a data since epoch
# print(time_string)

