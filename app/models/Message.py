from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()
        self.__query = ''
        self.__data = {}

    def run_query(self, query, data={}):
        return self.db.query_db(query, data)

    def get_id_user(self, id):
        self.__query = "SELECT id, email, concat(first_name, ' ', last_name) as name, user_level, description, DATE_FORMAT(created_at, '%M %D %Y') AS created_at FROM users WHERE id = :id"
        self.__data = {
            'id': id
        }
        return self.run_query(self.__query, self.__data)

    def get_messages(self, id):
        self.__query = "SELECT m.id, concat(u.first_name, ' ', u.last_name) AS name, m.msg_text, DATE_FORMAT(m.created_at, '%b %D %Y') AS created_at FROM messages m, users u WHERE m.for_id = :for_id AND m.user_id = u.id ORDER BY m.created_at DESC"
        self.__data = {
            'for_id': id
        }
        return self.run_query(self.__query, self.__data)

    def insert_message(self, id, form, user_id):
        self.__query = "INSERT INTO messages (user_id, for_id, msg_text, created_at, modified_at) VALUES (:user_id, :for_id, :msg_text, NOW(), NOW())"
        self.__data = {
            'user_id': user_id,
            'for_id': id,
            'msg_text': form['message']
        }
        return self.run_query(self.__query, self.__data)

    def get_comments(self, id):
        self.__query = "SELECT c.id, c.msg_id, concat(u.first_name, ' ', u.last_name) AS name, c.cmt_text, DATE_FORMAT(c.created_at, '%b %D %Y') AS created_at FROM comments c, users u WHERE c.msg_id = :msg_id AND c.user_id = u.id ORDER BY c.created_at DESC"
        self.__data = {
            'msg_id': id,
        }
        return self.run_query(self.__query, self.__data)

    def insert_comment(self, id, form, for_id, user_id):
        self.__query = "INSERT INTO comments (msg_id, user_id, for_id, cmt_text, created_at, modified_at) VALUES (:msg_id, :user_id, :for_id, :cmt_text, NOW(), NOW())"
        self.__data = {
            'msg_id': id,
            'user_id': user_id,
            'for_id': for_id,
            'cmt_text': form['comment']
        }
        return self.run_query(self.__query, self.__data)
