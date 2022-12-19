from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

class Success(View):
    def get(self, request):
        return render(request, 'success.html')
