import argparse

from core import Engine

DB = None
def init(db_name='test.json'):
  global DB
  DB = Engine(db_name)


def insert_todo(title, eta=None):
  return DB.create(title=title, eta=eta)

def add_parent(child_tid,parent_tid):
  assert DB.is_present(child_tid)
  assert DB.is_present(parent_tid)

  return DB.alter(child_tid, 'parent', parent_tid)

def delete(tid):
  '''
    soft delete.
  '''
  assert DB.is_present(tid)
  return DB.alter(tid, 'status',"DONE")

def stringify_record(record, full=False):
  if not full:
    return "{} {} {}".format(record['tid'], record['eta'], record['title'].title())
  record_string = '''
  Title : {}
  ETA   : {}
  Labels: {}
  Status: {}
  T-Id  : {}
  Notes : {}
  '''.format(
          record['title'],
          record['eta'],
          record['labels'],
          record['status'],
          record['tid'],
          record['notes'],
  )
  return record_string

def print_tree(tid=None,indent=0):
  if indent>5:
    print("|||")
    return
  Records = DB.list(tid)
  for record in Records :
    print("  "*indent,end='')
    print(stringify_record(record))
    print_tree(record['tid'],indent+1)
