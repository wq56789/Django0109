from django.shortcuts import render
from adduser.models import stuTest
# Create your views here.

def bd(request):
    return render(request, 'bd.html')

#获取网页信息 添加到 数据库
def adduser(request):
    name=request.POST['name']
    sex = request.POST['sex']
    age = request.POST['age']
    jg = request.POST['jg']
    stul = stuTest(name=name, sex=sex, age=age,jg=jg)
    stul.save()
    return render(request,'tj.html')

#查询
def select(request):
    list=stuTest.objects.all()
    return render(request,'list.html',{'list':list})

#修改
def find(request):
    sid=request.GET['sid']
    list=stuTest.objects.get(id=sid)
    return render(request,'update.html',{'list':list})
#获取网页信息 更新到 数据库
def update(request):
    id=request.POST['id']
    name=request.POST['name']
    sex=request.POST['sex']
    age=request.POST['age']
    jg=request.POST['jg']
    stu=stuTest.objects.get(id=id)
    stu.name=name
    stu.sex=sex
    stu.age=age
    stu.jg=jg
    stu.save()
    list=stuTest.objects.all()
    return render(request,'list.html',{'list':list})

#删除个人信息
def delete(request):
    id=request.GET['sid']
    stuTest.objects.get(id=id).delete()
    list = stuTest.objects.all()
    return render(request, 'list.html', {'list': list})