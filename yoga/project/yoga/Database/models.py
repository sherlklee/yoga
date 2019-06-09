from django.db import models

# Create your models here.
#登录账号和id
class Customer(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    identity = models.CharField(default="customer",max_length=12)  #表示用户的身份 管理员为admin教练为trainer

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

class Customerinformation(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    sex = models.BooleanField(default=True)#ture表示为女，false表示男
    name = models.CharField(max_length=12)
    phone = models.CharField(max_length=11)
    birthday = models.DateField(default='1990/01/01')
    profession = models.CharField(max_length=20)
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

    def setage(self, p):
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

    def Detweight(self, p):
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

class Trainerinformation(models.Model):
    username = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    sex = models.BooleanField(default=True) #ture表示女 false表示男
    professionaltitle= models.CharField(max_length=30)
    introdution = models.CharField(max_length=100)
    photo = models.CharField(max_length=25)

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

    def Getsex(self):
        return self.sex

    def Setprofessionaltitle(self, p):
        self.professionaltitle = p
        self.save()

    def Getprofessionaltitle(self):
        return self.professionaltitle

    def Setintrodution(self, p):
        self.intrudution = p
        self.save()

    def Getintrodution(self):
        return self.intrudution

    def Setphoto(self, p):
        self.photo = p
        self.save()

    def Getphoto(self):
        return self.photo

class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=20)
    trainer = models.CharField(max_length=20)
    courseprice = models.FloatField(default=0)
    coursevalid = models.BooleanField(default=True)#表示该课程是否有效
    introdution = models.CharField(max_length=100)

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




