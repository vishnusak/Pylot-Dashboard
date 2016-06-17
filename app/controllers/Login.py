from system.core.controller import *

class Login(Controller):
    def __init__(self, action):
        super(Login, self).__init__(action)
        self.load_model('Login')
        self.__db = self.models['Login']

    def login(self):
        user_email = request.form['email'] if request.form['email'] else ''
        user_password = request.form['password'] if request.form['password'] else ''
        #
        email_isValid = self.__db.lemail_validate(user_email)
        pwd_isValid = self.__db.lpwd_validate(user_password)
        loggedin_user = self.__db.login(request.form)

        session['err'] = {}
        session['form'] = {}

        if not email_isValid['status']:
            session['err'].update(email_isValid['msg'])
        else:
            session['form']['email'] = user_email

        if not pwd_isValid['status']:
            session['err'].update(pwd_isValid['msg'])

        if not loggedin_user['status']:
            session['err'].update(loggedin_user['msg'])

        if not session['err']:
            session['form'] = {}
            session['user-id'] = loggedin_user['msg']['id']
            session['user'] = loggedin_user['msg']['user']
            session['user_level'] = loggedin_user['msg']['level']
            session['all_users'] = self.__db.get_all_users()
            return redirect('/dashboard')
        else:
            return self.load_view('login.html')

    def register(self):
        user_fname = request.form['fname'] if request.form['fname'] else ''
        user_lname = request.form['lname'] if request.form['lname'] else ''
        user_email = request.form['email'] if request.form['email'] else ''
        user_password = request.form['password'] if request.form['password'] else ''
        user_c_password = request.form['c_password'] if request.form['c_password'] else ''

        fname_isValid = self.__db.name_validate(user_fname, 'f')
        lname_isValid = self.__db.name_validate(user_lname, 'l')
        email_isValid = self.__db.remail_validate(user_email)
        pwd_isValid = self.__db.rpwd_validate(user_password, user_c_password)

        session['err'] = {}
        session['form'] = {}

        if not fname_isValid['status']:
            session['err'].update(fname_isValid['msg'])
        else:
            session['form']['fname'] = user_fname

        if not lname_isValid['status']:
            session['err'].update(lname_isValid['msg'])
        else:
            session['form']['lname'] = user_lname

        if not email_isValid['status']:
            session['err'].update(email_isValid['msg'])
        else:
            session['form']['email'] = user_email

        if not pwd_isValid['status']:
            session['err'].update(pwd_isValid['msg'])

        if not session['err']:
            session['form'] = {}
            registered_user = self.__db.do_register(request.form)

            if session['page'] == 'register':
                session['user-id'] = registered_user['id']
                session['user'] = registered_user['user']
                session['user_level'] = registered_user['level']

            session['all_users'] = self.__db.get_all_users()
            return redirect('/dashboard')
        else:
            return self.load_view('register.html')
