from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, URL

class InstagramForm(FlaskForm):
    username = StringField("Enter your Instagram Id", validators=[DataRequired()])
    password = PasswordField("Enter your Instagram password", validators=[DataRequired()])
    target_username = StringField("Enter the Instagram Id of any user to follow their followers", validators=[DataRequired()])
    submit = SubmitField("SUBMIT")
    
class TinderForm(FlaskForm):
    username = StringField("Enter your Facebook Id", validators=[DataRequired()])
    password = PasswordField("Enter your Facebook password", validators=[DataRequired()])
    submit = SubmitField("SUBMIT")
    
class WifiComplaintForm(FlaskForm):
    promised_up = StringField("Enter your internet Promised Upload speed", validators=[DataRequired()])
    promised_down = StringField("Enter your internet Promised Download speed", validators=[DataRequired()])
    email = StringField("Enter your X/Twitter Phone/Email/Username", validators=[DataRequired(), Email()])
    username = StringField("Enter your X/Twitter Phone/username to verify", validators=[DataRequired()])
    password = PasswordField("Enter your X/Twitter password", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class SpotifyForm(FlaskForm):
    client_id = StringField("Enter your client ID", validators=[DataRequired()])
    client_secret = StringField("Enter your client secret", validators=[DataRequired()])
    date = StringField("Which year do you want to travel to? Type the date in this format YYYY-MM-DD", validators=[DataRequired()])
    submit = SubmitField("SUBMIT")
    
class CookieClickerForm(FlaskForm):
    minute = StringField("Enter how many minute you want to play!", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class WebsiteScrapingForm(FlaskForm):
    url = StringField("Enter a valid website URL", validators=[DataRequired(), URL()])
    element = StringField("Enter a element to scrape, for example( h1, p )", validators=[DataRequired()])
    submit = SubmitField("Submit")