from tinydb import TinyDB, Query
from random import randint

import utils
import todoer

WORDS = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum".split()

def rnd_wrd():
  return WORDS[randint(0,len(WORDS)-1)]

def rnd_time():
  return utils.time_to_string(
          year = randint(2015,2018), 
          month = randint(0,11), 
          day=randint(0,28), 
          hour=randint(0,23), 
          minute=randint(0,59), 
          sec=randint(0,59)
  )

todoer.init('test.json')

todoer.DB._DB.purge_tables()

tids = []
for i in range(100):
  if i%3==0:
    tid = todoer.insert_todo(rnd_wrd())
  else:
    tid = todoer.insert_todo(rnd_wrd(),rnd_time())
  tids.append(tid)

for i in range(100):
  ind1 = randint(0,len(tids)-1)
  ind2 = randint(0,len(tids)-1)
  if ind1!=ind2:
    todoer.add_parent(tids[ind1],tids[ind2])

  
todoer.print_tree()
