from django.shortcuts import render

# Create your views here.

USER_LIST = []
for i in range(1,999):
    temp = {'name': 'root' + str(i), 'age': i}
    USER_LIST.append(temp)

# def index(request):
#     per_page_count = 20
#     current_page = request.GET.get('p', '')
#     if not current_page:
#         current_page = 1
#     current_page = int(current_page)
#     # p = 1
#     # 0 ~ 9

#     # p = 2
#     # 10 ~ 19
#     start = (current_page - 1) * per_page_count
#     end = current_page * per_page_count

#     data = USER_LIST[start:end]

#     context = {}
#     up_page = current_page - 1
#     next_page = current_page + 1

#     context['user_list'] = data
#     context['up_page'] = up_page
#     context['next_page'] = next_page

#     return render(request, 'index.html', context)


# Django自带的分页
def index(request):
    context = {}
    from django.core.paginator import Paginator
    # 全部数据: USER_LIST, 
    # per_page: 每页显示条目数量
    # count: 数据中个数
    # num_pages: 总页数
    # page_range: 总页数的索引范围
    # page: page对象(是否具有下一页,是否有上一页)
    current_page = request.GET.get('p')
    # Paginator对象
    paginator =  Paginator(USER_LIST, 10)  # 每页显示的条数
    try:
        # Page对象
        posts = paginator.page(current_page)
        # has_next:               是否有下一页
        # next_page_number        下一页页码
        # has_previous            是否有上一页
        # previous_page_number    上一页页码
        # object_list             分页之后的数据列表, 已经切片好的数据
        # number                  当前页
        # paginator               paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context['posts': posts]
    return render(request, 'index.html', context)