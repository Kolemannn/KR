# -*- coding: utf-8 -*-

class multirequest(object):
 	def __init__(self, function = None):
 		if function :
 			self.__Functions = { 'GET' : function}
 		else :
 			self.__Functions = dict()

 	def method(self, title):
 		def attach (function) :
 			self.__Functions [title] = function
 			return self
 		return attach
 		
########################################################## 		

 	def GET(self, function) :
 		self.__Functions['GET'] = function
 		return self 

 	def POST(self, function) :
 		self.__Functions['POST'] = function
 		return self 

 	def DELETE(self, function) :
 		self.__Functions['DELETE'] = function
 		return self 

 ########################################################	
 	def __call__ (self, request, *args, **kwargs):
 		try:
	 		func = self.__Functions [request.method]
	 		return func (request, *args, **kwargs)
 		except KeyError as Exc :
 			raise
 	
