import datetime

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from .forms import StringForm
import hashlib

from .models import RequestLog


def index(req) -> HttpResponse:
    form = StringForm()
    return render(req, 'index.html', {'form': form})


def hash_service(req) -> HttpResponse:
    # timestamp the request arrived
    timestamp = datetime.datetime.utcnow()  # save time in utc format

    # get user query parameter 'string'
    string = req.GET.get('string', '')
    if string == '':
        return HttpResponseBadRequest()

    # encode user query to bytes
    hash_obj = hashlib.sha1(string.encode())

    # get the last 256 characters of the hexadecimal representation of the hash
    hex_repr = hash_obj.hexdigest()[-256:]

    # Save the request
    RequestLog.objects.create(timestamp=timestamp, query=string, hash=hex_repr)
    return JsonResponse({'hash': hex_repr})


def request_log(req) -> HttpResponse:
    request_log_list = RequestLog.objects.all().order_by('-id')
    return render(req, 'request_log.html', { 'request_log_list': request_log_list})
