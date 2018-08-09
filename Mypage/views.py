#encoding=utf-8
from django.shortcuts import render

from django.http import HttpResponse
from .models import Users , Userinfo, Courseinfo, Teacherinfo, TeacherCourse, StudentCourse, Department_College, Classtime, \
    Classroom, Params
from django.shortcuts import redirect
import json
from urllib.parse import unquote

# Create your views here.

def homepage(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return render(request, 'login.html')
    user = Users.objects.get(username = cook)
    if user.customertype == 0:
        return render(request, 'homepage.html')
    elif user.customertype == 1:
        return render(request, 'homepage_t.html')

def selectsubject(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return render(request, 'login.html')
    return render(request, 'selectsubject.html')

def modifypwd(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return render(request, 'login.html')
    return render(request, 'modifypwd.html')

def do_modifypwd(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return render(request, 'login.html')
    username = request.session.get('username')
    old_password = request.GET.get('old_password')
    new_password = request.GET.get('new_password')
    try:
        account = Users.objects.get(username=username)
    except:
        return HttpResponse('用户名密码不存在。')
    if account.password != old_password:
        return HttpResponse('原密码输入错误。')
    elif old_password == new_password:
        return HttpResponse('原密码和新密码不能相同。')
    else:
        Users.objects.filter(username=username).update(password=new_password)  # update可多条
        return HttpResponse('密码修改成功!')



def studentinfo(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return render(request, 'login.html')
    user = Users.objects.get(username = cook)
    if user.customertype == 0:
        userinfo = Userinfo.objects.get(user_username=cook)  # update可多条
        dep = Department_College.objects.get(departmentnumber=userinfo.user_department)
        userinfo.user_department = dep.departmentname
        userinfo.user_college = dep.collegename
        return render(request, 'studentinfo.html', {'userinfo':userinfo})
    elif user.customertype == 1:
        userinfo = Teacherinfo.objects.get(teacher_username=cook)
        dep = Department_College.objects.get(departmentnumber=userinfo.teacher_faculty)
        userinfo.teacher_faculty = dep.departmentname + dep.collegename
        return render(request, 'teacherinfo.html', {'userinfo':userinfo})

def studentinfo_update(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return  render(request, 'login.html')
    user = Users.objects.get(username = cook)
    if user.customertype == 0:
        userinfo = Userinfo.objects.get(user_username=cook)  # update可多条
        dep = Department_College.objects.get(departmentnumber=userinfo.user_department)
        userinfo.user_department = dep.departmentname
        userinfo.user_college = dep.collegename
        return render(request, 'studentinfo_update.html', {'userinfo':userinfo})
    elif user.customertype == 1:
        userinfo = Teacherinfo.objects.get(teacher_username=cook)
        dep = Department_College.objects.get(departmentnumber=userinfo.teacher_faculty)
        userinfo.teacher_faculty = dep.departmentname + dep.collegename
        return render(request, 'teacherinfo_update.html', {'userinfo':userinfo})

def studentinfo_update_save(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return  render(request, 'login.html')
    try:
        username = request.GET.get('username')
        phone = request.GET.get('phone')
        adress = request.GET.get('adress')
        print(username, phone, adress)
        user = Users.objects.get(username=cook)
        if user.customertype == 0:
            Userinfo.objects.filter(user_username=username).update(user_phone=phone, user_adress=adress)  # update可多条
        elif user.customertype == 1:
            Teacherinfo.objects.filter(teacher_username = username).update(teacher_phone=phone, teacher_adress=adress)
        return HttpResponse('修改成功!')
    except:
        return HttpResponse('修改数据异常!')


def classschedule(request):
    cook = request.COOKIES.get('username')
    if cook == None:
        return  render(request, 'login.html')
    print('cook:', cook)
    user = Users.objects.get(username=cook)
    if user.customertype == 0:
        return render(request, 'classschedule.html')
    elif user.customertype == 1:
        return render(request, 'teacher_classschedule.html')

def get_classschedule(request):
    def get_time_place(data):
        time = []
        place = []
        res1 = data.split(';')
        for res2 in res1:
            res3 = res2.split('|')
            res4 = res3[0].split(',')
            tag = 0
            for t in res4:
                time.append(t)

            place.append(res3[1])
        return time, place

    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return  render(request, 'login.html')
    one = {}
    two = {}
    three = {}
    four = {}
    five = {}
    six = {}
    seven = {}
    eight = {}
    nine = {}
    ten = {}
    eleven = {}

    param = Params.objects.get(param='term')
    user = Users.objects.get(username=cook)
    if user.customertype == 0:
        studentcourses = StudentCourse.objects.filter(student_username = cook,term_now=param.term_now, tag=param.tag)
    elif user.customertype == 1:
        studentcourses = TeacherCourse.objects.filter(course_teacher_username = cook,
                                                   term=param.term_now, tag=param.tag)
    for studentcourse in studentcourses:
        if user.customertype == 0:
            course = TeacherCourse.objects.get(course_teacher_username = studentcourse.teacher_username,
                                           course_code = studentcourse.course_code, term=param.term_now, tag=param.tag)
        elif user.customertype == 1:
            course = studentcourse
        times, places= get_time_place(course.course_classtime)
        courseinfo = Courseinfo.objects.get(course_code = course.course_code)
        for time in times:
            classtime = Classtime.objects.get(num=time)
            place = Classroom.objects.get(classroomnum = places[0])
            am = {}

            if classtime.weekday == '周一':
                am['Mon'] = courseinfo.course_name+'('+ place.classroomname +')'
            elif classtime.weekday == '周二':
                am['Tues'] = courseinfo.course_name+'('+ place.classroomname +')'
            elif classtime.weekday == '周三':
                am['Wed'] = courseinfo.course_name+'('+ place.classroomname +')'
            elif classtime.weekday == '周四':
                am['Thur'] = courseinfo.course_name+'('+ place.classroomname +')'
            elif classtime.weekday == '周五':
                am['Fri'] = courseinfo.course_name+'('+ place.classroomname +')'
            elif classtime.weekday == '周六':
                am['Satu'] = courseinfo.course_name+'('+ place.classroomname +')'
            elif classtime.weekday == '周日':
                am['Sun'] = courseinfo.course_name+'('+ place.classroomname +')'

            if classtime.classnum == '第一节课':
                one.update(am)
            elif classtime.classnum == '第二节课':
                two.update(am)
            elif classtime.classnum == '第三节课':
                three.update(am)
            elif classtime.classnum == '第四节课':
                four.update(am)
            elif classtime.classnum == '第五节课':
                five.update(am)
            elif classtime.classnum == '第六节课':
                six.update(am)
            elif classtime.classnum == '第七节课':
                seven.update(am)
            elif classtime.classnum == '第八节课':
                eight.update(am)
            elif classtime.classnum == '第九节课':
                nine.update(am)
            elif classtime.classnum == '第十节课':
                ten.update(am)
            elif classtime.classnum == '第十一节课':
                eleven.update(am)

    schedule1 = []
    schedule1.append(one)
    schedule1.append(two)
    schedule1.append(three)
    schedule1.append(four)
    schedule1.append(five)
    schedule1.append(six)
    schedule1.append(seven)
    schedule1.append(eight)
    schedule1.append(nine)
    schedule1.append(ten)
    schedule1.append(eleven)
    schedule = {}
    schedule['rows'] = schedule1
    schedule = json.dumps(schedule)
    return HttpResponse(schedule, content_type='application/json')


def selsubnotice(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    return render(request, 'selsubnotice.html')

def selsubhelp(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return  render(request, 'login.html')
    return render(request, 'selsubhelp.html')

def gradecheck(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return  render(request, 'login.html')
    param = Params.objects.get(param = 'term')
    userinfo = Userinfo.objects.get(user_username = cook)
    yearnum = int(param.term_now) - int(userinfo.user_grade)
    term = []
    for i in range(yearnum+1):
        if i == 0:
            term.append(str(int(userinfo.user_grade) + i) + '年~'+ str(int(userinfo.user_grade) + i + 1) +'第一学期')
        else:
            if i == yearnum:
                if param.tag == 0:
                    term.append(str(int(userinfo.user_grade) + i - 1) + '年~'+ str(int(userinfo.user_grade)+i) + '第二学期')
                else:
                    term.append(str(int(userinfo.user_grade) + i - 1) + '年~'+ str(int(userinfo.user_grade)+i) + '第二学期')
                    term.append(str(int(userinfo.user_grade) + i) + '年~'+ str(int(userinfo.user_grade) + i + 1) +'第一学期')
            else:
                term.append(str(int(userinfo.user_grade) + i - 1) + '年~'+ str(int(userinfo.user_grade)+i) + '第二学期')
                term.append(str(int(userinfo.user_grade) + i) + '年~'+ str(int(userinfo.user_grade) + i + 1) +'第一学期')
    num = len(term)
    return render(request, 'gradecheck.html', {'term': json.dumps(term)})


def login(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    return render(request, 'login.html')

def login_check(request):
    try:
        regResponse = {"errorCode": 0, "errorsList": ''}
        username = request.GET.get('username')
        password = request.GET.get('password')
        if (username == '') or (password == ''):
            regResponse['errorCode'] = 1
            regResponse['errorsList'] = '用户名或密码不能为空。'
            return HttpResponse(json.dumps(regResponse))
        try:
            account = Users.objects.get(username=username)
            # account = ue.objects.all()
        except:
            regResponse['errorCode'] = 1
            regResponse['errorsList'] = '用户名密码不存在。'
            return HttpResponse(json.dumps(regResponse))
        if account == None:
            regResponse['errorCode'] = 1
            regResponse['errorsList'] = '用户名不存在。'
            return HttpResponse(json.dumps(regResponse))
        elif password != account.password:
            regResponse['errorCode'] = 1
            regResponse['errorsList'] = '密码错误。'
            return HttpResponse(json.dumps(regResponse))
        elif (account.customertype ==0) or (account.customertype ==1):
            response = HttpResponse(json.dumps(regResponse))
            response.set_cookie("username", username)
            request.session['is_login'] = 'true'
            request.session['username'] = username
            return response

    except:
        return HttpResponse('登录异常。')


def getcourse(request):
    def get_time_place(data):
        res = ''
        res1 = data.split(';')
        for res2 in res1:
            res3 = res2.split('|')
            res4 = res3[0].split(',')
            tag = 0
            for t in res4:
                cla = Classtime.objects.get(num=str(t))
                if tag == 0:
                    res = res + cla.weekday + cla.classnum
                    tag+=1
                else:
                    res = res + cla.classnum

            classroom = Classroom.objects.get(classroomnum=res3[1])
            res = res + '(' + classroom.classroomname + ')；'

        return res

    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return  render(request, 'login.html')

    cou = []
    account = Userinfo.objects.get(user_username=cook)
    department = account.user_department
    college = account.user_college
    print(department, '  ', college)

    teachercourses = TeacherCourse.objects.filter(course_to_department=department, course_to_college=college)
    for teachercourse in teachercourses:
        course = Courseinfo.objects.get(course_code=teachercourse.course_code)
        teacher = Teacherinfo.objects.get(teacher_username=teachercourse.course_teacher_username)
        isCheck = StudentCourse.objects.filter(course_code = course.course_code, student_username=cook,
                               teacher_username = teacher.teacher_username)


        if isCheck:
            check = '删除'
        else:
            check = '选择'
        cou.append({
            'name': course.course_name,
            'nameid': course.course_code,
            'namexh': course.course_number,
            'teacher': teacher.teacher_name,
            'teacher_username': teacher.teacher_username,
            'namelex': course.course_attribute,
            'gradelex': teachercourse.course_examtype,
            'place': get_time_place(teachercourse.course_classtime),
            'week': teachercourse.course_classweek,
            'select': check,
        })
    return HttpResponse(json.dumps(cou), content_type="application/json")

def selectsubject_action(request):
    try:
        cook = request.COOKIES.get('username')
        print('cook:', cook)
        if cook == None:
            return render(request, 'login.html')
        data = request.POST.get('data')
        action = request.POST.get('action')
        data = unquote(data)
        data = json.loads(data)
        teacher_username = data['teacher_username']
        course_code = data['nameid']
        student_username = cook
        param = Params.objects.get(param = 'term')
        if action == 'select':
            isCheck = StudentCourse.objects.filter(course_code=course_code, exam_num = 1, term_now = param.term_now, tag = param.tag)
            if isCheck:
                return HttpResponse(json.dumps({'rescode': '0', 'res': '已选择该门课程，请选择其他课程。'}))
            StudentCourse.objects.create(course_code=course_code, student_username=student_username,
                                            teacher_username=teacher_username, term_now = param.term_now, tag = param.tag)
            return  HttpResponse(json.dumps({'rescode': '1', 'res': '选课成功。'}))
        else:
            StudentCourse.objects.filter(course_code=course_code, student_username=student_username,
                                         teacher_username=teacher_username, exam_num = 1, term_now = param.term_now, tag = param.tag).delete()
            return HttpResponse(json.dumps({'rescode': '1', 'res': '删除成功。'}))
    except:
        return HttpResponse(json.dumps({'rescode': '1', 'res': '操作异常，请重新选择。'}))



def gradecheck_get(request):
    text = request.GET.get('text')
    year = text[:4]
    if '一' in text:
        tag = 1
    else:
        year = str(int(year) + 1)
        tag = 0
    studentcourse = StudentCourse.objects.filter(term_now = year, tag = tag)
    if studentcourse == None:
        return HttpResponse('未查询到数据。')
    else:
        cou = []
        for i in studentcourse:
            course = Courseinfo.objects.get(course_code = i.course_code)
            if i.ispass == 0:
                res = '尚未评定'
            elif i.ispass == 1:
                res = '通过'
            else:
                res = '未通过'
            cou.append({
                'name': course.course_name,
                'grade': i.course_grade,
                'pass': res,
            })
    return HttpResponse(json.dumps(cou), content_type="application/json")


def studyagain(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return  render(request, 'login.html')
    return render(request, 'studyagain.html')



def teacher_courseinfo(request):
    cook = request.COOKIES.get('username')
    print('cook:', cook)
    if cook == None:
        return  render(request, 'login.html')
    param = Params.objects.get(param = 'term')
    teachercourses = TeacherCourse.objects.filter(course_teacher_username = cook,term = param.term_now, tag=param.tag)
    course = []
    stu = []
    for teachercourse in teachercourses:
        cou = Courseinfo.objects.get(course_code=teachercourse.course_code)
        course.append({
            'code': cou.course_code,
            'name': cou.course_name,
        })

    return render(request, 'teacher_courseinfo.html', {'course': json.dumps(course)})

def getteacher_course(request):
    code = request.GET.get('code')
    text = request.GET.get('text')
    param = Params.objects.get(param='term')
    stus = StudentCourse.objects.filter(course_code=code,term_now = param.term_now, tag=param.tag)
    student = []
    for stu in stus:
        stuinfo = Userinfo.objects.get(user_username = stu.student_username)
        if stu.course_grade == 0:
            grade = ''
        else:
            grade = stu.course_grade
        if stu.ispass == 0:
            ispass = ''
        elif stu.ispass == 1:
            ispass = '通过'
        else:
            ispass = '未通过'
        student.append({
            'id': stuinfo.user_username,
            'name': stuinfo.user_name,
            'coursename': text,
            'grade': grade,
            'pass':ispass,
            'edit': '编辑',
        })
    return HttpResponse(json.dumps(student), content_type='application/json')


def save_studentgrade(request):
    xh = request.GET.get('xh')
    courseid = request.GET.get('courseid')
    grade = request.GET.get('grade')
    if grade == '':
        grade = 0
    else:
        grade = float(grade)
    ispass = int(request.GET.get('ispass', 0))
    try:
        param = Params.objects.get(param = 'term')
        StudentCourse.objects.filter(student_username=xh, course_code=courseid,
                                     term_now = param.term_now, tag=param.tag).update(course_grade=grade, ispass=ispass)
        return HttpResponse('保存成功。')
    except:
        return HttpResponse('保存失败，请重新录入。')






