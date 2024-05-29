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
    date = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


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

    
class CommunityPost(db.Model,SerializerMixin):
    class CommunityPost(db.Model, SerializerMixin):
        __tablename__ = 'community_post'
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        content = db.Column(db.String(500), nullable=False)
        date = db.Column(db.DateTime, nullable=True)
        comments = db.relationship('Comments', backref='community_post', lazy=True)

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

class Comments(db.Model,SerializerMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    community_post_id = db.Column(db.Integer, db.ForeignKey('community_post.id'), nullable=True)

    def __repr__(self):
        return f'<Comment {self.content}>'

    @validates('content')
    def validate_content(self, key, content):
        if not content:
            raise AssertionError('No content provided')
        if len(content) > 500:
            raise AssertionError('Content must be less than 500 characters')
        return content

    @validates('title')
    def validate_date(self, key, title):
        if not title:
            raise AssertionError('No title provided')
        return title