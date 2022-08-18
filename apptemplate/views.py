from django.shortcuts import render
# from django.http import HttpResponse


def projects(request):
    msg = 'Welcome cunt face'
    context = {
        'msg': msg
    }
    return render(request, 'apptemplate/projects.html', context)

def project(request, pk):
    return render(request, 'apptemplate/single-project.html')
