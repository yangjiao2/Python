import urllib.request

def _web_information(_symbol, _start_date, _end_date)->str:
    SYMBOL = _symbol
    START_MONTH = _start_date.split('-')[1]
    START_DAY = _start_date.split('-')[2]
    START_YEAR = _start_date.split('-')[0]
    END_MONTH = _end_date.split('-')[1]
    END_DAY = _end_date.split('-')[2]
    END_YEAR = _end_date.split('-')[0]
    web = 'http://ichart.yahoo.com/table.csv?' + 's=' + SYMBOL + '&a=' + START_MONTH + '&b=' + START_DAY + '&c=' + START_YEAR + '&d=' + END_MONTH + '&e=' + END_DAY + '&f=' + END_YEAR + '&g=d'
    print (web)
    return web


def _get_response(website:str)->'HTTPResponse':
    response = urllib.request.urlopen(website)
    return response

def _organize_data(response: 'Response') -> list:
    _raw_data = response.read()
    _raw_string = _raw_data.decode(encoding= 'utf-8')
    _lines = _raw_data.splitlines()
    return _lines
    
def get_data(_symbol, _start_date, _end_date) ->list:
    try: 
        _information = _web_information(_symbol, _start_date, _end_date)
        _response = _get_response(_information)
        _list_of_lines = _organize_data(_response)
    except:
        print ('Fail to recieve data from website')
    else:
        return _list_of_lines


#print (get_data('GOOG', '2011-2-1', '2011-2-11'))