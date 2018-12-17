import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from . import models
from . import Paging
# Create your views here.


def serialize(request):
	person = models.Person.objects.all()
	person_list = []
	for i in person:
		person_list.append({"name": i.name, "age": i.age})

	# return JsonResponse({"data": person_list})
	return HttpResponse(json.dumps(person_list, ensure_ascii=False))
	# content_type='appliaction/json,charset=utf-8'  # 下载
	# ret = serializers.serialize('json', person)  # 序列化
	# return JsonResponse(ret, safe=False)


def sweetalert(request):
	if request.method == "GET":
		person_count = models.Person.objects.all().count()
		pag = Paging.Paging(total=person_count)
		page_num = request.GET.get('page', '')
		try:
			if page_num:
				page_num = int(page_num)
			if page_num <= 1:
				page_num = 1
			if page_num >= pag.total:
				page_num = pag.total

		except Exception as e:
			page_num = 1

		pages_list = pag.page_number(page_num)  # 页码
		up_page, down_page = pag.up_down_page(page_num)  # 上一页,下一页
		start_strip, end_strip = pag.start_end_strip(page_num)

		context = {}
		persons = models.Person.objects.all()
		context['persons'] = persons[start_strip:end_strip]
		context['pages_list'] = pages_list
		context['up_page'] = up_page
		context['down_page'] = down_page

		return render(request, 'sweetalert.html', context)

	else:
		del_id = request.POST.get('del_id')
		models.Person.objects.filter(id=del_id).delete()
		import json
		return HttpResponse(json.dumps({'status': 1}, ensure_ascii=False))


