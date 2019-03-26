import re
def runner():
    count = 0
    regex=r"\[(\d{2}\/\w{3}\/\d{4}):(\d{2}:\d{2}:\d{2}) \+\d{4}\]"
    for line in file("/var/log/httpd/access_log"):
        count =count +1
    lastLine = re.search(regex, line)
    lastLine = lastLine.group(0)

    f = open("/var/log/httpd/access_log", "r")
    text=f.read()
    firstLine = re.search(regex, text)
    firstLine = firstLine.group(0)
    result= "from the period %s to %s the number of access times %d \n" % (firstLine,lastLine,count)
    return result
