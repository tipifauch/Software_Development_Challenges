# import pickle
#
# f = open("myfile2", "w")
# mylist = ['cdatetime', 'datetime', 'p0', "(S'\\x07\\xdf\\x0c\\x1f\\x01\\t\\x15\\x07\\x99('", 'p1', 'tp2', 'Rp3', '.']
# f.write("\n".join(map(lambda x: str(x), mylist)))
# f.close()
#
# pickled_date = open('myfile2', 'r')
# date = pickle.load(pickled_date)
# pickled_date.close()
#
# print date

import calendar

command = 'Listen, I was written on 9 Oct 15. Which day of the week (Monday, Tuesday,... Sunday) was it?'

date = command.replace('.',' ').split()
print date[5:8]

day = int(date[5])
month = date[6]
year = int(date [7])

dicto = dict((v,k) for k,v in enumerate(calendar.month_abbr))
print dicto

month = int(dicto.get(month))

weekday = calendar.weekday(year,month,day)
weekday =  calendar.day_name[weekday]

print weekday

secret = []
secret = secret_command.split('\n')
print secret[1]


> scp tipi@softdev.s3.eurecom.fr:challenge/python3/square.jpg .