from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired('Enter the title'), Length(min=4, max=300, message='Title must be 4-300 characters')])  
    body = TextAreaField('Body', validators=[InputRequired('Enter the body'), Length(min=50, max=10000, message='Body must contain at least 50 characters')]) 