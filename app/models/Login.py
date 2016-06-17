from system.core.model import Model
import re

class Login(Model):
    def __init__(self):
        super(Login, self).__init__()
        self.__query = ''
        self.__data = {}

    def run_query(self, query, data={}):
        return self.db.query_db(query, data)

    def get_user(self, email):
        self.__query = "SELECT concat(first_name, ' ', last_name) as name, password, id, user_level FROM users WHERE email = :email"
        self.__data = {
            'email': email
        }
        return self.run_query(self.__query, self.__data)

    def get_all_users(self):
        self.__query = "SELECT id, email, concat(first_name, ' ', last_name) AS name, CASE user_level WHEN 9 THEN 'Admin' WHEN 1 THEN 'Normal' END AS user_level, DATE_FORMAT(created_at, '%b %D %Y') AS created_at FROM users"
        self.__data = {}
        return self.run_query(self.__query, self.__data)

    def get_count(self):
        self.__query = "SELECT count(*) as rows FROM users"
        self.__data = {}
        return self.run_query(self.__query, self.__data)

    def do_register(self, form):
        user = {
            'fname': form['fname'],
            'lname': form['lname'],
            'email': form['email'],
            'pwd': self.bcrypt.generate_password_hash(form['password']),
            'level': 0, 'desc': ''
        }

        count = self.get_count()
        if count[0]['rows'] > 0:
            user['level'] = 1
        else:
            user['level'] = 9

        self.register_user(user)
        user_details = self.get_user(form['email'])
        return {'id': user_details[0]['id'], 'user': user_details[0]['name'], 'level': user_details[0]['user_level']}

    def register_user(self, user):
        self.__query = "INSERT INTO users (first_name, last_name, email, password, user_level, description, created_at, modified_at) VALUES(:first_name, :last_name, :email, :password, :user_level, :description, NOW(), NOW())"
        self.__data = {
            'first_name': user['fname'],
            'last_name': user['lname'],
            'email': user['email'],
            'password': user['pwd'],
            'user_level': user['level'],
            'description': user['desc']
        }
        return self.run_query(self.__query, self.__data)

    def name_validate(self, name, which_name):
        return self.__name_validate(name, which_name)

    def __name_validate(self, name, which_name):
        digit = re.compile('[0-9]')
        has_digit = digit.search(name)

        result = {
            'status': False,
            'msg': {}
        }

        if which_name == 'f':
            msg_key = 'fname'
        else:
            msg_key = 'lname'

        if len(name) <= 2:
            result['msg'][msg_key] = '** must have more than 2 chars **'
        elif has_digit:
            result['msg'][msg_key] = '** must not have numbers **'
        else:
            result['status'] = True
            result['msg'] = {}

        return result

    def remail_validate(self, email):
        email_validity = self.__email_validate(email)
        if email_validity['status']:
            user = self.get_user(email)
            if user:
                email_validity['status'] = False
                email_validity['msg']['email'] = '** mail id already exists **'

        return email_validity

    def lemail_validate(self, email):
        return self.__email_validate(email)

    def __email_validate(self, email):
        mail = re.compile(r'^[a-zA-Z0-9\._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
        is_email = mail.match(email)

        result = {
            'status': False,
            'msg': {}
        }

        if is_email:
            result['status'] = True
            result['msg'] = {}
        else:
            result['msg']['email'] = '** Invalid Email **'

        return result

    def rpwd_validate(self, pwd, c_pwd=None):
        pwd_isValid = self.__pwd_validate(pwd)
        if pwd_isValid['status']:
            return self.__match_pwd(pwd, pwd_c=c_pwd)
        else:
            return pwd_isValid

    def lpwd_validate(self, pwd):
        return self.__pwd_validate(pwd)

    def __pwd_validate(self, pwd):
        digit = re.compile('[0-9]')
        cap = re.compile('[A-Z]')
        has_digit = digit.search(pwd)
        has_cap = cap.search(pwd)

        result = {
            'status': False,
            'msg': {}
        }

        if len(pwd) < 8:
            result['msg']['pwd'] = '** must be minimum 8 chars **'
        elif not has_cap:
            result['msg']['pwd'] = '** must have atleast 1 uppecase char **'
        elif not has_digit:
            result['msg']['pwd'] = '** must have atleast 1 digit **'
        else:
            result['status'] = True
            result['msg'] = {}

        return result

    def __match_pwd(self, pwd, **pwd_args):
        result = {
            'status': True,
            'msg': {}
        }

        if 'pwd_c' in pwd_args:
            if pwd != pwd_args['pwd_c']:
                result['status'] = False
                result['msg']['cpwd'] = "** confirmation password doesn't match **"
        elif 'pwd_hsh' in pwd_args:
            if not self.bcrypt.check_password_hash(pwd_args['pwd_hsh'], pwd):
                result['status'] = False
                result['msg']['pwd'] = "** Password mismatch **"

        return result

    def login(self, form):
        isLogin = {
            'status': False,
            'msg': {}
        }

        user = self.get_user(form['email'])
        if user:
            pwd_validity = self.__match_pwd(form['password'], pwd_hsh = user[0]['password'])
            if pwd_validity['status']:
                pwd_validity['msg']['id'] = user[0]['id']
                pwd_validity['msg']['user'] = user[0]['name']
                pwd_validity['msg']['level'] = user[0]['user_level']

            return pwd_validity
        else:
            isLogin['status'] = False
            isLogin['msg']['email'] = '** email-id not found **'
            return isLogin
