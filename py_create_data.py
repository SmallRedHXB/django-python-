#!/usr/bin/env python
#encoding=utf-8
# -*- coding: utf-8 -*-
# @Date    : 2015-07-28 20:38:38
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com

'''
create some records for demo database
'''

from .Mypage.models import Users, Userinfo, Teacherinfo


def main():
    try:
        account = Users.objects.get(username='201800000')
        create = Userinfo.objects.create(user=account, user_username='201800000',
                                         user_name = '胡雄斌',
                                         user_sex = '男',
                                         user_age = '26',
                                         user_grade = '2015级',
                                         user_class = '计算机一班',
                                         user_phone = '18067938112',
                                         user_adress = '杭州市滨江区临江花园',
                                        )


    except:
        pass


    try:
        account = Users.objects.get(username='000000001')
        create = Teacherinfo.objects.create(teacher=account, teacher_username='000000001',
                                            teacher_name = '老有才',
                                            teacher_sex = '男',
                                            teacher_age = '46',
                                            teacher_phone = '18028269431',
                                            teacher_adress = '厦门市鼓浪屿256号',
                                            teacher_professional = '教授',
                                            teacher_faculty = '信息科学与技术学院计算机系',
                                            teacher_profession='计算机数学',
                                        )


    except:
        pass


if __name__ == '__main__':
    main()
    print("Done!")