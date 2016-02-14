#!/usr/bin/env python

from command import Executor

HIVE_SQL_COUNT="USE {0};SELECT COUNT(*) FROM {0}.{1};"

class SqlExec(Executor):

	def __init__(self,dbName,tblName):

		self.dbName=dbName
		self.tblName=tblName

	def sql_result(self):

		print(Executor(HIVE_SQL_COUNT.format(self.dbName,self.tblName)).execute_os_command())



    
