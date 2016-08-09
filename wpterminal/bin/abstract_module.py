import sys, os, json, requests

class AbstractModule():

	def __init__ ( self, paths ):
		self.paths = paths;
		return

	def _createFile ( self, path, name ):
		_file = open( path +  name, 'w+')
		return _file

	def _createDir (self, path, name ):
		os.makedirs( path + name )
		return path + name

	def _writeToFile( self,  _file, lines = [] ):
		for x in range( len( lines ) ):
			_file.write( lines[x] )

	def _copyDir ( self, path ):
		return path

	def run (self):
		return
