from tinydb import TinyDB, Query
import time
import utils

class Engine(object):
  def __init__(self,database_name='db.json'):
    self._DB = TinyDB(database_name,indent=2)

  def insert(self, eta=None, title="toDO:", parent=None, labels=[], status=None,notes=''):
    tid = utils.get_new_tid()
    while self.is_present(tid):
      '''
        the index which marks  the start of 6-alphabet  sha hash in get_new_tid
        is randomised earier this  loop was looping many times and hence had to
        insert an time.sleep(1). But after randommisation, even if it is called
        multiple times a second, the 6 alphabet sha hash returned is random.
      '''
      tid = utils.get_new_tid()  

    D = {
      'tid'   : tid,
      'parent': parent,
      'labels': labels,
      'title' : title,
      'eta'   : eta,
      'status': status,
      'notes' : notes,
    }
    try:
      self._DB.insert(D)
      return tid
    except:
      return None
  
  def modify(self,tid, key,value):
    R = Query()
    try:
      self._DB.update({key: value}, R['tid'] == tid)
      return True
    except:
      return False
  
  def is_present(self,tid):
    R = Query()
    return self._DB.contains(R.tid == tid)
  
  def purge(self):
    '''
      delete all and only top level tasks which has been marked done
    '''
    R = Query()
    self._DB.remove(R['status'] == "DONE" and R['parent'] == None)
  def get_all(self,tid=None):
    R = Query()
    Records=self._DB.search(R['status'] != "DONE" and R['parent'] == tid)
    Records.sort(key=lambda R: utils.string_to_time(R['eta'])) 
    return Records
