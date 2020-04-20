from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('E-mail', validators=[DataRequired(), Email()])
	subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=35)])
	message = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=78)])

	submit = SubmitField('Send')

