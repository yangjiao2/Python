import os
import operator

total_people = 0
total_datafiles = 0
sent_messages = 0
sent_messages1 = 0
inbox_messages = 0
folder_names = dict()
datafiles = dict()
main_path = "C:\\Users\\Yang\\Enron_mail\\maildir"

def dealingwithfolders(people, path, counter):
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            counter += dealingwithfolders(people, os.path.join(path, folder), counter)
        elif os.path.isfile(os.path.join(path, folder)):
            counter += 1
            dealingwithsentmessages(people, os.path.join(path, folder))
    return counter

def dealingwithsentmessages(people, path):
    first_two = 0
    for line in open(path):
        if first_two < 2 and (str(line).lower().startswith("from") or str(line).lower().startswith("x-from")):
            first_two += 1
            if people.lower() in str(line):
                global sent_messages
                sent_messages = sent_messages + 1
##                print (path, people, line)
                return
                
total_people = len(os.listdir(main_path))

total_people = len(os.listdir(main_path))
for peoplefolder in os.listdir(main_path):
    people_counter = 0
    print ("\nNow processing people " + str(peoplefolder))
    people = peoplefolder.split("-")[0]
    for messagefolder in os.listdir(os.path.join(main_path, peoplefolder)):
        counter = 0
        current_folder = os.path.join(main_path, peoplefolder, messagefolder)
        if os.path.isdir(current_folder):
            folder_names[peoplefolder] = messagefolder
            new_counter = dealingwithfolders(people, current_folder, counter)
            counter += new_counter
            if "inbox" in current_folder.lower():
                inbox_messages = inbox_messages + counter
            if "sent" in current_folder.lower():
                sent_messages1 = sent_messages1 + counter
        elif os.path.isfile(messagefolder):
            print ("Error: uncategorized file within message folder " + str(current_folder))
            counter += 1
        else:
            print ("Error: uncategorized file/folder type " + str(current_folder))
        print ("-- " + current_folder + " (" + str(counter) + " file)")
        total_datafiles += counter
        people_counter += counter
    datafiles[peoplefolder] = people_counter


sorted_datafiles = sorted(datafiles.items(), key=operator.itemgetter(1))

print("\n\n\n=====================================")
print("total_people:", total_people)
print("total_datafiles: ", total_datafiles)
print("sent_messages: ", sent_messages ,", ", sent_messages1)
print("inbox_messages: ", inbox_messages)
print("largest datafiles: ", sorted_datafiles[-10:])
print("=====================================")


