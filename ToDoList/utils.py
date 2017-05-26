import time 
import datetime
import hashlib
from random import randint

TIME_FORMAT="%Y-%b-%d %H:%M:%S"

def time_to_string(year, month, day, hour, minute, sec):
  t = (year, month, day, hour, minute, sec ,0 ,0 ,0)
  return time.strftime(TIME_FORMAT ,t)

def string_to_time(time_string):
  if time_string is None:
    time_string = time_to_string(2100,1,1,1,1,1)
  return time.strptime(time_string,TIME_FORMAT)

def get_new_tid():
   time_string = time.strftime(TIME_FORMAT,time.gmtime())
   time_string = time_string.encode('utf-8')
   hash_ = hashlib.sha224(time_string).hexdigest()
   index = randint(0,len(hash_)-6)
   return hash_[index:index+6]
