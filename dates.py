import datetime
import pytz
today = datetime.date.today()
print (today)
tdelta = datetime.timedelta(days=7)
bday = datetime.date(2022,5,18)
till_bday = bday - today
print (till_bday.days)


# dt = datetime.datetime(2021,7,9,14,0,45,tzinfo=pytz.utc)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
print(dt_mtn.strftime('%B %d, %Y'))
# for tz in pytz.all_timezones:
#     print(tz)