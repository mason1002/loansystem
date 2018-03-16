from django.shortcuts import render
from user_app import models

# Create your views here.

user_list = [
    {"user": "ass", "pwd": "123"},
    {"user": "bitch", "pwd": "abc"},
]


def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("Loan System")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()

    return render(request, "index.html", {"data": user_list})
