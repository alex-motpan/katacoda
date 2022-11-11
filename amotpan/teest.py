def format_duration(seconds):
    time_dict = {'years': 31536000, 'days': 86400, 'hours': 3600, 'minutes': 60}
    result_dict = {}
    for k,v in time_dict.items():
        print(k, v, seconds)
        if seconds // v:
            result_dict[k] =  seconds // v
            seconds -= v * (seconds // v)
    return result_dict
print(format_duration(7260))