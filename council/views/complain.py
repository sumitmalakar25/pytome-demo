from django.shortcuts import render, redirect
from council.models import Complain
from django.views import View

class Complaint(View):
    def get(self,request):
        return render(request,'complain.html')

    def post(self,request):
        postdata = request.POST
        date=postdata.get('date')
        name = postdata.get('name')
        phone = postdata.get('phone')
        address = postdata.get('address')
        complain = postdata.get('complain')

        value={
            'name':name,
            'phone':phone,
            'address':address,
        }
        error_message = None
        complain = Complain(date=date,name=name,phone=phone,address=address,complain=complain)

        error_message = self.validatecomplain(complain)
        if not error_message:
            complain.register()
            return redirect('success1')
        else:
            data = {'error':error_message,'value':value}
            return render(request,'complain.html',data)

    def validatecomplain(self,complain):
        error_message = None
        if(not complain.name):
            error_message = 'Name Required!!'
        elif (not complain.phone):
            error_message = 'Phone Number Required!!'
        elif len(complain.phone)<10:
            error_message = 'Phone no not valid'
        elif (not complain.address):
            error_message = 'address Required!!'
        elif (not complain.complain):
            error_message = 'complain Required!!'
        elif complain.isExists():
            error_message = 'Email Already Exist'
        return error_message