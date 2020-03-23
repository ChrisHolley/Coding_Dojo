from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from loginApp.models import user
from .models import Messages, Comments

# from .models import NAME_OF_YOUR_MODEL_HERE
#render

#get
def WALL(request):
    if 'user_id' in request.session:
        print(user.objects.get(id=request.session['user_id']))
        context = {
            'user' : user.objects.get(id=request.session['user_id']),
            'All_Messages' : Messages.objects.all(),
            'All_Comments' : Comments.objects.all()
        }
        return render(request, 'wall_welcome.html', context)
    return redirect('/login')


#POST
def new_post(request):
    if 'user_id' in request.session:
        # errors = Show.objects.show_validator(request.POST)
        # if len(errors) > 0:\
            # for key, value in errors.items():
            #     messages.error(request, value)
            # return redirect('')
        NEW_POST_MESSAGE = request.POST['New_Post']
        USER = user.objects.get(id=request.session['user_id'])
        newmsg = Messages.objects.create(message=NEW_POST_MESSAGE, user=USER)
        print(newmsg)
        return redirect('/wall')
    return redirect('/login')

def new_comment(request):
    if 'user_id' in request.session:
        NEW_COMMENT = request.POST['New_Comment']
        USER = user.objects.get(id=request.session['user_id'])
        MSG = Messages.objects.get(id=request.POST['msg_id'])
        newcomment = Comments.objects.create(comment=NEW_COMMENT, messages=MSG, user=USER)
        print(newcomment)
        return redirect('/wall')
    return redirect('/login')

def delete_comment(request):
    errors = Comments.objects.delete_comment_validator(request.POST)
    if 'user_id' in request.session:
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wall')
        else:
            this_comment = Comments.objects.get(id=request.POST['delete_comment_id'])
            this_comment.delete()
    return redirect('/wall')

