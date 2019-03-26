import error_log
import access_log
import AddUser
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Lazy System Admin', font='starwars'), attrs=['bold'])
print("\nMade By Omar Yassin\n")
print("What are you trying to do today:\n ")
print("1: Print me HTTPD error log\n")
print("2: Print me HTTPD access log\n")
print("3: Add new accounts from my csv file\n")
user_input = int(raw_input("Enter the number of the option you want to excute: "))
print
if (user_input== 1):
    result=error_log.runner()
    print result

elif (user_input==2):
    result = access_log.runner()
    print result

elif (user_input==3):
    fName=raw_input("Enter your CSV FileName: ")
    result = AddUser.runner(fName)
else:
    print("Wrong Input")
    exit()

User_output = raw_input(" Do you want to save your output to a text file: (Y for yes and N for No): ")
if(User_output=="Y" or User_output=="y"):
    outFileName= raw_input("Enter the output file name: ")
    f = open(outFileName,'w')
    print >>f, figlet_format('Lazy System Admin', font='starwars')
    print >>f, "\nMade By Omar Yassin\n"
    print >>f, result


