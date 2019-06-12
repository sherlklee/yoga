from django.db import models

# Create your models here.
#登录账号和id
class Customer(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    identity = models.CharField(default="customer", max_length=12)  #表示用户的身份 管理员为admin教练为trainer

    def checkpassword(self , uncheckpassword):
        if self.password == uncheckpassword:
            return True
        else:
            return False

    def Getidentity(self):
        return self.identity

    def Isadmin(self):
        if self.identity == "admin":
            return True
        else:
            return False

    def Istrainer(self):
        if self.identity == "trainer":
            return True
        else:
            return False

    def Iscustomer(self):
        if self.identity == "customer":
            return True
        else:
            return False

#用户的个人信息
class Customerinformation(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    sex = models.BooleanField(default=True)#ture表示为女，false表示男
    name = models.CharField(max_length=12)
    phone = models.CharField(max_length=11)
    birthday = models.DateField(default='1990-01-01')
    profession = models.CharField(max_length=20, default=" ")
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    bust = models.FloatField(default=0)
    waistline = models.FloatField(default=0)
    hipline = models.FloatField(default=0)
    shoulderwidth = models.FloatField(default=0)

    def Setphone(self, p):
        self.phone = p
        self.save()

    def Getphone(self):
        return self.phone

    def Setname(self, p):
        self.name = p
        self.save()

    def Getname(self):
        return self.name

    def Setage(self, p):
        self.age = p
        self.save()

    def Getage(self):
        return self.age

    def Setbirthday(self, p):
        self.birthday = p
        self.save()

    def Getbirthday(self):
        return self.birthday

    def Setprofession(self, p):
        self.profession = p
        self.save()

    def Getprofession(self):
        return self.profession

    def Setsex(self, p):
        self.sex = p
        self.save()

    def Getsex(self):
        return self.sex

    def Setheight(self, p):
        self.height = p
        self.save()

    def Getheight(self):
        return self.height

    def Setweight(self, p):
        self.weight = p
        self.save()

    def Getweight(self):
        return self.weight

    def Setbust(self, p):
        self.bust = p
        self.save()

    def Getbust(self):
        return self.bust

    def Setwaistline(self, p):
        self.waistline = p
        self.save()

    def Getwaistline(self):
        return self.waistline

    def Sethipline(self, p):
        self.hipline = p
        self.save()

    def Gethipline(self):
        return self.hipline

    def Setshoulderwidth(self, p):
        self.shoulderwidth = p
        self.save()

    def Getshoulderwidth(self):
        return self.shoulderwidth

#教练的个人简介
class Trainerinformation(models.Model):
    username = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    sex = models.BooleanField(default=True) #ture表示女 false表示男
    professionaltitle= models.CharField(max_length=30)
    introduction = models.CharField(max_length=100)
    photo = models.CharField(max_length=25)
    phone = models.CharField(max_length=11)

    def Setname(self, p):
        self.name = p
        self.save()

    def Getname(self):
        return self.name

    def Setage(self, p):
        self.age = p
        self.save()

    def Getage(self):
        return self.age

    def Setsex(self, p):
        self.sex = p
        self.save()
    def Setphone(self,p):
        self.phone = p
        self.save()

    def Getphone(self):
        return self.phone

    def Getsex(self):
        return self.sex

    def Setprofessionaltitle(self, p):
        self.professionaltitle = p
        self.save()

    def Getprofessionaltitle(self):
        return self.professionaltitle

    def Setintroduction(self, p):
        self.introduction = p
        self.save()

    def Getintroduction(self):
        return self.intruduction

    def Setphoto(self, p):
        self.photo = p
        self.save()

    def Getphoto(self):
        return self.photo

#课程
class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=20, unique=True)
    trainer = models.CharField(max_length=20)
    courseprice = models.FloatField(default=0.0)
    coursevalid = models.BooleanField(default=True)#表示该课程是否有效
    introduction = models.CharField(max_length=100)

    def Course(self, coursename, trainer, courseprice, introdution):
        self.coursename = coursename
        self.trainer = trainer
        self.courseprice = courseprice
        self.introdution = introdution
        self.save()

    def Getcourseid(self):
        return self.courseid

    def Setcoursename(self,p):
        self.coursename = p
        self.save()

    def Getcoursename(self):
        return self.coursename

    def Settrainer(self, p):
        self.trainer = p
        self.save()

    def Gettrainer(self):
        return self.trainer

    def Setcourseprice(self, p):
        self.courseprice = p
        self.save()

    def Getcourseprice(self):
        return self.courseprice

    def Setcoursevalid(self,p):
        self.coursevalid = p
        self.save()

    def Getcoursevalid(self):
        return self.coursevalid

    def Setintrodution(self,p):
        self.introdution = p
        self.save()

    def Getintrodution(self):
        return self.introdution

#订单
class BuyRecord(models.Model):
    number = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    coursename = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)      #表示课程的数量
    time = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)         #表示订单的总金额
    pay_flag = models.BooleanField(default=False)  # 标记是否付钱的订单
    valid = models.BooleanField(default=True)  # 标记是否为取消的订单

    def Getnumber(self):
        return self.number

    def Setnumber(self, p):
        self.number = p
        self.save()

    def Getusername(self):
        return self.username

    def Setusername(self, p):
        self.username = p
        self.save()

    def Getcoursename(self):
        return self.coursename

    def Setcoursename(self, p):
        self.coursename = p
        self.save()

    def Getamount(self):
        return self.amount

    def Setamount(self, p):
        self.amount = p
        self.save()

    def Getprice(self):
        return self.price

    def Setprice(self, p):
        self.price = p
        self.save()

    def Gettime(self):
        return self.time

    def Settime(self, p):
        self.time = p
        self.save()

    def Getpayflag(self):
        return self.pay_flag

    def Setpayflag(self, p):
        self.pay_flag = p
        self.save()

    def Getvalid(self):
        return self.valid

    def Setvalid(self, p):
        self.valid = p
        self.save()

#教室
class Classroom(models.Model):
    classroomid = models.AutoField(primary_key=True)
    classroomname = models.CharField(max_length=20,unique=True)
    note = models.CharField(max_length=50)
    maxpersonnumber = models.IntegerField(default=0)

    def Setclassroomname(self,p):
        self.classroomname = p
        self.save()

    def Getclassroomname(self):
        return self.classroomname

    def Setnote(self,p):
        self.note = p
        self.save()

    def Getnote(self):
        return self.note

    def Setmaxpersonnumber(self,p):
        self.maxpersonnumber = p
        self.save()

    def Getmaxpersonnumber(self):
        return self.maxpersonnumber

#教室的安排
class classroomorder(models.Model):
    orderid = models.AutoField(primary_key=True)
    classroomid = models.IntegerField(default=0)
    username = models.CharField(max_length=20)
    coursename = models.CharField(max_length=20)
    date = models.DateField(default="2019-6-11")
    dateclassnumber = models.IntegerField(default=0)   #表示一天中第几节课程

    def Setclassroomid(self,p):
        self.classroomid = p
        self.save()

    def Getclassroomid(self):
        return self.classroomid

    def Setusername(self,p):
        self.username = p
        self.save()

    def Getusername(self):
        return self.username

    def Setdate(self,p):
        self.date = p
        self.save()

    def Getdate(self):
        return self.date


#用户预约记录
class customercourseorder(models.Model):
    orderid = models.AutoField(primary_key=True)
    classid =models.IntegerField(default=0)

    def Setclassid(self,p):
        self.classid = p
        self.save()

    def Getclassid(self):
        return self.classid


