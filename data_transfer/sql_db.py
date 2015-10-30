import csv
import sqlite3
import io
from operator import itemgetter
insert_spot = 3
con = sqlite3.connect('applications.db')
cur = con.cursor()
##print all the tables
##cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
cur.execute('SELECT * FROM applications_history')
##print cursor
##print (cur.fetchmany(20))

app_header = ('_id', 'timestamp', 'device_id', 'package_name', 'application_name', 'process_importance', 'process_id', 'double_end_timestamp', 'is_system_app')
app_raw_data = list(cur.fetchmany(30))
app_data = []
for tuples in app_raw_data:
          app_data.append(tuples[:insert_spot] + ('',)*3 + tuples[insert_spot:] + (0,))


con2 = sqlite3.connect('plugin_browser_history.db')
cur2 = con2.cursor()
##cur2.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
cur2.execute('SELECT * FROM plugin_browser_history')
##print (cur2.fetchmany(15))

browser_header = ('_id', 'timestamp', 'device_id', 'browser_title', 'browser_url', 'browser_visited_time')
browser_raw_data = list(cur2.fetchmany(30))
browser_data = []
for tuples in browser_raw_data:
          browser_data.append(tuples + ('',)*(len(app_header) - len(browser_header)) + (1,))


raw_header = ('_id', 'timestamp', 'device_id', 'browser_title', 'browser_url', 'browser_visited_time', 'package_name', 'application_name', 'process_importance', 'process_id', 'double_end_timestamp', 'is_system_app', 'is_website')
raw_data = []
raw_data.extend(app_data)
raw_data.extend(browser_data)

browser_data.insert(0,browser_header)
app_data.insert(0,app_header)

##sort the data
sorted_data = sorted(raw_data, key = itemgetter(1))
sorted_data.insert(0,raw_header)

with open('application_data.csv', 'w', newline = '') as writingfile:
          writefile = csv.writer(writingfile)
          writefile.writerows(app_data)

with io.open('browser_data.csv', 'w', newline = '') as writingfile:
          writefile = csv.writer(writingfile)
          writefile.writerows(browser_data)


with open('application_browser_data.csv', 'w', newline = '') as writingfile:
          writefile = csv.writer(writingfile)
          writefile.writerows(sorted_data)



