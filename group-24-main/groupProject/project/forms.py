from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError, Email
from project.models import User, Choices

class Register(FlaskForm):

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')
    username = StringField(label = 'Username:', validators=[Length(min=2, max=30), DataRequired(message = "Username field should not be empty!")])
    email = StringField(label="Email: ", validators=[Email(), DataRequired(message = "Email field should not be empty!")])
    password = PasswordField(label = 'Password:', validators=[Length(min=6), DataRequired(message = "Password field should not be empty!")])
    confirmation = PasswordField(label = 'Password Confirmation:', validators=[EqualTo('password'), DataRequired(message = "Password confirmation field should not be empty!")])
    submit = SubmitField(label = 'Register')

class SignIn(FlaskForm):
    username = StringField(label = 'Username:', validators=[Length(min=2, max=30), DataRequired(message = "Username field should not be empty!")])
    password = PasswordField(label = 'Password:', validators=[Length(min=6), DataRequired(message = "Password field should not be empty!")])
    submit = SubmitField(label = 'Sign In')

class makeChoice(FlaskForm):
    # tbh this might not be required but I just got it to work and I'm too scared to remove it and have to debug a lot
    def validate_username(self, username):
        choices = Choices.query.filter_by(username=username.data).first()
        if choices:
            raise ValidationError('You have already submitted your choices')
    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired(message = "Username field should not be empty!")])
    # I know that the choices code is ungodly long but there's not too much I can do if I'm going
    # to make the db hold the proper name choices instead of conversions eg (1 = spice up your life)
    first_choice = SelectField(u'First Choice:', choices=[("Spice_up_your_life", "Spice up your life") , ("Ungrading_Simulator", "Ungrading Simulator"), ("Group_Allocation_System", "Group Allocation System"), ("Optical_recognition_in_Online_Games", "Optical recognition in Online Games"), ("Mapping_Cities_in_Python", "Mapping Cities in Python"), ("VICTA_Desktop", "VICTA Desktop"), ("VICTA_Mobile_App", "VICTA Mobile App"), ("Scrapping_Job_listing_websites", "Scrapping Job listing websites")], validators=[DataRequired(message = "you must make a first choice")])
    # I wasn't sure which to use because radio looks fine but select is space efficient, easy and sleek
    # can change SelectField to RadioField if you want to see what radio looks like
    second_choice = SelectField(u'Second Choice:', choices=[("Spice_up_your_life", "Spice up your life") , ("Ungrading_Simulator", "Ungrading Simulator"), ("Group_Allocation_System", "Group Allocation System"), ("Optical_recognition_in_Online_Games", "Optical recognition in Online Games"), ("Mapping_Cities_in_Python", "Mapping Cities in Python"), ("VICTA_Desktop", "VICTA Desktop"), ("VICTA_Mobile_App", "VICTA Mobile App"), ("Scrapping_Job_listing_websites", "Scrapping Job listing websites")], validators=[DataRequired(message="you must make a second choice")])
    third_choice = SelectField(u'Third Choice:', choices=[("Spice_up_your_life", "Spice up your life") , ("Ungrading_Simulator", "Ungrading Simulator"), ("Group_Allocation_System", "Group Allocation System"), ("Optical_recognition_in_Online_Games", "Optical recognition in Online Games"), ("Mapping_Cities_in_Python", "Mapping Cities in Python"), ("VICTA_Desktop", "VICTA Desktop"), ("VICTA_Mobile_App", "VICTA Mobile App"), ("Scrapping_Job_listing_websites", "Scrapping Job listing websites")], validators=[DataRequired(message="you must make a third choice")])
    submit = SubmitField(label='set choices')

