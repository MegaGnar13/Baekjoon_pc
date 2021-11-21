from datetime import datetime

start="05/04 MON"
what="06/12"
print(start[-3:])
start=start[:-4]
start=start.split("/")
what=what.split("/")
start=''.join(start)
what=''.join(what)
# print(start,what)

now=datetime.strptime(what,"%m%d")

date_to_compare=datetime.strptime(start,"%m%d")

date_diff=now-date_to_compare
print(date_diff.days)

