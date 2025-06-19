from django.shortcuts import render

def about(request):
    return render(request, 'siteinfo/about.html')

def terms(request):
    return render(request, 'siteinfo/terms.html')
