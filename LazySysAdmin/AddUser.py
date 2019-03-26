import csv
import os
def runner(filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # response = os.system("ping -c 1 192.168.8.1")
        my_list=[]
        commands = []
        for row in readCSV:
            fullName = row[0]
            words = row[0].split()
            letters = [word[0] for word in words]
            initials = "".join(letters)
            userCommand = "useradd " + initials + " -g " + row[3] + " -c " + "\"" + row[0] + "\""
            commands.append(userCommand)
            my_list.append(row[3])
        my_list = sorted(set(my_list))
        for i in my_list:
            groupCommand = "groupadd " + i
            commands.append(groupCommand)
    commands.reverse()
    print "Running the following commands:"
    for i in commands:
        #os.system(i)
        print i
    return commands

