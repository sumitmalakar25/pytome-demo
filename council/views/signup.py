from django.shortcuts import render, redirect
from council.models import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        address = postdata.get('address')

        value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email,
            'address':address,
        }
        error_message = None
        customer = Customer(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password,address=address)

        error_message = self.validatecustomer(customer)
        if not error_message:
            customer.register()
            return redirect('success')
        else:
            data = {'error':error_message,'value':value}
            return render(request,'signup.html',data)

    def validatecustomer(self,customer):
        error_message = None
        if(not customer.first_name):
            error_message = 'First Name Required!!'
        elif len(customer.first_name)<4:
            error_message = 'First name must be more than 4 character long'
        elif (not customer.last_name):
            error_message = 'Last Name Required!!'
        elif (not customer.phone):
            error_message = 'Phone Number Required!!'
        elif len(customer.phone)<10:
            error_message = 'Phone no not valid'
        elif (not customer.password):
            error_message = 'Password Required!!'
        elif len(customer.password)<6:
            error_message = 'Password must be 6 char long'
        elif (not customer.address):
            error_message = 'address Required!!'
        elif customer.isExists():
            error_message = 'Email Already Exist'
        return error_message