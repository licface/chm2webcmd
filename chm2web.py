import os
import sys
import configset
import optparse
import subprocess
import traceback
import fileinput
import re

__version__ = "1.0"
__test__ = "0.2"
__author__ = "licface"
__url__ = "licface@yahoo.com"
__email__ = "licface@yahoo.com"
__sdk__ = "2.7"
__build__ = "win"

class chm2web:
	def __init__(self, parent=None):
		self.chm2web_path = r"c:\Program Files\A!K Research Labs\chm2web\chm2web.exe"
		self.name = os.path.basename(__file__)
		self.default_project_file = os.path.join(os.path.dirname(__file__), 'project.chm2web')
		self.mainProjectFile()
		self.masterpath = r'c:\Program Files\A!K Research Labs\chm2web'
		self.data_template = {1:"corporate.cwtpl", 2:"corporate-red.cwtpl", 3:"default.cwtpl", 4:"default-red.cwtpl", 5:"default-sunny.cwtpl", 6:"industrial-blue.cwtpl", 7:"industrial-green.cwtpl", 8:"industrial-vinous.cwtpl", 9:"simple.cwtpl", 10:"modern_bl.cwtpl", 11:"modern_or.cwtpl", 12:"modern_gr.cwtpl", 13:"modern_gy.cwtpl", 14:"modern_rd.cwtpl", 15:"quiet-bl.cwtpl", 16:"quiet-rd.cwtpl", 17:"windows-silver.cwtpl", 18:"windows-green.cwtpl"}

	def showTemplate(self):
		print "\n"
		usage_template = """            Template : 
			1. Corporate Blue       10. Modern Blue
			2. Corporate Red        11. Modern Orange
			3. Default Blue         12. Modern Green
			4. Default Red          13. Modern Grey
			5. Default Sunny        14. Modern Red
			6. Industrial Blue      15. Quiet Blue
			7. Industrial Green     16. Quiet Red
			8. Industrial Vinous    17. Windows Classic
			9. Simple White         18. Windows Green  
		"""
		return usage_template

	def mainProjectFile(self):
		if not os.path.isfile(self.set_project_file()):
			ft = open(os.path.join(os.path.dirname(__file__), "default.chm2web"), 'r').read()
			f = open(os.path.join(os.path.dirname(__file__), self.set_project_file()), 'w')
			f.write(ft)
			ft.close()
			f.close()

	def set_main_source(self, mainfile):
		return configset.write_config('MAIN','SourceFile', self.default_project_file, mainfile)

	def get_main_source(self, mailfile):
		return configset.get_config2('MAIN','SourceFile', self.default_project_file, mainfile)

	def set_project_file(self, filename=None):
		if not filename == None:
			return os.path.abspath(filename)	
		else:
			#print "self.default_project_file =", self.default_project_file
			return self.default_project_file
		#print "filename X =", filename

	def get_template(self, template):
		if isinstance(template, int):
			main_template = os.path.join(self.masterpath, "Templates\\" + self.data_template[template])
		else:
			main_template = os.path.join(self.masterpath, "Templates\modern_bl.cwtpl")
		return configset.get_config2('OPTIONS', 'Template', self.default_project_file, main_template)

	def set_template(self, template):
		if isinstance(template, int):
			main_template = os.path.join(self.masterpath, "Templates\\" + self.data_template[template])
		else:
			main_template = os.path.join(self.masterpath, "Templates\modern_bl.cwtpl")
		return configset.write_config('OPTIONS', 'Template', self.default_project_file, main_template)

	def get_homeurl(self, homeurl):
		return configset.get_config2('VARS', 'varHomeUrl', self.default_project_file, homeurl)

	def set_homeurl(self, homeurl):
		return configset.write_config('VAR', 'varHomeUrl', self.default_project_file, homeurl)

	def get_pagecaption(self, caption):
		return configset.get_config2('VAR', 'varPageCaption', self.default_project_file, caption)

	def set_pagecaption(self, caption):
		return configset.write_config('VAR', 'varPageCaption', self.default_project_file, caption)

	def get_serversidepath(self, serverside):
		return configset.get_config2('OPTIONS', 'ServerSidePath', self.default_project_file, serverside)

	def set_serversidepath(self, serverside):
		return configset.write_config('OPTIONS', 'ServerSidePath', self.default_project_file, serverside)

	def get_targetfolder(self, folder):
		configset.get_config2('MAIN', 'TargetFolder', self.default_project_file, folder)

	def set_targetfolder(self, folder):
		if not os.path.isdir(folder):
			os.mkdir(folder)
		configset.write_config('MAIN', 'TargetFolder', self.default_project_file, folder)

	def get_indexfilename(self, indexfile):
		return configset.get_config2('MAIN', 'IndexFileName', self.default_project_file, indexfile)

	def set_indexfilename(self, indexfile):
		return configset.write_config('MAIN', 'IndexFileName', self.default_project_file, indexfile)

	def getIndex(self, varindex):
		return configset.get_config2('VAR', 'varIndex', self.default_project_file, varindex)

	def setIndex(self, varindex):
		return configset.write_config('VAR', 'varIndex', self.default_project_file, varindex)

	def get_searchquery_len(self, querylen):
		return configset.get_config2('OPTIONS', 'MinQueryLen', self.default_project_file, querylen)

	def set_searchquery_len(self, querylen):
		return configset.write_config('OPTIONS', 'MinQueryLen', self.default_project_file, querylen)

	def replace(self, file, pattern, subst):
	    file_handle = open(file, 'r')
	    file_string = file_handle.read()
	    file_handle.close()

	    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
	    file_string = (re.sub(pattern, subst, file_string))

	    # Write contents to file.
	    # Using mode 'w' truncates the file.
	    file_handle = open(file, 'w')
	    file_handle.write(file_string)
	    file_handle.close()

	def reconfig(self):
		self.replace(self.set_project_file(), " = ", "=")

	def run(self, projectfile=None, chm=None, template=None, url=None, caption=None, sidepath=None, folder=None, indexfile=None, indexvar=None, querylen=None, no_browser=None, quiet=None, open_only=None, verbosity=None, daemon=None):
		if verbosity == 2:
			print "projectfile    =", projectfile
			print "chm            =", chm
			print "template       =", template
			print "url            =", url
			print "caption        =", caption
			print "sidepath       =", sidepath
			print "folder         =", folder
			print "indexfile      =", indexfile
			print "indexvar       =", indexvar
			print "querylen       =" , querylen
			print "no_browser     =", no_browser
			print "quiet          =", quiet
			print "open_only      =", open_only
			print "verbosity      =", verbosity
			print "-"*110
			print self.showTemplate()
		try:
			if verbosity > 0:
				if projectfile != None:
					print "set Project File          :", projectfile
					self.set_project_file(projectfile)
				else:
					print "set Project File          :", self.set_project_file()
					projectfile = self.set_project_file()

				if template != None:
					print "set Template Name         :", template
					self.set_template(template)
				else:
					print "set Template Name         : Modern Blue (10)" 
					self.set_template(10)

				print "set Home Url              :", url
				self.set_homeurl(url)
			
				print "set Caption               :", caption
				self.set_pagecaption(caption)
			
				if sidepath != None:
					print "set Server Side Path      :", sidepath
					self.set_serversidepath(sidepath)
				else:
					print "set Server Side Path      :", url
					self.set_serversidepath(url)
			
				print "set Target Folder         :", folder
				self.set_targetfolder(folder)
			
				if indexfile != None:
					print "set Index File Name       :", indexfile
					self.set_indexfilename(indexfile)
				else:
					print "set Index File Name       : index.html"
					self.set_indexfilename('index.html')
			
				if indexvar != None:
					print "set Index Variable        :", indexvar
					self.setIndex(indexvar)
				else:
					print "set Index Variable        : Index"
					self.setIndex("Index")
			
				if querylen != None:
					print "set Query Len             :", querylen
					self.set_searchquery_len(querylen)
				else:
					print "set Query Len             : 1"
					self.set_searchquery_len(1)
			
				print "set Main Chm File         :", chm
				self.set_main_source(chm)
				#print "\n"
				#print "final project file         =", str(projectfile)
			else:
				if projectfile != None:
					self.set_project_file(projectfile)
				else:
					projectfile = self.set_project_file()

				if template != None:
					self.set_template(template)
				else:
					self.set_template(10)

				self.set_homeurl(url)
			
				self.set_pagecaption(caption)
			
				if sidepath != None:
					self.set_serversidepath(sidepath)
				else:
					self.set_serversidepath(url)
			
				self.set_targetfolder(folder)
			
				if indexfile != None:
					self.set_indexfilename(indexfile)
				else:
					self.set_indexfilename('index.html')
			
				if indexvar != None:
					self.setIndex(indexvar)
				else:
					self.setIndex("Index")
			
				if querylen != None:
					self.set_searchquery_len(querylen)
				else:
					self.set_searchquery_len(1)
			
				self.set_main_source(chm)
				#print "\n"
				#print "final project file         =", str(projectfile)
			self.reconfig()
			if quiet:
				if no-browser:
					if daemon:
						pid = subprocess.Popen([self.chm2web_path, str(projectfile) + " /d /q"]).pid
						return pid
					else:
						os.chdir(os.path.dirname(self.chm2web_path))
						os.system("chm2web.exe" + " " + str(projectfile) + " /d /q")
				else:
					if daemon:
						pid = subprocess.Popen([self.chm2web_path, str(projectfile) + " /q"]).pid
						return pid
					else:
						os.chdir(os.path.dirname(self.chm2web_path))
						os.system("chm2web.exe" + " " + str(projectfile) + " /q")
			else:
				if no_browser:
					if daemon:
						pid = subprocess.Popen([self.chm2web_path, str(projectfile) + " /d"]).pid
						return pid
					else:
						os.chdir(os.path.dirname(self.chm2web_path))
						os.system("chm2web.exe" + " " + str(projectfile) + " /d")
				else:
					if daemon:
						pid = subprocess.Popen([self.chm2web_path, str(projectfile)]).pid
						return pid
					else:
						os.chdir(os.path.dirname(self.chm2web_path))
						os.system("chm2web.exe" + " " + str(projectfile))
			if open_only:
				if daemon:
					pid = subprocess.Popen([self.chm2web_path, str(projectfile) + " /n"]).pid
					return pid
				else:
					os.chdir(os.path.dirname(self.chm2web_path))
					os.system("chm2web.exe" + " " + str(projectfile) + " /n")
		except:
			if verbosity > 1:
				icon = os.path.join(os.path.dirname(__file__), 'chm2web.png')
				traceback.format_exc_syslog_growl(True, growl_appname="Python Traceback - chm2web", growl_title="Python Traceback (chm2web)", severity=3, growl_icon=icon)
	def set(self, projectfile=None, chm=None, template=None, url=None, caption=None, sidepath=None, folder=None, indexfile=None, indexvar=None, querylen=None, no_browser=None, quiet=None, open_only=None, verbosity=None):
		print "projectfile    =", projectfile
		print "chm            =", chm
		print "template       =", template
		print "url            =", url
		print "caption        =", caption
		print "sidepath       =", sidepath
		print "folder         =", folder
		print "indexfile      =", indexfile
		print "indexvar       =", indexvar
		print "querylen       =" , querylen
		print "no_browser     =", no_browser
		print "quiet          =", quiet
		print "open_only      =", open_only
		print "verbosity      =", verbosity
		print "-"*110
		try:
			if verbosity > 0:
				if projectfile != None:
					print "set Project File          :", projectfile
					self.set_project_file(projectfile)
				else:
					print "set Project File          :", self.set_project_file()
					projectfile = self.set_project_file()
			if verbosity > 0:
				if template != None:
					print "set Template Name         :", template
					self.set_template(template)
				else:
					print "set Template Name         : Modern Blue (10)" 
					self.set_template(10)
			if verbosity > 0:
				print "set Home Url              :", url
			self.set_homeurl(url)
			if verbosity > 0:
				print "set Caption               :", caption
			self.set_pagecaption(caption)
			if verbosity > 0:
				if sidepath != None:
					print "set Server Side Path      :", sidepath
					self.set_serversidepath(sidepath)
				else:
					print "set Server Side Path      :", url
					self.set_serversidepath(url)
			if verbosity > 0:
				print "set Target Folder         :", folder
			self.set_targetfolder(folder)
			if verbosity > 0:
				if indexfile != None:
					print "set Index File Name       :", indexfile
					self.set_indexfilename(indexfile)
				else:
					print "set Index File Name       : index.html"
					self.set_indexfilename('index.html')
			
			if verbosity > 0:
				if indexvar != None:
					print "set Index Variable        :", indexvar
					self.setIndex(indexvar)
				else:
					print "set Index Variable        : Index"
					self.setIndex("Index")
			if verbosity > 0:
				if querylen != None:
					print "set Query Len             :", querylen
					self.set_searchquery_len(querylen)
				else:
					print "set Query Len             : 1"
					self.set_searchquery_len(1)
			if verbosity > 0:
				print "set Main Chm File         :", chm
			self.set_main_source(chm)
			print "\n"
			print "final project file         =", str(projectfile)
			self.reconfig()
		except:
			if verbosity > 1:
				icon = os.path.join(os.path.dirname(__file__), 'chm2web.png')
				traceback.format_exc_syslog_growl(True, growl_appname="Python Traceback - chm2web", growl_title="Python Traceback (chm2web)", severity=3, growl_icon=icon)

	def command(self, print_help=None):
		parser = optparse.OptionParser()
		parser.add_option("-p", "--project", help="Project File (*.chm2web), default='project.chm2web'", action="store_true")
		parser.add_option("-f", "--file", help="File *.chm to converting", action="store")
		parser.add_option("-n", "--no-run", help="not run the conversion. Instead it will open the specified project file. This flag has effect only if [project file] parameter is given.", action="store_true")
		parser.add_option("-b", "--no-browser", help="will not open the browser window after conversion. Otherwise the default setting will be used.", action="store_true")
		parser.add_option("-q", "--quiet", help="quiet mode. chm2web will not display GUI. Requires [project file] option.", action="store_true")
		parser.add_option("-s", "--set", help="Set/config file config only", action="store_true")
		parser.add_option("-t", "--template", help="Number of Template Project Name, default='Modern Blue (10)'", action="store", type=int)
		parser.add_option("-l", "--home-url", help="Home Url or Homepage Url", action="store")
		parser.add_option("-c", "--caption", help="Page Caption Name and Title Site Name", action="store")
		parser.add_option("-r", "--side-path", help="Server Side Path Name, default is Home Url", action="store")
		parser.add_option("-d", "--target-folder", help="Target Folder where to extract File CHM, default make folder if not exist", action="store")
		parser.add_option("-i", "--index", help="Index File Name Of File Of Extracted, default='index.html'", action="store")
		parser.add_option("-x", "--var-index", help="Variable Index Name (default: 'Index')", action="store")
		parser.add_option("-e", "--query-len", help="Index Search Query Len, default= 1", action="store", type=int)
		parser.add_option("-T", "--show-Template", help="Show Template List", action="store_true")
		parser.add_option("-g", "--run-background", help="Run in Background", action="store_true")
		parser.add_option("-v", "--verbosity", help="Show running process", action="count")
		options, args = parser.parse_args(sys.argv)
		if len(sys.argv) > 1:
			#print "options =", options, "\n"
			if options.set:
				self.set(options.project, options.file, options.template, options.home_url, options.caption, options.side_path, options.target_folder, options.index, options.var_index, options.query_len, options.no_browser, options.quiet, options.no_run, options.verbosity, options.run_background)
			else:
				if options.file:
					#run(self, projectfile=None, chm=None, template=None, url=None, caption=None, sidepath=None, folder=None, indexfile=None, indexvar=None, querylen=None, no_browser=None, quiet=None, open_only=None, verbosity=None):
					self.run(options.project, options.file, options.template, options.home_url, options.caption, options.side_path, options.target_folder, options.index, options.var_index, options.query_len, options.no_browser, options.quiet, options.no_run, options.verbosity, options.run_background)
				else:
					print "\n"
					parser.print_help()
					print "\n"
		elif print_help:
			print "\n"
			parser.print_help()
			print "\n"
			#print self.showTemplate()
		else:
			print "\n"
			parser.print_help()
			print "\n"
			#print self.showTemplate()

if __name__ == "__main__":
	c = chm2web()
	c.command()
	#c.set_homeurl('http://licface.net')
	#print c.get_homeurl('http://licface.net')
	#f = open('project.chm2web').read()
	#print f

