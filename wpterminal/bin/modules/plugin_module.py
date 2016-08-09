import os
import sys
from wpterminal.bin.abstract_module import AbstractModule

class PluginModule(AbstractModule):

	def __init__ ( self, paths):
		self.paths = paths
		self.plugins_path = self.paths['plugins']
		self.plugin_path = self.plugins_path

	def create ( self, line = 0) :
		self.dirname = input('Plugin Directory Name: ')
		self.plugin_declarations = {
			'Plugin Name': input('Plugin name: '),
			'Plugin URI': input('Plugin URI: '),
			'Description': input('Plugin description: '),
			'Author': input('Plugin Author: '),
			'Author URI': input('Plugin Author URI: '),
			'Domain Path': ( input('Domain Path (/languages/): ') if input('Domain Path (/languages/): ') != '' else '/languages/' ),
			'Text Domain': ( input('Text Domain (plugin_name): ') if  input('Text Domain (plugin_name): ') != '' else self.dirname.replace('-', '_').lower() ),
			'Version': ( input('Version (0.0.1): ') if input('Version (0.0.1): ') != '' else '0.0.1' )
		}
		self.plugin_path = self._createDir( self.plugins_path, '/' + self.dirname )

		self.plugin_inc_path = self._createDir(self.plugin_path, '/inc')
		self.plugin_res_path = self._createDir(self.plugin_path, '/res')
		self.plugin_templates_path = self._createDir(self.plugin_path, '/templates')
		self.plugin_langs_path = self._createDir(self.plugin_path, '/' + ( self.plugin_declarations['Domain Path'] if self.plugin_declarations['Domain Path'] != '' else 'languages') )

		self.plugin_js_path = self._createDir(self.plugin_res_path, '/js')
		self.plugin_css_path = self._createDir(self.plugin_res_path, '/css')

		self.plugin_css_admin_path = self._createDir(self.plugin_css_path, '/admin')
		self.admin_css = self._createFile( self.plugin_css_admin_path, '/admin.css')
		self.plugin_css_frontend_path = self._createDir(self.plugin_css_path, '/frontend')
		self.frontend_css = self._createFile( self.plugin_css_frontend_path, '/frontend.css')

		self.plugin_js_admin_path = self._createDir(self.plugin_js_path, '/admin')
		self.admin_js = self._createFile(self.plugin_js_admin_path, '/admin.js')
		self.plugin_js_frontend_path = self._createDir(self.plugin_js_path, '/frontend')
		self.frontend_js = self._createFile(self.plugin_js_frontend_path, '/frontend.js')

		self.plugin_file = self._createFile( self.plugin_path,  '/' + self.dirname + '.php' )
		self._writePluginDeclaration( self.plugin_declarations, self.plugin_file )

	def remove ( self, line= 0):
		return

	def clone ( self, line = 0) :
		return

	def run ( self ):
		return

	def _writePluginDeclaration ( self, plugin_declarations, _file ):
		_file.write('<?php\n')
		_file.write('/*\n')
		_file.write(' *\n')
		for key, value in plugin_declarations.items() :
			_file.write(' * ' + key + ': ' + value + '\n')
		_file.write(' *\n')
		_file.write(' */\n\n')
		_file.write('define("THE_PLUGIN_BASE_PATH", plugin_dir_path( __FILE__ ));\n')
		_file.write('define("THE_PLUGIN_INC_PATH", plugin_dir_path( __FILE__ ) . "/inc");\n')
		_file.write('define("THE_PLUGIN_JS_URL", plugin_dir_url( __FILE__ ) . "/res/js");\n')
		_file.write('define("THE_PLUGIN_STYLES_URL", plugin_dir_url( __FILE__ ) . "/res/css");\n')
		_file.write('define("THE_PLUGIN_TEMPLATES_PATH", plugin_dir_path( __FILE__ ) . "/templates");\n\n')

		init_fnc_declaration = 'function init_'  + self.dirname.replace('-', '_').lower() + '_plugin ()\n{\n\n}\n'
		init_hook_declaration = 'add_action("init", "init_' + self.dirname.replace('-', '_').lower() + '_plugin");\n\n'

		_file.write(init_fnc_declaration);
		_file.write(init_hook_declaration);

		activate_fnc_declaration = 'function activate_'  + self.dirname.replace('-', '_').lower() + '_plugin ()\n{\n\n}\n'
		activate_hook_declaration = 'register_activation_hook(__FILE__, "active_' + self.dirname.replace('-', '_').lower() + '_plugin");\n'

		_file.write(activate_fnc_declaration);
		_file.write(activate_hook_declaration);



		_file.write('?>')
