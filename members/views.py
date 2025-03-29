from django.http import HttpResponse
from django.template import loader
from .models import user
def get_homepage(request):
  template = loader.get_template('page.html')
  users = user.objects.all()
  context = {'list_of_users' : users}
  return HttpResponse(template.render(context, request))

def get_info(request, id):
  template = loader.get_template('lenhanbo.html')
  users = user.objects.get(id = id)
  context = {'user' : users}
  return HttpResponse(template.render(context, request))