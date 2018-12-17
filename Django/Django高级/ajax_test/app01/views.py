from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, 'index.html')


def ajax_test(request):
	if request.method == "GET":
		first_num = request.GET.get("first_num", "")
		last_num = request.GET.get("last_num", "")

		if first_num and last_num:
			eq_num = int(first_num) + int(last_num)


		from django.http import JsonResponse
		return JsonResponse({"data": eq_num})
	else:
		first_num = request.POST.get("first_num", "")
		last_num = request.POST.get("last_num", "")

		if first_num and last_num:
			eq_num = int(first_num) + int(last_num)


		from django.http import JsonResponse
		return JsonResponse({"data": eq_num})