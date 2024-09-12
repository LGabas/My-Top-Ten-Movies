from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

# WTFORM FOR RATING MOVIE
class RatingForm(FlaskForm):
    rating = FloatField(label='Your Rating Out of 10', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField("Done")

# WTFORM FOR MOVIE TITLE
class TitleForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')