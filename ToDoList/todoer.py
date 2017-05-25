import argparse

from tinydb import TinyDB, Query

import utils

DB = TinyDB('db.json',indent=2)



def insert_todo(eta, title="toDO:", parent=None, labels=[], status=None,notes=''):
  tid = utils.get_new_tid()

  D = {
    'tid': tid,
    'parent':parent,
    'labels':labels,
    'title': title,
    'eta': eta,
    'status':status,
    'notes':notes,
  }
  try:
    DB.insert(D)
    return tid
  except:
    return None

def modify(tid, key,value):
  R = Query()
  try:
    DB.update({key: value}, R['tid'] == tid)
    return True
  except:
    return False


def is_present(tid):
  R = Query()
  return DB.contains(R.tid == tid)

def purge():
  '''
    delete all and only top level tasks which has been marked done
  '''
  R = Query()
  DB.remove(R['status'] == "DONE" and R['parent'] == None)

## function 

def add_parent(child_tid,parent_tid):
  assert is_present(child_tid)
  assert is_present(parent_tid)

  return modify(child_tid, 'parent', parent_tid)


def delete(tid):
  '''
    soft delete.
  '''
  assert is_present(tid)
  return modify(tid, 'status',"DONE")


