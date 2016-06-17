from system.core.controller import *

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        self.load_model('Message')
        self.__db = self.models['Message']

    def show_mb(self, id):
        self.__mbuser(id)
        self.__getmessages(id)
        return self.load_view('messageboard.html')

    def comments_for(self, id):
        self.__getcomments(id)
        return self.load_view('comments.html')

    def post_msg(self, id):
        user_id = session['user-id']
        self.__db.insert_message(id, request.form, user_id)
        self.__getmessages(id)
        return self.load_view('messages.html')

    def post_cmt(self, id):
        user_id = session['user-id']
        for_id = session['mb']['id']
        self.__db.insert_comment(id, request.form, for_id, user_id)
        self.__getcomments(id)
        return self.load_view('comments.html')

    def __mbuser(self, id):
        mb_user = self.__db.get_id_user(id)[0]
        print mb_user
        session['mb'] = {
            'id': mb_user['id'],
            'email': mb_user['email'],
            'name': mb_user['name'],
            'desc': mb_user['description'],
            'date': mb_user['created_at']
        }

    def __getmessages(self, id):
        session['messages'] = self.__db.get_messages(id)
        print "session['messages'] - ", session['messages']

    def __getcomments(self, id):
        session['comments'] = self.__db.get_comments(id)
        print "session['comments'] - ", session['comments']
