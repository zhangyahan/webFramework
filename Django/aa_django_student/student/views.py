from django.shortcuts import render, HttpResponse
from student import models
import json


def student(reqeust):
    students = models.Student.objects.all()
    classes = models.Classes.objects.all()
    context = {}

    context['students'] = students
    context['classes'] = classes
    return render(reqeust, 'student.html', context)


def addStudent(reqeust):
    context = {
        'status': True,
        'message': None
    }
    if reqeust.method == "POST":
        username = reqeust.POST.get('username', '')
        userage = reqeust.POST.get('userage', '')
        gender = reqeust.POST.get('gender', '')
        classes = reqeust.POST.get('classes', '')

        if username and userage and gender and classes:
            obj = models.Student.objects.create(
                username=username,
                age=int(userage),
                gender=int(gender),
                cs_id=int(classes),
            )

            context['stu_id'] = obj.id
        else:
            context['status'] = False
            context['message'] = '用户输入错误'
    return HttpResponse(json.dumps(context, ensure_ascii=False))


def delStudent(reqeust):
    context = {'status': True,}
    try:
        delUid = reqeust.GET.get('delUid', '')
        models.Student.objects.filter(id=delUid).delete()
    except Exception as e:
        context['status'] = False
    
    return HttpResponse(json.dumps(context))
