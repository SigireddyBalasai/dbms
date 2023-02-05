from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql://./conference?driver=ODBC Driver 17 for SQL Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()


class Author(db.Model):
    __tablename__ = 'Author'
    Email = db.Column(db.String(50), primary_key=True)
    First_name = db.Column(db.String(20), unique=True, nullable=False)
    Last_name = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, Email, First_name, Last_name):
        self.Email = Email
        self.First_name = First_name
        self.Last_name = Last_name


class reviewer(db.Model):
    __tablename__ = 'reviewer'
    Email = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    First_name = db.Column(db.String(20), unique=True, nullable=False)
    Last_name = db.Column(db.String(20), unique=True, nullable=False)
    Affliation = db.Column(db.String(20), unique=True, nullable=False)
    Phone_number = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, Email, First_name, Last_name, Affiliation, Phone_number):
        self.Email = Email
        self.First_name = First_name
        self.Last_name = Last_name
        self.Affliation = Affiliation
        self.Phone_number = Phone_number


class Paper(db.Model):
    __tablename__ = 'Papers'
    Paper_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=False)
    Abstract = db.Column(db.String(50), unique=True, nullable=False)
    Title = db.Column(db.String(50), unique=True, nullable=False)
    File_name = db.Column(db.String(50), unique=True, nullable=False)
    author_email = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, Paper_id, Abstract, Title, File_name, author_email):
        self.Paper_id = Paper_id
        self.Title = Title
        self.author_email = author_email
        self.Abstract = Abstract
        self.File_name = File_name


class reveiw(db.Model):
    __tablename__ = 'reveiw'
    Email = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    MeritScore = db.Column(db.Integer, unique=True, nullable=False)
    RelevanceScore = db.Column(db.Integer, unique=True, nullable=False)
    OriginalityScore = db.Column(db.Integer, unique=True, nullable=False)
    ReadabilityScore = db.Column(db.Integer, unique=True, nullable=False)
    Paperid = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    AuthorFeedback = db.Column(db.String(50), unique=True, nullable=False)
    CommitteFeedback = db.Column(db.String(50), unique=True, nullable=False)
    Recommendation = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, Email, MeritScore, RelevanceScore, OriginalityScore, ReadabilityScore, Paperid, AuthorFeedback,
                 CommitteFeedback, Recommendation):
        self.Email = Email
        self.MeritScore = MeritScore
        self.RelevanceScore = RelevanceScore
        self.OriginalityScore = OriginalityScore
        self.ReadabilityScore = ReadabilityScore
        self.Paperid = Paperid
        self.AuthorFeedback = AuthorFeedback
        self.CommitteFeedback = CommitteFeedback
        self.Recommendation = Recommendation


def get_app():
    return app
