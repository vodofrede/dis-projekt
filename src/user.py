from flask import Blueprint, render_template

user = Blueprint('user', __name__)

posts = [{}]


@user.route("/")
def get(id):
    return 


@user.route("/about")
def about():
    return render_template('about.html', title='About')


@user.route("/login", methods=['GET', 'POST'])
def login(id):
    result = loginUser(id)
    if (result):
        return render_template('frontpage.html', title='Home')
    else:  
        return render_template('login.html', title='Error')
    


@user.route("/logout")
def logout(id):
    logoutUser(id)
    return render_template('login.html', title='Logout')

