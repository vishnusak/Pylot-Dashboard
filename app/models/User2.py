from Login import Login

class User2(Login):
    def __init__(self):
        super(User2, self).__init__()
        self.__query = ''
        self.__data = {}

    def del_user(self, id):
        self.__data = {
        'id': id
        }
        self.__query = "DELETE FROM comments WHERE user_id = :id or for_id = :id"
        self.run_query(self.__query, self.__data)
        self.__query = "DELETE FROM messages WHERE user_id = :id or for_id = :id"
        self.run_query(self.__query, self.__data)
        self.__query = "DELETE FROM users WHERE id = :id"
        return self.run_query(self.__query, self.__data)

    def get_id_user(self, id):
        self.__query = "SELECT id, email, first_name, last_name, user_level, description FROM users WHERE id = :id"
        self.__data = {
            'id': id
        }
        return self.run_query(self.__query, self.__data)

    def update_detail(self, id, form):
        if 'level' in form:
            self.__query = "UPDATE users SET email = :email, first_name = :first_name, last_name = :last_name, user_level = :user_level, modified_at = NOW() WHERE id = :id"
            self.__data = {
                'id': id,
                'email': form['email'],
                'first_name': form['fname'],
                'last_name': form['lname'],
                'user_level': form['level']
            }
        else:
            self.__query = "UPDATE users SET email = :email, first_name = :first_name, last_name = :last_name, modified_at = NOW() WHERE id = :id"
            self.__data = {
                'id': id,
                'email': form['email'],
                'first_name': form['fname'],
                'last_name': form['lname']
            }
        return self.run_query(self.__query, self.__data)

    def update_pwd(self, id, form):
        self.__query = "UPDATE users SET password = :password, modified_at = NOW() WHERE id = :id"
        self.__data = {
            'id': id,
            'password': self.bcrypt.generate_password_hash(form['password'])
        }
        return self.run_query(self.__query, self.__data)

    def update_desc(self, id, form):
        self.__query = "UPDATE users SET description = :description, modified_at = NOW() WHERE id = :id"
        self.__data = {
            'id': id,
            'description': form['desc']
        }
        return self.run_query(self.__query, self.__data)
