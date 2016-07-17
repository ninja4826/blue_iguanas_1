@echo off
setlocal EnableDelayedExpansion
setlocal EnableExtensions

del db.sqlite3
set python=/usr/bin/python
!python! ./manage.py migrate
if exist ./todo/fixtures/seed.json (
  !python! ./manage.py loaddata seed
)