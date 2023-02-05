from flask import render_template, send_from_directory, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from methods import get_app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from methods import Author
from methods import db
from methods import Paper
from methods import reveiw
from methods import reviewer

app = get_app()
app.config['UPLOAD_FOLDER'] = "/papers"
app.config['SECRET_KEY'] = 'hello'


@app.route("/")
def main():
    return render_template('homepage.html')


@app.route("/show_author", methods=['GET', 'POST'])
def show_author():
    print(request.method)
    if request.method == 'POST':
        ok = request.form.get("search")
        answer = [Author.query.get(ok)]
        print(answer)
        return render_template("AUTHORTABLE.html", bod=answer)
    else:
        answer = Author.query.all()
        print(answer[0].__dict__)
    return render_template("AUTHORTABLE.html", bod=answer)


@app.route("/show_paper", methods=['GET', 'POST'])
def show_paper():
    if request.method == 'POST':
        ok = request.form.get("search")
        answer = [Paper.query.get(ok)]
        return render_template("PAPERTABLE.html", bod=answer)
    else:
        answer = Paper.query.all()
        print(answer[0].__dict__)
    return render_template("PAPERTABLE.html", bod=answer)


@app.route("/show_reviewer", methods=['GET', 'POST'])
def show_reviewer():
    if request.method == 'POST':
        ok = request.form.get("search")
        answer = [reviewer.query.get(ok)]
        print(answer)
        return render_template("REVIEWERTABLE.html", bod=answer)
    else:
        answer = reviewer.query.all()
        print(answer[0].__dict__)

    return render_template("REVIEWERTABLE.html", bod=answer)


@app.route("/show_review", methods=['GET', 'POST'])
def show_review():
    if request.method == 'POST':
        ok = request.form.get("search")
        answer = [reveiw.query.filter_by(Email=ok)]
        return render_template("REVIEWTABLE.html", bod=answer)
    else:
        answer = reveiw.query.all()

    return render_template("REVIEWTABLE.html", bod=answer)


@app.route('/reviewer', methods=['GET', 'POST'])
def reviewer_add():
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('Email')
        first_name = request.form.get('First_Name')
        last_name = request.form.get('Last_Name')
        phone_no = (request.form.get('Phone_Number'))
        Affliation = request.form.get("Affliation")
        print(email, first_name, last_name, phone_no, Affliation)
        a1 = reviewer(Email=email, First_name=first_name, Last_name=last_name, Phone_number=phone_no,
                      Affiliation=Affliation)
        db.session.add(a1)
        db.session.commit()
        print(request.form)
        return request.form
    else:
        return render_template('rewiever.html')


@app.route('/login', methods=['GET', 'POST'])
def login_all():
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        print(request.args)

    else:
        return render_template('login.html')


@app.route('/author', methods=['GET', 'POST'])
def sign_up_author():
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        try:
            a1 = Author(Email=email, First_name=first_name, Last_name=last_name)
            db.session.add(a1)
            db.session.commit()

        except Exception as e:
            flash(e.args, 'error')
            return redirect(url_for('sign_up_author'))
        return render_template('success.html')
    else:
        return render_template('author.html')


@app.route('/paper', methods=['GET', 'POST'])
def add_paper():
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('email')
        f = request.files['paper_name']
        f.save(f"paper/{secure_filename(f.filename)}")
        paper_title = request.form.get("'paper_title")
        filename = f.filename

        abstract = request.form.get('abstract')
        paper_id = request.form.get('paper_id')
        print(paper_title)
        a1 = Paper(author_email=email, Abstract=abstract, File_name=filename, Title=paper_title, Paper_id=paper_id)
        db.session.add(a1)
        db.session.commit()
        print(request.form)
        return render_template('success.html')
    else:
        return render_template('paper.html')


@app.route('/review', methods=['GET', 'POST'])
def add_review():
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        paper_id = request.form.get('paper_id')
        reviewer_id = request.form.get('reviewer_id')
        meritscore = request.form.get('meritscore')
        originality_score = request.form.get('originality_score')
        relevanceScore = request.form.get('RelevanceScore')
        readabilityScore = request.form.get('ReadabalityScore')
        Recommendation = request.form.get('RECOMMENDATION')
        incomment = request.form.get('INCOMMENT')
        outcomment = request.form.get('OUTCOMMENT')
        print(Recommendation)
        a1 = reveiw(Paperid=paper_id, Email=reviewer_id, MeritScore=meritscore, OriginalityScore=originality_score,
                    ReadabilityScore=readabilityScore, RelevanceScore=relevanceScore, Recommendation=Recommendation,
                    AuthorFeedback=incomment,
                    CommitteFeedback=outcomment)
        db.session.add(a1)
        db.session.commit()
        print(request.form)
        return request.form
    else:
        return render_template('rewiev.html')


@app.route('/<file>')
@app.route('/static/<file>')
def send(file):
    return send_from_directory('static', file)


app.run(host="0.0.0.0", debug=True)
