import indicator

# already download the list
Menu = '1. According to the price moves above the N-day simple moving average\n2. According to the N-day directional indicator moves above a chosen value '

def _apply_simple_moving_average(list_of_lines:list)-> list:
    _initial_report_information = directional_strategy()
    return _initial_report_information.collect_data(list_of_lines)

def _apply_directional_average(list_of_lines:list)-> list:
    _initial_report_information
    return _initial_report_information.collect_data(list_of_lines)
            
def _get_strategy(list_of_lines)->str:
    print (Menu)
    while True:
        try:
            result = eval(input('Strategy (Answer should be 1 or 2):'))
            #check
        except:
            raise InvalidInputError
        else:
            
            if result == 1:
                self._strategy = 'Simple'
                indicator.simple._excute(list_of_lines[1:])
            elif result == 2:
                self._strategy = 'Directional'
                indicator.directional._excute(list_of_lines[1:])
                


