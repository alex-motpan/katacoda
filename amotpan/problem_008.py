# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
# It is much easier to understand with an example:
# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
# Note that spaces are important.
# Detailed rules
# The result_dicting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space.
# The unit of time is used in plural if the integer is greater than 1.
# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.
# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
# Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


def format_duration(seconds):
    
    result_list_1, result_list_2 =  [], []    
    time_dict, result_dict = {'year': 31536000, 'day': 86400, 'hour': 3600, 'minute': 60}, {}

    
    if seconds == 0:
        return "now"
    
    
    for k,v in time_dict.items():
        if seconds // v:
            result_dict[k] =  seconds // v
            seconds -= v * (seconds // v)
    
    
    # # Years
    # year = seconds // 31536000
    # if year:
    #     seconds -= year * 31536000
    #     result_dict['year'] = year
    
    
    # # Days
    # day = seconds // 86400
    # if day:
    #     seconds -= day * 86400
    #     result_dict['day'] = day


    # # Hours
    # hour = seconds // 3600
    # if hour:
    #     seconds -= hour * 3600
    #     result_dict['hour'] = hour


    # # Minutes
    # minutes = seconds // 60
    # if minutes:
    #     seconds -= minutes * 60
    #     result_dict['minute'] = minutes


    # Seconds
    seconds %= 60
    if seconds:
        result_dict['second'] = seconds
   
   
    ###########  
    for k, v in result_dict.items():
        if v > 1:
            result_list_1.append(f'{v} {k}s')
        else:
            result_list_1.append(f'{v} {k}')


    ###########
    if len(result_list_1) > 1:   
        for key in range(len(result_list_1)):
            if key == len(result_list_1) - 2:
                result_list_2.append(result_list_1[key])
                result_list_2.append('and')
            elif key == len(result_list_1) - 1:
                result_list_2.append(f'{result_list_1[key]}')
            else:
                result_list_2.append(f'{result_list_1[key]},')
        return ' '.join(result_list_2)
    else:
        return ''.join(result_list_1)
    
    
tests = {1:  "1 second", 62: "1 minute and 2 seconds", 120: "2 minutes", 3600: "1 hour", 3662: "1 hour, 1 minute and 2 seconds", 917634512: "29 years, 35 days, 18 hours, 28 minutes and 32 seconds", 0: "now"}
for k, v in tests.items():
    if format_duration(k) == v:
        print(f'OK -> format_duration({k}) == {v}')
    else:
        print(f'NOT OK -> format_duration({k}) != {v}')
        print(format_duration(k))