import time 
import datetime
import hashlib


TIME_FORMAT="%Y-%b-%d %H:%M:%S"

def time_to_string(year,month,day,hour,minute,sec):
  t = (year, month, day, hour, minute, sec ,0 ,0 ,0)
  return time.strftime(TIME_FORMAT ,t)


def get_new_tid():
   time_string = time.strftime(TIME_FORMAT,time.gmtime())
   hash_ = hashlib.sha224(time_string).hexdigest()
   return hash_[0:7]
