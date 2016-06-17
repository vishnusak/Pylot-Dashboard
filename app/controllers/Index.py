from system.core.controller import *

class Index(Controller):
    def __init__(self, action):
        super(Index, self).__init__(action)
        self.__init_func_called = False

    def __init_func(self):
        if 'user-id' not in session:
            session['user-id'] = None
        if 'user' not in session:
            session['user'] = None
        if 'user_level' not in session:
            session['user_level'] = None
        if 'all_users' not in session:
            session['all_users'] = []
        if 'err' not in session:
            session['err'] = {}
        if 'form' not in session:
            session['form'] = {}
        if 'page' not in session:
            session['page'] = ''
        if 'popup' not in session:
            session['popup'] = False
        if 'popup-id' not in session:
            session['popup-id'] = None
        if 'edit_user' not in session:
            session['edit_user'] = {}
        if 'mb' not in session:
            session['mb'] = {}
        if 'messages' not in session:
            session['messages'] = []
        if 'comments' not in session:
            session['comments'] = []

        self.__init_func_called = True

    def index(self):
        if not self.__init_func_called:
            self.__init_func()

        session['err'] = {}
        session['form'] = {}
        session['page'] = ''
        session['popup'] = False
        session['popup-id'] = None
        session['edit_user'] = {}

        if session['user-id']:
            return self.load_view('dashboard.html')
        else:
            return self.load_view('index.html')

    def logoff(self):
        session.clear()
        self.__init_func_called = False
        return redirect('/')

    def gotologin(self):
        if not self.__init_func_called:
            self.__init_func()

        return self.load_view('login.html')

    def gotoregister(self):
        if not self.__init_func_called:
            self.__init_func()

        session['page'] = 'register'
        return self.load_view('register.html')

    def gotodash(self):
        if not self.__init_func_called:
            self.__init_func()

        if session['user-id']:
            return self.load_view('dashboard.html')
        else:
            return redirect('/login')
