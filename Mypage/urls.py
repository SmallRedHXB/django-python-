from django.urls import path
from . import views


app_name='[Mypage]'

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('selectsubject/', views.selectsubject, name='selectsubject'),
    path('modifypwd/', views.modifypwd, name='modifypwd'),
    path('studentinfo/', views.studentinfo, name='studentinfo'),
    path('classschedule/', views.classschedule, name='classschedule'),
    path('selsubnotice/', views.selsubnotice, name='selsubnotice'),
    path('selsubhelp/', views.selsubhelp, name='selsubhelp'),
    path('gradecheck/', views.gradecheck, name='gradecheck'),
    path('login/', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),
    path('do_modifypwd/', views.do_modifypwd, name='do_modifypwd'),
    path('studentinfo_update/', views.studentinfo_update, name='studentinfo_update'),
    path('studentinfo_update_save/', views.studentinfo_update_save, name='studentinfo_update_save'),
    path('getcourse/', views.getcourse, name='getcourse'),
    path('get_classschedule/', views.get_classschedule, name='get_classschedule'),
    path('selectsubject_action/', views.selectsubject_action, name='selectsubject_action'),
    path('studyagain/', views.studyagain, name='studyagain'),
    path('gradecheck_get/', views.gradecheck_get, name='gradecheck_get'),
    path('teacher_courseinfo/', views.teacher_courseinfo, name='teacher_courseinfo'),
    path('getteacher_course/', views.getteacher_course, name='getteacher_course'),
    path('save_studentgrade/', views.save_studentgrade, name='save_studentgrade'),
]
