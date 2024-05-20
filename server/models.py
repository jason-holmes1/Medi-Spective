from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from config import db, bcrypt

#Models for Database

class User(db.Model,SerializerMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    journal_entries = db.relationship('JournalEntry', backref='user', lazy=True)


    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    def __repr__(self):
        return f'<User {self.username}>'

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
        if len(username) > 100:
            raise AssertionError('Username must be less than 100 characters')
        return username

    @validates('password')
    def validate_password(self, key, password):
        if not password:
            raise AssertionError('No password provided')
        if len(password) > 100:
            raise AssertionError('Password must be less than 100 characters')
        return password

class JournalEntry(db.Model,SerializerMixin):
    __tablename__ = 'journal_entry'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'<JournalEntry {self.title}>'

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise AssertionError('No title provided')
        if len(title) > 100:
            raise AssertionError('Title must be less than 100 characters')
        return title

    @validates('content')
    def validate_content(self, key, content):
        if not content:
            raise AssertionError('No content provided')
        if len(content) > 500:
            raise AssertionError('Content must be less than 500 characters')
        return content

    @validates('date')
    def validate_date(self, key, date):
        if not date:
            raise AssertionError('No date provided')
        return date
    
class CommunityPost(db.Model,SerializerMixin):
    __tablename__ = 'community_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'<CommunityPost {self.title}>'

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise AssertionError('No title provided')
        if len(title) > 100:
            raise AssertionError('Title must be less than 100 characters')
        return title

    @validates('content')
    def validate_content(self, key, content):
        if not content:
            raise AssertionError('No content provided')
        if len(content) > 500:
            raise AssertionError('Content must be less than 500 characters')
        return content

    @validates('date')
    def validate_date(self, key, date):
        if not date:
            raise AssertionError('No date provided')
        return date
    
class MoodInput(db.Model,SerializerMixin):
    __tablename__ = 'mood_input'
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'<MoodInput {self.mood}>'
    @validates('mood')
    def validate_mood(self, key, mood):
        if not mood:
            raise AssertionError('No mood provided')
        if mood < 1 or mood > 10:
            raise AssertionError('Mood must be between 1 and 10')
        return mood

    @validates('date')
    def validate_date(self, key, date):
        if not date:
            raise AssertionError('No date provided')
        return date
class Resources(db.Model,SerializerMixin):
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'<Resources {self.title}>'

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise AssertionError('No title provided')
        if len(title) > 100:
            raise AssertionError('Title must be less than 100 characters')
        return title

    @validates('content')
    def validate_content(self, key, content):
        if not content:
            raise AssertionError('No content provided')
        if len(content) > 500:
            raise AssertionError('Content must be less than 500 characters')
        return content

    @validates('date')
    def validate_date(self, key, date):
        if not date:
            raise AssertionError('No date provided')
        return date