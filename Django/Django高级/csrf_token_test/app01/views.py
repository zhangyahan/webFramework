from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	ret_str = """
		<a href="/login/">login or register</a>
	"""
	return HttpResponse(ret_str) 


def login(request):
	
	if request.method == "GET":
		return render(request, 'login.html')
	else:
		name = request.POST.get('name', '')
		pwd = request.POST.get('password', '')
		if name == 'zyh' and pwd == '123456':
			return HttpResponse('Wolcome my site')
		return HttpResponse('username or password is not font')



def transfor(request):
	if request.method == 'GET':
		return render(request, 'transfor.html')
	else:
		return HttpResponse('OK')