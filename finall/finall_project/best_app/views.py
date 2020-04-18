from django.shortcuts import render
from best_app.models import User
# Create your views here.
def index(request):
    # my_dict = {"success_me":"Hi i am from index.html"}
    return render(request, "finall_project/index.html")

def users (request):
    love_list =  User.objects.order_by("first_name")
    samir_dict = {"love": love_list}
    return render(request, "finall_project/users.html", context= samir_dict)
