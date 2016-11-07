from django.shortcuts import render, redirect


def index(request):
    context = {'testmsg': 'hello world!'}
    return render(request, 'helloworld/index.html', context)
