from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    phone_number = db.Column(db.Integer)

    @validates('name')
    def validate_name(self, key, name):
        if name == "":
            raise ValueError("Name cannot be left blank!")
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if len(number) == 10:
            return number
        raise ValueError("Phone number must be 10 digits!")

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    @validates('title')
    def validate_title(self, key, title):
        clickbait = ["Won't believe", "Secret", "Top", "Guess"]
        if not any(included in title for included in clickbait):
            raise ValueError("Title doesn't have necessary clickbait!")
        return title
    
    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Content must be at least 250 characters!")
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Summary has exceeded maximum limit of 250 characters!")
        return summary
    
    @validates('category')
    def validate_post(self, key, category):
        if category.lower() != "fiction" or category.lower() != "non-fiction":
            raise ValueError("Post category must be either 'Fiction' or 'Non-Fiction'")
        return category
    
