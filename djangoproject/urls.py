from django.contrib import admin
from django.urls import path
from blogs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('login',views.login),
    path('login_teacher',views.login_teacher),
    path('regis_student',views.regis_student),
    path('regis_teacher',views.regis_teacher),
    path('addMembers',views.addMembers),
    path('addTeacher',views.addTeacher),
    path('loginform',views.loginform),
    path('loginform_teacher',views.loginform_teacher),
    path('regis_success',views.regis_success),
    path('logout',views.logout),
    path('logout_teacher',views.logout_teacher),
    path('creategroup_form',views.creategroup_form),
    path('joinform',views.joinform),
    path('CreateGroup',views.CreateGroup),
    path('Join',views.Join),
]
