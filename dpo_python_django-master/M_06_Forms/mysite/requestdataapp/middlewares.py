import time

from django.http import HttpRequest
from django.shortcuts import render


def setup_useragent_on_request_middleware(get_response):
    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response

    return middleware


class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.response_count = 0
        self.exceptions_count = 0
        self.request_time = {}

    def __call__(self, request: HttpRequest):
        time_delay = 5
        if not self.request_time:
            print("First request")
        else:
            if round(time.time()) * 1 - self.request_time['time'] < time_delay and self.request_time['ip_address'] == request.META.get('REMOTE_ADDR'):
                print("Too many request per time. Wait 5 sec.")
                return render(request, 'requestdataapp/request-error.html')
        self.request_time = {'time': round(time.time()) * 1, 'ip_address': request.META.get('REMOTE_ADDR')}

        self.requests_count += 1
        print("+1 request. Now we have:", self.requests_count)
        response = self.get_response(request)
        self.response_count += 1
        print("+1 response. Now we have:", self.response_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print(f"got {self.exceptions_count} exceptions now")

