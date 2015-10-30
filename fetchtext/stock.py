import urllib.request
import strategy
import download
import indicator
import time


Menu = '1. According to the price moves above the N-day simple moving average\n2. According to the N-day directional indicator moves above a chosen value '

class InvalidInputError(Exception):
    pass


class Stock:


    def _get_ticket_symbol()->str:
        while True:
            
            result = input('Ticket Symbol:').strip().upper()
            if len(result) == 4:
                return result
            else:
                raise InvalidInputError

    def check_date(date)-> bool:
        if date[4] == '-' and date[-3] == '-':
            return False
        checking = date.split('-')
        now_time = time.ctime(time.time())
        now_time_list = now_time.split()
        DIC = {'Jan': 1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        now_month = DIC[now_time_list[1]]
        now_day = DIC[now_time_list[2]]
        now_year = DIC[now_time_list[-1]]
        if checking[0] == now_year and checking[1] <= now_month and checking[2] <= now_day:
            return True
        elif checking[0] <= now_year and checking[1]<=12 and checking[2] <= 31:
            return True
        else:
            return False


    def _get_start_date()->str:
        while True:
            
            result = input('Start date (YYYY-MM-DD):').strip()
            if check_date(result):
                return result
            else:
                raise InvalidInputError


    def _get_end_date()->str:
        while True:
        
            result = input('End date (YYYY-MM-DD):').strip()
            if check_date(result):
                return result
            else:
                raise InvalidInputError
    # check start date <  end date

    
    def _symbol():
        self._symbol = _get_ticket_symbol()
        return self._symbol

    def _start_date():
        self. _start_date = _get_start_date()
        return self._start_date

    def _end_date():
        self._end_date = _get_end_date()
        return self._end_date

    
    def _get_strategy()->int:
        print (Menu)
        while True:
            strategy_choice = eval(input('Strategy (Answer should be 1 or 2):'))
            if type(result) == int and result <=2:
                return strategy_choice
            else:
                raise InvalidInputError
            
    def _get_indicators(list_of_lines, strategy_choice)->list:    
        if strategy_choice == 1:

            result = indicator.simple_indicators(list_of_lines[1:])
            return result
        
        elif strategy_choice == 2:

            result = indicator.directional_indicators(list_of_lines[1:])
            return result

    def _get_signal_strategy(list_of_lines, indicators, strategy)->list:
        indicators_list  = [directional, simple]
        result = indicator_list[_strategy]._excute(indicators, list_of_lines)
        return result

    def _organize_lines(list_of_lines, indicators, signal)->list:
        _raw_list = []
        for i in range(len(list_of_lines)):
            _raw_list.append([list_of_lines[i][0], float(list_of_lines[i][-1].strip()), indicators[i], signal[i]])
        return _raw_list
        
        
            
      
    def run_program():
        
        stock = Stock()
        _initial_lines = download.get_data(stock._symbol, stock._start_date, stock._end_date)
        _strategy = stock._get_strategy()
        _indicators = _get_indicators(_initial_lines, _strategy)
        _day = indicator._day
        _signal_strategy =  _get_signal_strategy(_initial_lines, indicators, _strategy)
        _final_lines = _organize_lines(_initial_lines, _indicators, _signal_strategy)
        
##        choice = strategy()
##        _initial_report = s.strategy(stock._strategy)
##        print_formatted_output(_initial_stock, _initial_report)

if __name__ == '__main__':
    Stock.run_program()