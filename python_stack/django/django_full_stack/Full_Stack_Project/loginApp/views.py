from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import user
#render
def logout(request):
    request.session.flush()
    return redirect('/login')

def welcome(request):
    if 'user_id' in request.session:
        print(user.objects.get(id=request.session['user_id']))
        context = {
            'user' : user.objects.get(id=request.session['user_id'])
        }
        return render(request, 'welcome.html', context)
    return render(request, 'login.html')

#POST
def login(request):
    if request.method=='POST':
        print("if statment in login method POST ran")
        errors = user.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print("error in login method is running")
            return redirect('/login')
        # see if the username provided exists in the database
        user_login = user.objects.filter(email=request.POST['login_email']) 
        print(f"user login={user_login}")
        # why are we using filter here instead of get?
        if user_login: # note that we take advantage of truthiness here: an empty list will return false
            logged_user = user_login[0] 
            print(f"logged_user={logged_user}")
            # assuming we only have one user with this username, the user would be first in the list we get back
            # of course, we should have some logic to prevent duplicates of usernames when we create users
            # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
            print(bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()))
            if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
                request.session['user_id'] = logged_user.id
                # never render on a post, always redirect!
                print("login succesful")
                return redirect('/login/welcome')
            else:
                messages.error(request, "wrong password")
                return redirect('/login')

    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route
    return render(request, 'login.html')

def create_user(request):
    errors = user.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        fname = request.POST['form_first_name']
        lname = request.POST['form_last_name']
        email = request.POST['form_email']
        birthday = request.POST['form_birthday']
        rawPassword = request.POST['form_password']
        hashPass = bcrypt.hashpw(rawPassword.encode(), bcrypt.gensalt()).decode()
        # user.objects.create(first_name=fname, last_name=lname, email=email, birthday=birthday, password=password)
        # request.session['new_user.email'] = email
        print(f"name: {fname} {lname}")
        print(f"email: {email} ")
        print(f"birthday: {birthday} ")
        print(f"password: {rawPassword} ")
        print(f"hash: {hashPass} ")
        newUser = user.objects.create(first_name=fname, last_name=lname, email=email, birthday=birthday, password=hashPass)
        request.session['User_id'] = newUser.id
        return redirect("/login/welcome")
