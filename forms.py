from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, DateField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Optional
from wtforms.fields import DateTimeLocalField
from flask_ckeditor import CKEditorField

# Form in question