import os, sys, json
from wpterminal.bin.abstract_module import AbstractModule

class ThemeModule(AbstractModule):

		def __init__ ( self, paths):
			self.paths = paths
			self.themes_path = self.paths['themes']
			self.theme_path = self.themes_path
			self.theme_dir_name = '';
			return

		def create ( self, line = 0) :
			print ('creating plugin')

		def remove ( self, line= 0):
			return

		def clone ( self, line = 0) :
			return

		def run ( self ):
			return

		def _createStyle ( self ) :
			_file = self._createFile( self.theme_path, '/style.css', 'w+' )
			return _file

		def _createThemeDirsAndResources ( self ):

			self.theme_res_path = self._createDir( self.theme_path, '/res' )
			self.theme_css_path = self._createDir( self.theme_res_path, '/css' )
			self.theme_images_path = self._createDir( self.theme_res_path, '/images' )
			self.theme_js_path = self._createDir( self.theme_res_path, '/js' )
			self.theme_inc_path = self._createDir( self.theme_path, '/inc' )

			self.functions_file = self._createFile(self.theme_path, '/functions.php')
			self.index_file = self._createFile(self.theme_path, '/index.php')
			self.sidebar_file = self._createFile(self.theme_path, '/sidebar.php')
			self.page_file = self._createFile(self.theme_path, '/page.php')
			self.header_file = self._createFile(self.theme_path, '/header.php')
			self.footer_file = self._createFile(self.theme_path, '/footer.php')
			self.single_file = self._createFile(self.theme_path, '/single.php')

		def _createThemeHeader ( self ):
			return

		def _createThemeFooter ( self ):
			return

		def _createThemePage ( self ):
			return

		def _createThemeSingle ( self ):
			return
