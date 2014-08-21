chm2webcmd
==========

Command line wrapper chm2web windows from "A!K Research Labs"


usage
=============

		Usage: chm2web.py [options]

		Options:
		  -h, --help            show this help message and exit
		  -p, --project         Project File (*.chm2web), default='project.chm2web'
		  -f FILE, --file=FILE  File *.chm to converting
		  -n, --no-run          not run the conversion. Instead it will open the
								specified project file. This flag has effect only if
								[project file] parameter is given.
		  -b, --no-browser      will not open the browser window after conversion.
								Otherwise the default setting will be used.
		  -q, --quiet           quiet mode. chm2web will not display GUI. Requires
								[project file] option.
		  -s, --set             Set/config file config only
		  -t TEMPLATE, --template=TEMPLATE
								Number of Template Project Name, default='Modern Blue
								(10)'
		  -l HOME_URL, --home-url=HOME_URL
								Home Url or Homepage Url
		  -c CAPTION, --caption=CAPTION
								Page Caption Name and Title Site Name
		  -r SIDE_PATH, --side-path=SIDE_PATH
								Server Side Path Name, default is Home Url
		  -d TARGET_FOLDER, --target-folder=TARGET_FOLDER
								Target Folder where to extract File CHM, default make
								folder if not exist
		  -i INDEX, --index=INDEX
								Index File Name Of File Of Extracted,
								default='index.html'
		  -x VAR_INDEX, --var-index=VAR_INDEX
								Variable Index Name (default: 'Index')
		  -e QUERY_LEN, --query-len=QUERY_LEN
								Index Search Query Len, default= 1
		  -T, --show-template   Show Template List
		  -g, --run-background  Run in Background
		  -v, --verbosity       Show running process    


		Template :
					1. Corporate Blue       10. Modern Blue
					2. Corporate Red        11. Modern Orange
					3. Default Blue         12. Modern Green
					4. Default Red          13. Modern Grey
					5. Default Sunny        14. Modern Red
					6. Industrial Blue      15. Quiet Blue
					7. Industrial Green     16. Quiet Red
					8. Industrial Vinous    17. Windows Classic
					9. Simple White         18. Windows Green

author
==============
LICFACE <licface@yahoo.com>    