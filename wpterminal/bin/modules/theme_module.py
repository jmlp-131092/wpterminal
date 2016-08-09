import os, sys, json
from wpterminal.bin.abstract_module import AbstractModule

class ThemeModule(AbstractModule):

		def __init__ ( self, paths):
			self.paths = paths
			self.themes_path = self.paths['themes']
			self.theme_path = self.themes_path
			return

		def create ( self, line = 0) :
			print ('creating plugin')

		def remove ( self, line= 0):
			return

		def clone ( self, line = 0) :
			return

		def run ( self ):
			return
