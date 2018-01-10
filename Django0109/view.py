from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'hello.html')



# py={
#     1:{
#         '姓名':'王琪',
#         '性别':'男',
#         '年龄':23,
#         '学号':789,
#     },
#     2:{
#         '姓名':'赵本分',
#         '性别':'男',
#         '年龄':23,
#         '学号':456
#     },
#     3:{
#         '姓名':'魏东',
#         '性别':'男',
#         '年龄':23,
#         '学号':123
#     }
# }
#
# def BL():
#     for i,j in py.items():
#         print(i,j)
#
# print('------------------欢迎进入学生管理系统--------------------')
# BL()

