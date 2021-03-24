from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PropertyForm(FlaskForm):
	title = TextField("Property Title", validators=[DataRequired()])
	description = TextAreaField("Description", validators=[DataRequired()], render_kw={"rows": 5, "cols": 60})
	rooms = TextField("No. of Rooms", validators=[DataRequired()])
	bathrooms = TextField("No. of Bathrooms", validators=[DataRequired()])
	price = TextField("Price", validators=[DataRequired()])
	location = TextField("Location", validators=[DataRequired()])
	propertyType = SelectField(u'Property Type', choices=[('House'), ('Apartment')])
	photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])
