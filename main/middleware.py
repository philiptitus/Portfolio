from django.shortcuts import render, redirect
import os
from django.utils.deprecation import MiddlewareMixin

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.access_key = 'strovold'  # Replace with your secret key

    def __call__(self, request):
        # Check for the access key in the URL parameters
        if request.GET.get('access_key') == self.access_key:
            return self.get_response(request)

        # Allow access to the admin page and media files
        if request.path.startswith('/philip/') or request.path.startswith('/media/'):
            return self.get_response(request)

        # Show the "Under Construction" page for all other requests
        return render(request, 'under_construction.html')






class Redirect404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return redirect('/404/')
        return response
