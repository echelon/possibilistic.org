from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.conf import settings
import os
import time
import string
import markdown2 as markdown

def index(request):
	return HttpResponse(os.getcwd())

def view_page(request, page_name):
	# TODO: This is messy and insecure!

	locPart = '/markdown-docs'
	cachePart = '/markdown-cache'
	githubBase = 'http://github.com/echelon/markdown-docs/blob/master'

	basePath = ''
	githubUrl = ''

	if settings.DEBUG:
		basePath = '/home/brandon/Dev/possibilistic.org'
	else:
		basePath = '/home/possibilistic/possibilistic.org'

	path = basePath + locPart + '/' + str(page_name) + '.mkd'
	cachePath = basePath + cachePart + '/' + str(page_name) + '.mkd.cache'

	githubUrl = githubBase + '/' + str(page_name) + '.mkd'

	# If fail, try an index page...
	if not os.path.exists(path):
		path = basePath + locPart + '/' + str(page_name) + '/index.mkd'
		githubUrl = githubBase + '/' + str(page_name) + '/index.mkd'

	print path

	if not os.path.exists(path):
		raise Http404

	# TODO: @title directive. 
	title = None
	

	#page_name.split('/')

	title = string.replace(page_name, '/', ' > ')
	title = string.replace(title, '-', ' ')
	title = string.capwords(title)

	x = readfile(path)
	x = markdown.markdown(x)

	d = os.stat(path)
	t = time.localtime(int(d.st_mtime))
	editstr = time.strftime("%B %d, %Y", t)

	return render_to_response('markdown-base.html', {
									'title':	title,
									'content':	x,
									'editdate':	editstr,
									'githubUrl': githubUrl
								}, 
							  	mimetype='application/xhtml+xml')


def readfile(fname):
	f = open(fname)
	d = f.read()
	f.close()
	return d

#def writefile(fname, contents):
#	f = open(fname, 'w')
#	f.write(contents)
#	f.close()
