#encoding=utf-8
from django.db import models

# Create your models here.

class Users(models.Model):
    customertype = models.IntegerField(default=0)
    username = models.CharField(max_length=40, primary_key=True)
    password = models.CharField(max_length=80)

    def __unicode__(self):
        return self.username


class Userinfo(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    user_username = models.CharField(max_length=40)
    user_name = models.CharField(max_length=40)
    user_sex = models.CharField(max_length=10)
    user_age = models.IntegerField()
    user_department = models.CharField(max_length=100)
    user_college = models.CharField(max_length=100)
    user_grade = models.CharField(max_length=40)
    user_class = models.CharField(max_length=40)
    user_phone = models.CharField(max_length=40)
    user_adress = models.CharField(max_length=200)


    def __unicode__(self):
        return self.user_username

class Teacherinfo(models.Model):
    teacher = models.OneToOneField(Users, on_delete=models.CASCADE)
    teacher_username = models.CharField(max_length=40)
    teacher_name = models.CharField(max_length=40)
    teacher_sex = models.CharField(max_length=10)
    teacher_age = models.IntegerField()
    teacher_phone = models.CharField(max_length=40)
    teacher_adress = models.CharField(max_length=200)
    teacher_professional = models.CharField(max_length=500)
    teacher_faculty = models.CharField(max_length=100)
    teacher_profession = models.CharField(max_length=100)

    def __unicode__(self):
        return self.teacher_username


class Courseinfo(models.Model):
    course_name = models.CharField(max_length=40)
    course_code = models.CharField(max_length=40, primary_key=True)
    course_number = models.CharField(max_length=40)
    course_attribute = models.CharField(max_length=40)

    def __unicode__(self):
        return self.course_name

class TeacherCourse(models.Model):
    course_code = models.CharField(max_length=40)
    course_teacher_username = models.CharField(max_length=40)
    course_examtype = models.CharField(max_length=40)
    # course_classplace = models.CharField(max_length=400)
    course_classtime = models.CharField(max_length=800)
    course_classweek = models.CharField(max_length=100)
    course_to_department = models.CharField(max_length=100)
    course_to_college = models.CharField(max_length=100)
    term = models.CharField(max_length=10)
    tag = models.IntegerField(default=0)


class StudentCourse(models.Model):
    course_code = models.CharField(max_length=40)
    student_username = models.CharField(max_length=40)
    teacher_username = models.CharField(max_length=40)
    course_grade = models.FloatField(default=0)
    exam_num = models.IntegerField(default=1)
    term_now = models.CharField(max_length=10)
    tag = models.IntegerField(default=0)
    ispass = models.IntegerField(default=0)

class Department_College(models.Model):
    departmentnumber = models.CharField(max_length=40, primary_key=True)
    collegename = models.CharField(max_length=100, default='')
    departmentname = models.CharField(max_length=100, default='')

class Classtime(models.Model):
    num = models.CharField(max_length=40, primary_key=True)
    weekday = models.CharField(max_length=20)
    classnum = models.CharField(max_length=20)

class Classroom(models.Model):
    classroomnum = models.CharField(max_length=20, primary_key=True)
    classroomname = models.CharField(max_length=200)

class Params(models.Model):
    param = models.CharField(max_length=20, primary_key=True)
    term_now = models.CharField(max_length=10)
    tag = models.IntegerField(default=0)
