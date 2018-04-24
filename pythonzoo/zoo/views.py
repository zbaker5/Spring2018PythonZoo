from django.shortcuts import render

# Create your views here.

def index(request):
	temporaryData = "Zach"
	return render(
		request,
		"index.html",
		context = { 'temporaryData' : temporaryData }
	)	
