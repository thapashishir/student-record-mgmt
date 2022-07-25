from django.shortcuts import redirect, render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class UserLoginView(View):
    def get(self, request):
        return render(request, "user_mgmt/login.html")

    def post(self,request):
        users = [
            {
                "user_name" : "admin",
                "password"  : "admin",
                "role"      : "admin"
            },
            {
                "user_name" : "user",
                "password"  : "user",
                "role"      : "user"
            }

        ]
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")

        for user in users:

            if  user_name == user["user_name"] and password == user["password"]: 
                request.session["current_user"] = {
                    "user_name":  user["user_name"],
                    "role": user["role"]
                }
                return redirect("/student/list")
        
        return  HttpResponse("<h1>Invalid User Name Password</h1>")

class UserLoginOutView(View):
    def get(self, request):
        request.session["current_user"] = None
        return redirect("/login")

