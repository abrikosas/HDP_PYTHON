#!/usr/bin/env python 

"""Execute OS command passed by parameter

Method exec_command receives argument from __init__()

"""

import subprocess

class Executor:
	"""Class takes one parameter and execute it 
	"""
	def __init__(self, command):

		self.command = command


	def execute_os_command(self):

		try:
			process=subprocess.Popen(self.command,stdin=subprocess.PIPE,
									stdout=subprocess.PIPE,shell=True)
			output,error = process.communicate()
			return output
		except IOError as e:
			return 1
