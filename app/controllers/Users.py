from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User2')
        self.__db = self.models['User2']

    def new(self):
        session['page'] = ''
        return self.load_view('register.html')

    def remove(self, id=None):
        if session['user_level'] == 9:
            if not session['popup']:
                session['popup'] = True
                session['popup-id'] = id
            elif session['popup']:
                session['popup'] = False
                session['popup-id'] = None
                if id:
                    self.__db.del_user(id)
                    session['all_users'] = self.__db.get_all_users()
        return redirect('/dashboard')

    def remove_yes(self, id):
        return self.remove(id)

    def remove_no(self):
        return self.remove()

    def retrieve_user(self, id):
        user = self.__db.get_id_user(id)[0]

        session['edit_user']['id'] = user['id']
        session['edit_user']['email'] = user['email']
        session['edit_user']['fname'] = user['first_name']
        session['edit_user']['lname'] = user['last_name']
        session['edit_user']['level'] = user['user_level']
        session['edit_user']['desc'] = user['description']

    def edit(self, id):
        session['page'] = 'edit'
        self.retrieve_user(id)
        return self.load_view('edit.html')

    def profile(self, id):
        session['page'] = 'profile'
        self.retrieve_user(id)
        return self.load_view('edit.html')

    def upd_dtl(self, id):
        user_fname = request.form['fname'] if request.form['fname'] else ''
        user_lname = request.form['lname'] if request.form['lname'] else ''
        user_email = request.form['email'] if request.form['email'] else ''

        fname_isValid = self.__db.name_validate(user_fname, 'f')
        lname_isValid = self.__db.name_validate(user_lname, 'l')
        email_isValid = self.__db.remail_validate(user_email)

        session['err'] = {}

        if not fname_isValid['status']:
            session['err'].update(fname_isValid['msg'])
        else:
            session['edit_user']['fname'] = user_fname

        if not lname_isValid['status']:
            session['err'].update(lname_isValid['msg'])
        else:
            session['edit_user']['lname'] = user_lname

        if not email_isValid['status']:
            session['err'].update(email_isValid['msg'])
        else:
            session['edit_user']['email'] = user_email

        if not session['err']:
            session['edit_user'] = {}
            self.__db.update_detail(id, request.form)
            session['all_users'] = self.__db.get_all_users()
            if session['page'] == 'edit':
                return self.edit(id)
            elif session['page'] == 'profile':
                return self.profile(id)
        else:
            return self.load_view('edit.html')

    def upd_pwd(self, id):
        user_password = request.form['password'] if request.form['password'] else ''
        user_c_password = request.form['c_password'] if request.form['c_password'] else ''

        pwd_isValid = self.__db.rpwd_validate(user_password, user_c_password)

        session['err'] = {}

        if not pwd_isValid['status']:
            session['err'].update(pwd_isValid['msg'])

        if not session['err']:
            session['edit_user'] = {}
            self.__db.update_pwd(id, request.form)
            if session['page'] == 'edit':
                return self.edit(id)
            elif session['page'] == 'profile':
                return self.profile(id)
        else:
            return self.load_view('edit.html')

    def upd_desc(self, id):
        if request.form['desc']:
            self.__db.update_desc(id, request.form)
            session['all_users'] = self.__db.get_all_users()
        return self.profile(id)
