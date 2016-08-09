import os, sys, json
from wpterminal.bin.abstract_module import AbstractModule

class PluginModule(AbstractModule):

	def __init__ ( self, paths):
		self.paths = paths
		self.plugins_path = self.paths['plugins']
		self.plugin_path = self.plugins_path


	def create ( self, line = 0) :

		self.dirname = input('[+] Plugin Directory Name: ')

		self.plugin_declarations = {
			'Plugin Name': {
				'default': 'undefined',
				'value': input('[+] Plugin name: ')
			},
			'Plugin URI': {
				'default': '#',
				'value': input('[+] Plugin URI: ')
			},
			'Description':{
				'defaut': 'undefined',
				'value': input('[+] Plugin description: ')
			},
			'Author': {
				'default': 'wpterminal',
				'value': input('[+] Plugin Author: ')
			},
			'Author URI': {
				'default': '#',
				'value': input('[+] Plugin Author URI: ')
			},
			'Domain Path': {
				'default': '/languages/',
				'value': input('[+] Domain Path (/languages/): ')
			},
			'Text Domain':{
				'default': self.dirname.replace('-', '_').lower(),
				'value': input('[+] Text Domain (plugin_name): ')
			},
			'Version': {
				'default': '0.0.1',
				'value': input('[+] Version (0.0.1): ')
			}
		}

		self._maybeAutofillInputs()
		self._createPluginDirsAndResources()
		self.plugin_file = self._createFile( self.plugin_path,  '/' + self.dirname.lower() + '.php' )
		self._writePluginDeclaration()
		self._populateMainFile()

		#setAdvancedSettings = True if input('Do you want to set more advanced options? (y/n): ') == 'y' else False

		#if ( setAdvancedSettings ) :
			#print(' ')
			#self._askForOOP()
		#else:
			#print(' ')

		print('WordPress Plugin structure created successfully at => ' + self.plugin_path )


	def remove ( self, line= 0):
		return


	def clone ( self, line = 0) :
		return


	def run ( self ):
		return


	def _createPluginDirsAndResources ( self ) :

		self.plugin_path = self._createDir( self.plugins_path, '/' + self.dirname )

		self.plugin_inc_path = self._createDir(self.plugin_path, '/inc')
		self.plugin_classes_path = self._createDir(self.plugin_inc_path, '/classes')
		self.plugin_interfaces_path = self._createDir(self.plugin_inc_path, '/interfaces')
		self.plugin_res_path = self._createDir(self.plugin_path, '/res')
		self.plugin_templates_path = self._createDir(self.plugin_path, '/templates')
		self.plugin_langs_path = self._createDir(self.plugin_path, '/' +  self.plugin_declarations['Domain Path']['value'] )

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


	def _writePluginDeclaration ( self ):

		self.plugin_file.write('<?php\n')
		self.plugin_file.write('/*\n')
		self.plugin_file.write(' *\n')

		for key, value in self.plugin_declarations.items() :
			item = self.plugin_declarations[key];
			self.plugin_file.write(' * ' + key + ': ' + item['value'] + '\n')

		self.plugin_file.write(' *\n')
		self.plugin_file.write(' */\n\n')


	def _maybeAutofillInputs ( self ) :

		for key, value in self.plugin_declarations.items():
			item = self.plugin_declarations[key];

			if ( item['value'] == '' or item['value'] == False) :
				item['value'] = item['default']
				self.plugin_declarations[key] = item;


	def  _populateMainFile ( self ):

		capsPluginName = self.dirname.replace('-', '_').upper()

		self.plugin_file.write('if ( ! defined( \'ABSPATH\' ) ) exit; // Exit if accessed directly\n\n')

		self.plugin_file.write('define("' + capsPluginName +'_BASE_PATH", plugin_dir_path( __FILE__ ));\n')
		self.plugin_file.write('define("' + capsPluginName +'_INC_PATH", plugin_dir_path( __FILE__ ) . "/inc");\n')
		self.plugin_file.write('define("' + capsPluginName +'_JS_URL", plugin_dir_url( __FILE__ ) . "/res/js");\n')
		self.plugin_file.write('define("' + capsPluginName +'_STYLES_URL", plugin_dir_url( __FILE__ ) . "/res/css");\n')
		self.plugin_file.write('define("' + capsPluginName +'_TEMPLATES_PATH", plugin_dir_path( __FILE__ ) . "/templates");\n\n')

		init_fnc_declaration = 'function init_'  + self.dirname.replace('-', '_').lower() + '_plugin ()\n{\n\n}\n'
		init_hook_declaration = 'add_action("init", "init_' + self.dirname.replace('-', '_').lower() + '_plugin");\n\n'

		self.plugin_file.write(init_fnc_declaration);
		self.plugin_file.write(init_hook_declaration);

		activate_fnc_declaration = 'function activate_'  + self.dirname.replace('-', '_').lower() + '_plugin ()\n{\n\n}\n'
		activate_hook_declaration = 'register_activation_hook(__FILE__, "activate_' + self.dirname.replace('-', '_').lower() + '_plugin");\n\n'

		self.plugin_file.write(activate_fnc_declaration);
		self.plugin_file.write(activate_hook_declaration);

		end_string = '/*\n *\n * File generated by WPTERMINAL - feel free to colaborate at https://github.com/jmlp-131092/wpterminal\n *\n */\n\n'
		self.plugin_file.write(end_string)

		self.plugin_file.write('?>')


	def _askForOOP( self ):

		hasOOP = True if input('[+] Do you want to use a main class to load the plugin? (y/n)')  == 'y' else False
		className = ''
		setInstanceAsGlobal = False

		if ( hasOOP ) :
			className = input('[+] Class Name: ')
			setInstanceAsGlobal = True if  input('[+] Create class instance as global? (y/n)') == 'y' else False
		else :
			return
