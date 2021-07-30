from datetime import time
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . models import Users
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'userReview/index.html')




def signUp(request):
    if request.method == 'POST':
        insertQuery = Users(first_name = request.POST['first_name'],
                            last_name = request.POST['last_name'],
                            email = request.POST['email'],
                            password = request.POST['password'],
                            gender = request.POST['gender'],
                            createdate = timezone.now())
        insertQuery.save()
        return redirect('signIn')
    return render(request, 'userReview/signUp.html')



def signIn(request):
    if request.method == 'POST':
        loginQuery = Users.objects.filter(email = request.POST['email'], password = request.POST['password'])
        if loginQuery.count() > 0:
            return redirect('userDashboard')
        else:
            return render(request, 'userReview/signIn.html', {'msginvalid' : 'username and password is invalid'})
    return render(request, 'userReview/signIn.html')




def userDashboard(request):
    return render(request, 'userReview/userDashboard.html')