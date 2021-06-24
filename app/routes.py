from flask import url_for, render_template
from werkzeug.utils import redirect
from urllib.parse import urlencode
from app import app
from app.forms import forms_py


@app.route('/')
@app.route('/index')
def index():
    """
    No Main page created for the site. Hence redirecting to Sign Up page.
    :return:
    """
    return redirect(url_for('register'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms_py.RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        vusername= form.vusername.data
        vemail= form.vemail.data
        return redirect(url_for('redirecting', username=username, email=email, vusername=vusername , vemail=vemail))
    return render_template('register.html', title='Register', form=form)


@app.route('/redirect/<username>/<email>/<vusername>/<vemail>', methods=['GET', 'POST'])
def redirecting(username, email, vusername, vemail):
    Division_Vice_President_UserName = "Roshan Gardi"
    Division_Vice_President_Email = "Roshan.Gardi-sa@csulb.edu"
    parameters = dict(Requester_UserName=username, Requester_Email=email,
                      DivisionVicePresident_UserName=vusername, DivisionVicePresident_Email=vemail)
    redirect_baseUrl = "https://na3.docusign.net/Member/PowerFormSigning.aspx?PowerFormId=ce0bc78a-2876-49ef-b9a5" \
                       "-83f6e515e855&env=na3&acct=713450e5-2dd0-4676-a3cb-609115e008d7&v=2"
    redirect_url = redirect_baseUrl + ("&" + urlencode(parameters) if parameters else "")
    print(redirect_url)
    return redirect(redirect_url)
