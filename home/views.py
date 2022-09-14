from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


def index(request):
    if request.method == 'POST':
        Username = request.POST.get("uname")
        pass1 = request.POST.get("psw")

        user = authenticate(username=Username, password=pass1)

        if user is not None:
            auth_login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "payment.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('index')

    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        fname = request.POST.get("Fname")
        lname = request.POST.get("Lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if User.objects.filter(username=Username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return redirect('index')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('index')

        if len(Username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('index')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('index')

        if not Username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('index')

        user = User.objects.create_user(Username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()

        messages.success(
            request, "Your Account has been created succesfully!! ")
        return redirect('index')

    return render(request, "signup.html")


def payment(request):
    if request.method == "POST":

        name = request.POST.get("name")
        lname = request.POST.get("lname")
        number = request.POST.get("number")
        upi = request.POST.get("upi")
        email = request.POST.get("email")
        zipc = request.POST.get("zip")
        amount = int(request.POST.get("amount"))*100
        currency = "INR"

        client = razorpay.Client(auth=("rzp_live_Vjj3uP8XwfZut7", "rk8pcH32KrbdsB3bkSVyKbBz"))

        DATA = {
                "amount": 5000000,
                "currency": "INR",
                "receipt": "receipt#1",
                   "notes": {
                           "key1": "value3",
                          "key2": "value2"
                           }
                   }
        payment = client.order.create(data=DATA)
        


        payment['money']=5000000
        # context['razorpay_order_id'] = payment['id']
        # context['razorpay_amount'] = amount
        # context['currency'] = currency
        # context['name'] = name
        # data = {'payment': payment, 'context': context}

        
        
        print(payment)
        return render(request, 'payment.html' )


    return render(request ,"payment.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')

   


