"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes

    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Index'
routes['/logoff'] = 'Index#logoff'
routes['/login'] = 'Index#gotologin'
routes['/register'] = 'Index#gotoregister'
routes['/dashboard'] = 'Index#gotodash'
routes['/users/new'] = 'Users#new'
routes['/users/remove/<id>'] = 'Users#remove'
routes['/users/remove/<id>/yes'] = 'Users#remove_yes'
routes['/users/remove/no'] = 'Users#remove_no'
routes['/users/edit/<id>'] = 'Users#profile'
routes['/users/<id>/edit'] = 'Users#edit'
routes['/users/show/<id>'] = 'Messages#show_mb'
routes['POST']['/login'] = 'Login#login'
routes['POST']['/register'] = 'Login#register'
routes['POST']['/users/update/detail/<id>'] = 'Users#upd_dtl'
routes['POST']['/users/update/pwd/<id>'] = 'Users#upd_pwd'
routes['POST']['/users/update/desc/<id>'] = 'Users#upd_desc'
routes['POST']['/messages/get_comments/<id>'] = 'Messages#comments_for'
routes['POST']['/messages/<id>'] = 'Messages#post_msg'
routes['POST']['/comments/<id>'] = 'Messages#post_cmt'
"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.

    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path).
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
