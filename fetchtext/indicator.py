##lis = open('table.csv','r')
##list_of_lines = lis.readlines()
####print (list_of_lines[1:])
##result = []
##for line in list_of_lines:
##ll = line.split(',')
##result.append (ll)

"""A module that implements the two indicators.
These are probably best implemneted as functions that
take
a list of prices, in ascending order of date,
and whatever other necessary parameters you think they need
(e.g., the number of days for the simple moving average) and
returns
a list of the indicator's value on each date represented in the list of prices.
"""

day = eval(input('Days:'))



def _sum_close_price(day, current_day, list_of_lines):
    summary = 0
    for i in range(day):
        summary += float(list_of_lines[current_day - i][-1])
    return summary

def _simple_indicator(list_of_lines):

    day = _day
    result = []
    for i in range(len(list_of_lines)):
        if i < day:
            result.append(0)
        else:
            result.append(simple._sum_close_price(day, i, list_of_lines)/ day)
    return result


         



def _create_directional_summed_close_price (list_of_lines):
    summary = []
    for i in range(len(list_of_lines)):
        if i == 0:
            summary.append (0)
        elif float(list_of_lines[i-1][-1]) < float(list_of_lines[i][-1]):
            summary.append(1)
        elif float(list_of_lines[i-1][-1]) > float(list_of_lines[i][-1]):
            summary.append(-1)
        else:
            summary.append (0)
    return summary
            
def _sum_close_price(day, current_day, _directional_summed_close_price):
    summary = 0
    for i in range(day):
        summary += _directional_summed_close_price[current_day - i]
    return summary
    

def _directional_indicator(day, _directional_summed_close_price):
    day = _day
    result = []
    for i in range(len(_directional_summed_close_price)):
        if i == 0:
            result.append(0)
        
        else:
            result.append(directional._sum_close_price(day, i, _directional_summed_close_price))
    return result



    
##indicators_list = [directional, simple]
##for indicator in indicators_list:
##a = indicator()
##b = indicator._excute(result[1:9])
##for line in b:
##    print ('{}  {:6.2f} {:6.2f} {:4}'.format(line[0],line[1], line[2], line[3]))
