from django.shortcuts import render

#homepage of the blog website
def home(request):
    return render(request, 'expt.html')
