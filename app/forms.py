import datetime
from flask_wtf import FlaskForm
from wtforms import (IntegerField, PasswordField,
                     SelectField, StringField, SubmitField)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """The form used for logging in."""
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    login = SubmitField("Login")


class PaymentForm(FlaskForm):
    """The form used for creating and updating Payments."""
    employer = SelectField("Employer", choices=[], coerce=int)
    employee = SelectField("Employee", choices=[], coerce=int)

    payment_date = DateField("Payment Date", validators=[DataRequired()], default=datetime.datetime.today)
    amount = IntegerField("Amount")

    submit = SubmitField("Save")


class EmployerForm(FlaskForm):
    """The form used for creating and updating Employers."""
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Save")
    total_amount_paid = IntegerField("Total Amount Paid", default=0)


class EmployeeForm(FlaskForm):
    """The form used for creating and updating Employees."""
    name = StringField("Name", validators=[DataRequired()])
    date_employed = DateField("Date Employed", validators=[DataRequired()], default=datetime.datetime.today)
    submit = SubmitField("Save")
