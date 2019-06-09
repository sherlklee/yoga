from Database.models import Customer
SESSION_LOGINSTATUS_ONLINE = 'Online'
SESSION_LOGINSTATUS_OFFLINE = 'Offline'
class SessionManager:
    session = None

    def __init__(self, request=None):
        if request is not None:
            self.session = request.session

    def Setusername(self, username):
        self.session['Username'] = username
        self.session.save()

    def SetloginStatus(self, loginStatus):
        self.session['LoginStatus'] = loginStatus
        self.session.save()

    def Setlogin(self, username):
        user= Customer.objects.get(username=username)
        self.Setusername(username)
        self.SetloginStatus(SESSION_LOGINSTATUS_ONLINE)

    def Islogined(self):
        if self.session.get('LoginStatus', default=SESSION_LOGINSTATUS_OFFLINE) == SESSION_LOGINSTATUS_ONLINE:
            return True
        else:
            return False

    def Setlogout(self):
        self.SetloginStatus(SESSION_LOGINSTATUS_OFFLINE)
        del self.session['Username']

    def Islogouted(self):
        if self.session.get('LoginStatus', default=SESSION_LOGINSTATUS_OFFLINE) == SESSION_LOGINSTATUS_OFFLINE:
            return True
        else:
            return False

    def Isadministrator(self):
        username=self.session.get("Username",default=None)
        if username is not None:
            user=Customer.objects.get(username=username)
            return user.Isadministrator()
        return False

    def Getusername(self):
        return self.session.get('Username', default=None)
