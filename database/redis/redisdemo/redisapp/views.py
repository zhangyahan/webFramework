from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import json
# Create your views here.


def index(request):
    key = 'haha'
    cache.set(key, json.dumps('wowoow'), settings.NEVENEVER_REDIS_TIMEOUT)
    return render(request, 'test.html')
