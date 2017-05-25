from tinydb import TinyDB, Query

import utils
import todoer


D = [{
  'parent':1000,
  'labels':[ 'label1', 'label2'],
  'title':'To do take one test',
  'eta':utils.time_to_string(2016,12,2,17,6,2),
  'status':'ongoing'
},{
  'parent':None,
  'labels':[ 'label1', 'label2'],
  'title':'To do take one test',
  'eta':None,
  'status':'ongoing'
},
]

'''
print todoer.insert_todo(**D[0])

print todoer.modify(1,'parent',24)
'''
todoer.purge()
