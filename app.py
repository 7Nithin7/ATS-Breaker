import os
from flask import Flask, render_template, request, redirect, jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
# from pyresparser import ResumeParser
from test import *
from custom import *

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dlfhjudvguy4wtyhriuwe6878y'
login_manager.init_app(app)
db.init_app(app)

thisdict = {}
data = {}
thisdict["nithincgeorge98@gmail.com"] = "pass"


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('pass')

        try:
            user = User.query.filter_by(email = email).first()
            print(user)
            if (check_password_hash(user.password, password)):
                login_user(user)
                return redirect('/front')
            else:
                return render_template('index.html', response = "Invalid Password")
        except:
            return redirect('/')

    else:
        # print('Hi')
        # wordfinder()
        return render_template("index.html")
        
        


@app.route('/register', methods=['GET', 'POST'])
def sign():
    if (request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('pass')
        fname = request.form.get('fname')
        lname = request.form.get('lname')

        # Add User
        try:
      
            new_user = User(fname = fname, lname = lname, email = email, password = generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
        except:
            return render_template("register.html")


        return redirect('/')
    else:
        return render_template("register.html")


@app.route('/front', methods=['GET', 'POST'])
@login_required
def front():
    if (request.method == 'POST'):
        # print("jjjjj")
        resume = request.files['resume']
        if (resume.filename != ''):
            res = secure_filename(resume.filename)
            resume.save(res)
            # print(secure_filename(resume.filename))
            data['resume_skills'] = extract((res))

            # Custom Function
            res_dict = wordfinder(res, data['resume_skills']) 
                
            
        else:
            resume_text = request.form.get('resume_text').replace(u'\u2022', ' ')
            data['resume_skills'] = conv(resume_text)

            # Custom Function
            res_dict = extractor(resume_text, data['resume_skills'])

        

        job_description = request.files['job_description']
        if (job_description.filename != ''):
            jd = secure_filename(job_description.filename)
            job_description.save(jd)
            data['jd_skills'] = extract(jd)

            # Custom Function
            jd_dict = wordfinder(jd, data['jd_skills'])
            
        else:
            job_description_text = request.form.get('job_description_text').replace(u'\u2022', ' ')
            data['jd_skills'] = conv(job_description_text)
            # print(data['jd_skills'])

            # Custom Function
            jd_dict = extractor(job_description_text, data['jd_skills'])


        # print(jsonify(data))
        # data = jsonify("data")
        # print(len(jd_dict))
        score = 0
        for skill in jd_dict:
            if (res_dict[skill]):
                score += 1
        try:
            
            score = int(score/len(jd_dict) * 100)
        except:
            pass
        # print(score)
        return render_template("front.html", rs = (res_dict), jd = (jd_dict.most_common()), score = score)
    else:
        return render_template("front.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')






if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    #     admin = User(fname = 'Nithin', lname = 'George', email = 'nithincgeorge98@gmail.com', password = generate_password_hash('pass'))
    #     db.session.add(admin)
    #     db.session.commit()

    app.run(debug=False)
