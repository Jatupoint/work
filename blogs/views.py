from django.shortcuts import render,redirect
from .models import Members,Class,Student,Teacher
from django.http import HttpResponse
from django.contrib.auth.models import User,auth,Group
from django.contrib import messages
# Create your views here.
def homepage(request):
    #เอาข้อมูลมาจาก model
    members = User.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    classrooms = Class.objects.all()
    return render(request,'home.html',{'member': members,'student':students,'teacher':teachers,'classroom':classrooms})
                                        
def loginform(request):
    return render(request,'loginform.html')

def loginform_teacher(request):
    return render(request,'login_teacher.html')

def regis_student(request):
    return render(request,'regis_student.html')

def regis_success(request):
    return render(request,'regis_success.html')

def groupform(request):
    return render(request,'creategroup.html')

def joinform(request):
    return render(request,'joinform.html')

def regis_teacher(request):
    return render(request,'regis_teacher.html')

def creategroup_form(request):
    return render(request,'creategroup_form.html')

def addMembers(request):
    username    = request.POST['username']
    firstname   = request.POST['firstname']
    lastname    = request.POST['lastname']
    email       = request.POST['email']
    password    = request.POST['password']
    repassword  = request.POST['repassword']
    if password == repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request,'มีผู้ใช้ลงทะเบียนในระบบแล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email นี้ลงทะเบียนแล้ว')
            return redirect('/register')
        else :
            user =User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname ,
            email=email,
            password=password
             )
            user.save()
            student = Student.objects.create(
            username = username,
            fullname = firstname,
            email = email,
            classroom = 'offline'
            )
            student.save()
            return redirect('/regis_success')
    else:
        messages.info(request,'รหัสผ่านไม่ตรงกัน')
        return redirect('/register')

def addTeacher(request):
    username    = request.POST['username']
    firstname   = request.POST['firstname']
    lastname    = request.POST['lastname']
    email       = request.POST['email']
    password    = request.POST['password']
    repassword  = request.POST['repassword']
    if password == repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request,'มีผู้ใช้ลงทะเบียนในระบบแล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email นี้ลงทะเบียนแล้ว')
            return redirect('/register')
        else :
            user =User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname ,
            email=email,
            password=password
             )
            user.save()
            teacher = Teacher.objects.create(
            username = username,
            fullname = firstname,
            email = email,
            classroom = 'offline'
            )
            teacher.save()
            return redirect('/regis_success')
    else:
        messages.info(request,'รหัสผ่านไม่ตรงกัน')
        return redirect('/register')

def login(request):
    username    = request.POST['username']
    password    = request.POST['password']
    #auth login
    user=auth.authenticate(username=username,password=password)
    if  user is not None:
        auth.login(request,user)
        if Student.objects.filter(classroom='offline').exists():
            Student.objects.update(classroom='online')
        return redirect('/')
        
    else:
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginform')

def login_teacher(request):
    tusername = request.POST['username']
    username    = request.POST['username']
    password    = request.POST['password']
    #auth login
    if  Teacher.objects.filter(username=tusername).exists() :
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.info(request,'ไม่พบข้อมูล')
            return redirect('/loginform_teacher')
    else :
        messages.info(request,'คุณไม่ใช่อาจารย์')
        return redirect('/loginform_teacher')

def Join(request):
        username = request.POST['username']
        code = request.POST['code']
        if Class.objects.filter(username=username,code=code).exists():
            Class.objects.create(username=username,code=code)
            return redirect('/regis_success')
        elif Class.objects.filter(code=code).exists():
            Class.objects.create(username=username,code=code)
            return redirect('/regis_success')
        else :
            messages.info(request,'ไม่มีคลาสเรียนนี้')
            return redirect('/joinform')


def CreateGroup(request):
        username = request.POST['username']
        code = request.POST['code']
        if Class.objects.filter(code=code).exists():
            messages.info(request,'ไม่มีคลาสเรียนนี้')
            return redirect('/regis_success')
        else :
            Class.objects.create(username=username,code=code)
            return redirect('/regis_success')

def logout(request):
    auth.logout(request)
    return redirect('/loginform')

def logout_teacher(request):
    auth.logout(request)
    c=Class.objects.all()
    c.delete()
    return redirect('/')