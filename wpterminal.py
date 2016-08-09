import os, sys, json, requests, cmd
from wpterminal.bin.modules.plugin_module import PluginModule
from wpterminal.bin.modules.theme_module import ThemeModule
from wpterminal.bin.help_module import HelpModule

class WPCMD(HelpModule):

	def __init__ ( self ):
		self.paths = {
			'plugins': 'wp-content/plugins/',
			'themes': 'wp-content/themes/'
		}
		self.help_lines = {
			'--create {arg}': 'it creates an entity of type {arg} , it can be \'--plugn\' or \'--theme\'',
			'--remove {arg}': 'it removes an entity of type {arg} , it can be \'--plugn\' or \'--theme\'',
			'--clone {arg}': 'it clones an entity of type {arg} , it can be \'--plugn\' or \'--theme\'',
		}
		self.modules = [
			'--plugin',
			'--theme',
			'--help'
		]
		self.modules_keys = {
			'--plugin': PluginModule( self.paths ),
			'--theme': ThemeModule( self.paths ),
			'--help': 'help'
		}
		self.verbs = [
			'--create',
			'--remove',
			'--clone',
			'--help'
		]
		self.args = sys.argv
		self.module = self.getModuleInstance()
		self.verb = self.getModuleVerb()
		self.run()

	def getModuleVerb ( self , line = 0):
		if ( len(sys.argv) >= 2 and sys.argv[1] in self.verbs ):
			return sys.argv[1]
		return False


	def getModuleInstance ( self, line = 0) :
		if ( len(sys.argv) >= 3 and sys.argv[2] in self.modules ):
			return sys.argv[2]
		return False


	def run( self, line = 0 ):
		if ( self.module and self.verb ) :
			module = self.modules_keys[self.module]
			method = self.verb.replace('-', '')
			result = getattr(module, method)()
		elif ( self.verb == '--help'):
			print('---------------------------')
			print('COMMANDS HELP')
			print('---------------------------')
			for cmd, value in self.help_lines.items():
				print(cmd + ' => ' + value)
				print('---------------------------')



if ( __name__ == '__main__' ):
	wpcmd = WPCMD()
