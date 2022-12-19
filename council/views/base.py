from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

class Base(View):
    def get(self, request):
        return render(request, 'base.html')
