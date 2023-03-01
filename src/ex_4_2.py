""" ex_4_2.py """
from datetime import datetime
from datetime import timedelta


def get_shutdown_events(logfile):
    """ Function 1"""
    f = open(logfile, 'rt')
    x = list()

    for i in f:
        x.append(i)
    final_lis = list()
    for i in x:
        if i.split()[4] == 'initiated.':
            final_lis.append(i[:-2])
    return final_lis


def logstamp_to_datetime(datestr):
    """ Function 2"""
    input_str = datestr
    format_str = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(input_str, format_str)


def time_between_shutdowns(logfile):
    """ Function 3"""
    x = get_shutdown_events(logfile)
    y = list()
    for i in x:
        u = i.split()[1]
        y.append(logstamp_to_datetime(u))
    return y[-1]-y[0]
