from django.shortcuts import render,  HttpResponse
from . import models
from . import Paging
# Create your views here.





def book(request):
	context = {}
	# 每页数量
	if request.method == 'GET':
		# 获取全部数据
		books_count = models.Book.objects.all().count()
		# 获取当前页
		page_num = request.GET.get('page', '')
		try:
			if page_num:
				page_num = int(page_num)
		except Exception as e:
			page_num = 1

		if page_num <= 1:
			page_num = 1
		elif page_num >= books_count:
			page_num = books_count
		



	pag = Paging.Paging(books_count)
	# 生成页码
	books_list = pag.page_number(page_num)
	print(books_list)

	# 获取上一页下一页按钮url
	up_page, down_page = pag.up_down_page(page_num)
	print(up_page, down_page)

	# 起始条数,终止条数
	start_strip, end_strip = pag.start_end_strip(page_num)

	books_info = models.Book.objects.all()

	# 返回数据
	context['books_list'] = books_list
	context['current_page'] = page_num
	context['up_page'] = up_page
	context['down_page'] = down_page
	context['books'] = books_info[start_strip: end_strip]
	context['first_page'] = 1  # 首页
	context['last_page'] = pag.total  # 尾页
	return render(request, 'books.html', context)


def dept(request):
	if request.method == 'GET':
		current_page = int(request.GET.get('page', ''))
		if not current_page:
			current_page = 1
		depts_count = models.Department.objects.all().count()

		if current_page >= depts_count:
			current_page = depts_count
		elif current_page <= 1:
			current_page = 1
		

		pag = Paging.Paging(depts_count)

		print('总页数>>>>>>>>>>>>>>>>>>>', pag.total)
		print('上一页和下一页>>>>>>>>>>>>', pag.up_down_page(current_page))
		print('页码>>>>>>>>>>>>>>>>>', pag.page_number(current_page))
		print('条数>>>>>>>>>>>>>>>', pag.start_end_strip(current_page))
		print(depts_count)
		print(current_page, '>>>>>>>>>>>>>>')
		return HttpResponse('ok')