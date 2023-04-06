from datetime import datetime

def get_timestamp():
    now = datetime.now()
    datestr = '{0}-{1}-{2}-{3}-{4}-{5}'. \
        format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    return datestr
