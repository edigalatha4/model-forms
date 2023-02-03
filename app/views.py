from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    TFO=TopicForm()
    d={'form':TFO}
    if request.method=='POST':
        fd=TopicForm(request.POST)
        if fd.is_valid():
            tn=fd.cleaned_data['topic_name']
            T=Topic.objects.get_or_create(topic_name=tn)[0]
            T.save()
            return HttpResponse('topic data is inserted successfully')

    return render(request,'insert_topic.html',d)


def topic_modelform(request):
    TMFO=ModelTopicForm()
    d={'form':TMFO}
    if request.method=='POST':
        FD=ModelTopicForm(request.POST)
        print(1)
        if FD.is_valid():
            print(2)
            FD.save()
            return HttpResponse('topic is inserted successfully by using model form')
    return render(request,'topic_modelform.html',d)


def webpage_modelform(request):
    WMFO=ModelWebpageForm()
    d={'form':WMFO}
    if request.method=='POST':
        FD=ModelWebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('webpage is inserted successfully by using model form')
    return render(request,'webpage_modelform.html',d)


def access_modelform(request):
    AMFO=ModelAcccessRecordsForm()
    d={'form':AMFO}
    if request.method=='POST':
        FD=ModelAcccessRecordsForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('accessrecord is inserted successfully by using model form')
    return render(request,'access_modelform.html',d)
