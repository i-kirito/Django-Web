from django import http
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def list1(request):
    return render(request, 'list1.html')
def list2(request):
    return render(request, 'list2.html')
def list3(request):
    dict={'name':{'英文':'ikirito','中文':'紫风'}}  #字典排列
    # dict={'name':['ikirito','紫风']}  #列表排列
    return render(request, 'list3.html',dict)
def html(request):
    str="""
"""
    return http.HttpResponse(str)