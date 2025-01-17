from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# This function will add new items and show All Items.....
def add_show(request):
  if request.method == 'POST':
    fm = StudentRegistration(request.POST)
    if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      ps = fm.cleaned_data['password']
      reg = User(name =nm,email=em,password=ps)
      # fm.save()
      reg.save()
      fm = StudentRegistration()
  else:
    fm = StudentRegistration()
  stud =User.objects.all()# for retrieve the data...
  return render(request,'enroll/addandshow.html', {'form':fm, 'stu': stud })

# This function will Update ...
def update_data(request,id):
  if request.method == 'POST' :
    pi = User.objects.get(pk = id)
    fm = StudentRegistration(request.POST,instance=pi)
    if fm.is_valid():
     fm.save()
  else:
    pi = User.objects.get(pk = id)
    fm = StudentRegistration(request.POST,instance=pi)

  return render(request,'enroll/updatestudent.html', {'form':fm})
  




# This Function will Delete data
def delete_data(request,id):
  if request.method == 'POST':
    pi = User.objects.get(pk = id)
    pi.delete()
    return HttpResponseRedirect('/')

