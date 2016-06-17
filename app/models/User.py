from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()
        self.__query = ''
        self.__data = {}

    def run_query(self, query, data={}):
        return self.db.query_db(query, data)

    def get_all_users(self):
        self.__query = "SELECT id, email, concat(first_name, ' ', last_name) AS name, CASE user_level WHEN 9 THEN 'Admin' WHEN 1 THEN 'Normal' END AS user_level, DATE_FORMAT(created_at, '%b %D %Y') AS created_at FROM users"
        self.__data = {}
        return self.run_query(self.__query, self.__data)

    def del_user(self, id):
        self.__query = "DELETE FROM users WHERE id = :id"
        self.__data = {
            'id': id
        }
        return self.run_query(self.__query, self.__data)

    def get_id_user(self, id):
        self.__query = "SELECT id, email, first_name, last_name, user_level, description FROM users WHERE id = :id"
        self.__data = {
            'id': id
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
