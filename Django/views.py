from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def list1(request):
    return render(request, "list1.html")


def list2(request):
    return render(request, "list2.html")


def list3(request):
    dict = {"name": {"英文": "ikirito", "中文": "紫风"}}  # 字典排列
    # dict={'name':['ikirito','紫风']}  #列表排列
    return render(request, "list3.html", dict)


def login(request):
    str = {"user": "ikirito", "password": "admin"}

    return render(request, "login.html", str)


def result(request):

    if request.GET['user']:
        a = request.GET['user']
    if request.GET['password']:
        b = request.GET['password']
    
    return HttpResponse('账号：'+a+'<br>密码：'+b)