import csv
import json

##csvfile = open('precipObject_stats.csv', 'r')
##jsonfile = open('precipObject_stats.json', 'w')
##
##fieldnames = ("object_id","object_avg_intensity","object_median_intensity","object_stddev_intensity","object_max_intensity","object_cent_lat","object_cent_lon","object_volume","object_duration","object_speed	object_startTime","object_endTime","object_start_lat_centroid","object_start_lon_centroid","object_end_lat_centroid","object_end_lon_centroid")
##reader = csv.DictReader( csvfile, fieldnames)
##for row in reader:
##    json.dump(row, jsonfile)
##    jsonfile.write('\n')



txtfile = open('precipObject_list_001.txt', 'r')
jsonfile = open('recipObject_list_001.json', 'w')

fieldnames = ("object_id","latitude","longtitude","time","intensity","location")
reader = csv.DictReader( txtfile, fieldnames)
i = 0
for row in reader:
    print(i)
    i = i+1
    row['id'] = i
    timelist = row['time'].split(' ')
    row['time'] = "datetime("+'"' + timelist[1] + 'T' + timelist[2] + "\")"
    row['location'] = "point("+"\"" + row['latitude'].split(' ')[-1] + ',' + row['longtitude'].split(' ')[-1] + "\")"
    json.dump(row, jsonfile)
    jsonfile.write('\n')
    if i == 10:
        break
print ('Finish dump')