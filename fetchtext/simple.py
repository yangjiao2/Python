lis = open('table.csv','r')
list_of_lines = lis.readlines()
##print (list_of_lines[1:])
result = []
for line in list_of_lines:
    ll = line.split(',')
    result.append (ll)


class simple:

    def __initial__(self, day):
        self._day = day
        
    def _day(self):
        return self._day

    def _sum_close_price(day, current_day, list_of_lines):
        summary = 0
        for i in range(day):
            summary += float(list_of_lines[current_day - i][-1])
        return summary

    def _create_indicator(day, list_of_lines):
        result = []
        for i in range(len(list_of_lines)):
            if i < day:
                result.append(0)
            else:
                result.append(simple._sum_close_price(day, i, list_of_lines)/ day)
        return result

    def _create_signal(list_of_indicators, list_of_lines):
        result = []
        for i in range(len(list_of_indicators)):
            if list_of_indicators[i] == None:
                result.append('')
            elif list_of_indicators[i] > float(list_of_lines[i][-1]):
                result.append ('SELL')
            elif list_of_indicators[i] < float(list_of_lines[i][-1]):
                result.append ('BUY')
            else:
                result.append ('')
        return result
             

    def _excute(list_of_lines, day):
        _raw_list = []
        _indicators = simple._create_indicator(day, list_of_lines)
        print (_indicators)
        _signal = simple._create_signal(_indicators, list_of_lines)
        print (_signal)
        for i in range(len(list_of_lines)):
            _raw_list.append([list_of_lines[i][0], float(list_of_lines[i][-1].strip()), _indicators[i], _signal[i]])
        return _raw_list


class directional:

    def __initial__(self, day):
        self._day = day
        self._sell_price = _sell()
        self._buy_price = _get_buy_price()

    def _day(self):
        return self._day
    def _sell():
        _sell_price = eval(input ('Sell:'))
        return _sell_price
    def _buy():
        _buy_price = eval(input ('Buy:'))
        return _buy_price


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
        

    def _create_indicator(day, _directional_summed_close_price):
        result = []
        for i in range(len(_directional_summed_close_price)):
            if i == 0:
                result.append(0)
            
            else:
                result.append(directional._sum_close_price(day, i, _directional_summed_close_price))
        return result

    def _create_signal(list_of_indicators, _buy_price, _sell_price):
        result = []
        for i in range(len(list_of_indicators)):
            if list_of_indicators[i] < _sell_price:
                result.append ('SELL')
            elif list_of_indicators[i] > _buy_price:
                result.append ('BUY')
            else:
                result.append ('')
        return result
        

    def _excute(list_of_lines, day):
        _raw_list = [[]] * len(list_of_lines)
        _buy_price = _buy()
        _sell_price = _sell()
        _day = _day()
        _directional_summed_close_price = _create_directional_summed_close_price (list_of_lines)
        _indicators = _create_indicator(_day, _directional_summed_close_price)
        _signal = _create_signal(_indicators, _buy_price, _sell_price)
        for i in range(len(list_of_lines)):
            _raw_list[i].extend([list_of_lines[0], list_of_lines[-1], _indicators[i], _signal[i]])
        return _raw_list        

    def _excute(list_of_lines, day):
        _raw_list = [] 
        _directional_summed_close_price = directional._create_directional_summed_close_price (list_of_lines)
        _indicators = directional._create_indicator(day, _directional_summed_close_price)
        #print ('indicator',_indicators)
        sell = directional._sell()
        buy = directional._buy()
        _signal = directional._create_signal(_indicators, sell, buy)
        #print ('signal',_signal)
        for i in range(len(list_of_lines)):

            _raw_list.append([list_of_lines[i][0], float(list_of_lines[i][-1].strip()), _indicators[i], _signal[i]])
        return _raw_list
        
indicators_list = [directional, simple]
for indicator in indicators_list:
    a = indicator()
    b = indicator._excute(result[1:9], 2)
    for line in b:
        print ('{}  {:6.2f} {:6.2f} {:4}'.format(line[0],line[1], line[2], line[3]))
