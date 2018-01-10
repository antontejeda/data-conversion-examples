import datetime

birth_date = "1-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.datetime.strptime(birth_date, date_format)

print parsed_date.strftime("%-m/%-d/%Y") # 01/11/17

# goal is 5/1/2012