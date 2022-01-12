from FS.Log import Log

def test_create():
  return Log('Log#1', '[28.11.21]: system prototype')


def test_read(log):
  log_contents = log.read()

  assert log_contents == '[28.11.21]: system prototype'


def test_append(log):
  log.append(' and tests are created.')
  log1_contents = log.read()
  
  assert log1_contents == '[28.11.21]: system prototype and tests are created.'

lg1 = test_create()
test_read(lg1)
test_append(lg1)