from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__) 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('FirstName must greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
        

    return render_template('sign_up.html')