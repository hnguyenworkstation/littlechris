import os
from sys import platform as _pl

if _pl is "linux" or _pl is "linux2":
	os.system("gnome-terminal -e 'bash -c \"python chris.py\"'")
elif _pl is "darwin":
	os.system("terminal -e 'bash -c \"python chris.py\"'")