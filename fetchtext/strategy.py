"""
A module that implements the signal strategies.
These must be implemented as classes
"""

class simple:
    
    def _excute(list_of_indicators, list_of_lines):
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
    
##    def _excute(list_of_lines):
##        _raw_list = []
##        _day = simple._day()
##        _indicators = simple._create_indicator(_day, list_of_lines)
##        print (_indicators)
##        _signal = simple._create_signal(_indicators, list_of_lines)
##        print (_signal)
##        for i in range(len(list_of_lines)):
##            _raw_list.append([list_of_lines[i][0], float(list_of_lines[i][-1].strip()), _indicators[i], _signal[i]])
##        return _raw_list


class directional:


    def _sell():
        _sell_price = eval(input ('Sell:'))
        return _sell_price
    def _buy():
        _buy_price = eval(input ('Buy:'))
        return _buy_price

    
    def _excute(list_of_indicators, _buy_price, _sell_price):
        _buy_price = directional._buy()
        _sell_price = directional._sell()
        result = []
        for i in range(len(list_of_indicators)):
            if list_of_indicators[i] < _sell_price:
                result.append ('SELL')
            elif list_of_indicators[i] > _buy_price:
                result.append ('BUY')
            else:
                result.append ('')
        return result
        

##    def _excute(list_of_lines):
##        _raw_list = []
##        _buy_price = directional._buy()
##        _sell_price = directional._sell()
##        _day = directional._day()
##        _directional_summed_close_price = directional._create_directional_summed_close_price (list_of_lines)
##        _indicators = directional._create_indicator(_day, _directional_summed_close_price)
##        #print ('indicator',_indicators)
##        sell = directional._sell()
##        buy = directional._buy()
##        _signal = directional._create_signal(_indicators, sell, buy)
##        #print ('signal',_signal)
##        for i in range(len(list_of_lines)):
##            _raw_list.append([list_of_lines[i][0], float(list_of_lines[i][-1].strip()), _indicators[i], _signal[i]])
##        return _raw_list