from datetime import time
from django.contrib.messages.constants import SUCCESS
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from django.contrib import messages
from django.shortcuts import redirect, render
from . models import Review, Users
from django.utils import timezone

# Create your views here.
def index(request):
    
    review = Review.objects.all()
    reviewcol = Review.objects.values('rating', 'reviewto')
    context = {'review': review,
               'reviewcol': reviewcol,}
    return render(request, 'userReview/index.html', context)




def signUp(request):
    if request.method == 'POST':
        checkemail = Users.objects.filter(email = request.POST['email'])
        if checkemail.count() > 0:
            messages.add_message(request, messages.WARNING, 'Email Id is All Ready Exists')
            return render(request, 'userReview/signUp.html')
        else:
            insertQuery = Users(first_name = request.POST['first_name'],
                                last_name = request.POST['last_name'],
                                email = request.POST['email'],
                                password = make_password (request.POST['password']),
                                gender = request.POST['gender'],
                                createdate = timezone.now())
            insertQuery.save()
            messages.add_message(request, messages.SUCCESS, 'Your account has been created')
        return render(request, 'userReview/signUp.html')
    return render(request, 'userReview/signUp.html')



def signIn(request):
    if request.method == 'POST':
        loginQuery = Users.objects.filter(email = request.POST['email']).values_list('id','password')
        passcheck = loginQuery[0][1]
        if loginQuery.count() > 0 and check_password(request.POST['password'],passcheck):
            loginQuery[0][0]
            request.session['logged'] = loginQuery[0][0]
            return redirect('reviewDashboard')
        else:
            return render(request, 'userReview/signIn.html', {'msginvalid' : 'username and password is invalid'})
    return render(request, 'userReview/signIn.html')




def reviewDashboard(request):
    if request.method == 'POST':
        if Review.objects.filter(users_id = request.session['logged'], reviewto = request.POST['reviewto']).count() == 0:
            rto = request.POST["textother"]  if request.POST["reviewto"]=="other" else request.POST["reviewto"] # insert Other Company Review
            insertReview = Review(users_id = request.session['logged'], # insert review in database
                                rating = request.POST['rating'],
                                reviewto = rto,
                                reviewdesc = request.POST['reviewdesc'], 
                                reviewdate = timezone.now())
            insertReview.save() 
            return redirect('reviewDashboard')
        elif Review.objects.filter(users_id = request.session['logged']):
            return render(request, 'userReview/reviewDashboard.html', {'errormsg' : 'You have already provided review'})
        
    context = {'showReviewData' : Review.objects.filter(users_id = request.session['logged'])}
    return render(request, 'userReview/reviewDashboard.html', context)


def reviewEdit(request):
    if request.method == 'POST':
        rto = request.POST["textother"]  if request.POST["reviewto"]=="other" else request.POST["reviewto"]
        editReview = Review.objects.get(pk=request.POST['textid'])
        editReview.users_id = request.session['logged']
        editReview.rating = request.POST['rating']
        editReview.reviewto = rto
        editReview.reviewdesc = request.POST['reviewdesc']
        editReview.reviewdate = timezone.now()
        editReview.save()
        return redirect('reviewDashboard')
    else:
        context = {'editValues' :Review.objects.get(pk=request.GET['q'])}
        return render(request, 'userReview/reviewEdit.html', context)




def reviewDelete(request):
    r = Review.objects.get(pk=request.GET["q"])
    r.delete()
    return redirect('reviewDashboard')


def userProfile(request):
    if request.session.has_key('logged'):
        userData = Users.objects.get(pk = request.session['logged'])
        context = {'userData' : userData}
        return render(request, 'userReview/userProfile.html', context)
    else:
        return redirect('signIn')




def userEditProfile(request):
    if request.method == 'POST':
        userEdit = Users.objects.get(pk = request.session['logged'])
        userEdit.first_name = request.POST['first_name']
        userEdit.last_name = request.POST['last_name']
        userEdit.email = request.POST['email']
        userEdit.password = request.POST['password']
        userEdit.gender = request.POST['gender']
        userEdit.save()
        return redirect('userProfile')
    valueShow = Users.objects.get(pk = request.session['logged'])
    context = {'valueShow' : valueShow}
    return render(request, 'userReview/userEditProfile.html', context)






def logOut(request):
    del request.session['logged']
    return redirect('/')