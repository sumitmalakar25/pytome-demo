from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

class Success1(View):
    def get(self, request):
        return render(request, 'success1.html')
