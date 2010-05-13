# Possibilistic
# 	MAIN VIEW

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('index.html')

# Note: ignore second param, used in regex grouping from url dispatcher
def about(request, x):
	return render_to_response('about.html')


