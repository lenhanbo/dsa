from django.http import HttpResponse, Http404
from django.template import loader
from .models import user
from .models import Comment as user_comment
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from .forms import Comment
def get_homepage(request):
  template = loader.get_template('page.html')
  users = user.objects.all().filter(first_name__startswith='x')
  # category  = ['Tìm kiếm', 'Tìm bạn để ăn', 'Khám phá blog']
  category  = {'Tìm kiếm' : 'timkiem', 'Tìm bạn để ăn' : 'timban', 'Khám phá blog' :'khampha'}
  my_form = Comment() 
  all_comments = user_comment.objects.all()
  context = {
    'list_of_users' : users,
    'categories' : category,
    'forms' : my_form,
    'comments' : all_comments,
  }
  return HttpResponse(template.render(context, request))

def submit_form(request):
  if request.method == "POST":
    my_form = Comment(request.POST)
    if my_form.is_valid():
      my_form.save()
  return redirect("/homepage/")

def delete_comment(request, id):
  if request.method == "POST":
    comment_to_delete = user_comment.objects.get(id = id)
    comment_to_delete.delete()
  return redirect("/homepage/")

    

def get_info(request, id):
  template = loader.get_template('lenhanbo.html')
  
  users = get_object_or_404(user, id = id)
  
  context = {'user' : users}
  return HttpResponse(template.render(context, request))


def timban(request):
  template = loader.get_template('danhsachban.html')
  user_list = user.objects.all()
  context = {
    'user_list': user_list
  }
  return HttpResponse(template.render(context, request))