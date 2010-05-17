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
	# TODO: Need to filter page_name (Even though urls.py only allows \W-.)

	def linkToTitle(link):
		"""Heuristic for turning a link into a title, 
		eg. /some-document/subdocument into a "Some Document > Subdocument"""
		title = string.replace(link, '/', ' > ')
		title = string.replace(title, '-', ' ')
		return string.capwords(title)

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

	if not os.path.exists(path):
		raise Http404

	# Generate back navigation
	parts = page_name.split('/')
	backnav = []
	for i in range(len(parts)):
		ln = "/docs/"
		for j in range(i+1):
			ln += parts[j] + "/"
		backnav.append({'link':ln, 'title': linkToTitle(parts[i])})

	if len(backnav) <= 1:
		backnav = None

	# TODO: @title directive. 
	title = linkToTitle(page_name)

	x = readfile(path)
	x = markdown.markdown(x)

	d = os.stat(path)
	t = time.localtime(int(d.st_mtime))
	editstr = time.strftime("%B %d, %Y", t)

	return render_to_response('markdown-base.html', {
									'title':	title,
									'content':	x,
									'editdate':	editstr,
									'githubUrl': githubUrl,
									'backnav': backnav,
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
