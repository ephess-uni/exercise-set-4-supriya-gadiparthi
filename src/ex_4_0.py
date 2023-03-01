""" ex_4_0.py """
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
