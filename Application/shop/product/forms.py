from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, FloatField, TextAreaField, validators

class Addproduct(Form):
    name = StringField('Product Name', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    size = FloatField('Size',[validators.DataRequired()])
    #stock = IntegerField('Stock', [validators.DataRequired()])
    add_info = TextAreaField('Additional Information', [validators.DataRequired()])

    image = FileField('Image', validators = [FileAllowed('jpg','png')])