import re
def runner():
    count = 0
    regex=r"\[\w{3} (\w{3} \d{2}) (\d{2}:\d{2}:\d{2})\.\d{6} (\d{4})\]"
    for line in file("/var/log/httpd/error_log"):
        count =count +1
    lastLine = re.search(regex, line)
    lastLine = lastLine.group(0)

    f = open("/var/log/httpd/error_log", "r")
    text=f.read()
    firstLine = re.search(regex, text)
    firstLine = firstLine.group(0)
    result= "from the period %s to %s the number of errors %d \n" % (firstLine,lastLine,count)
    return result