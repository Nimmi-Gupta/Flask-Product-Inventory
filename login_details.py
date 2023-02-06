from itertools import count

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key="login"
class User(db.Model):

        user_S_No = db.Column('User_Id',db.Integer(),primary_key= True)
        firstname = db.Column('First Name', db.String(30))
        lastname = db.Column('Last Name',db.String(30))
        contact = db.Column ('Contact',db.BigInteger())
        address = db.Column('Address', db.String(30))
        DOB = db.Column('DOB', db.String(30))
        email_id = db.Column('Email ID',db.String(30))
        password = db.Column('Password', db.String(30))
        conform_password = db.Column('Conform Password', db.String(30))
        gender = db.Column('Gender', db.String(30))
        age = db.Column('Age', db.Integer())
        country = db.Column('Country', db.String(30))
        city =db.Column('City',db.String(30))

# db.create_all() # ORM(Object-relational mapping)table create karke dega mysql me(orm h flask sqlalchemy)

#  iske baad ka code jab humko direct program me entre karna ho data ko toh hum aise likhte h
# user=User(user_id=1,firstname="Nimmi",lastname="Gupta",Contact=9071235929,Address="Undri",DOB="12/06/2022",email_id="nimmi@gamil.com",Gender ="Male",age=33,country="India",city="Pune" )
# db.session.add(user)
# db.session.commit()

class Product(db.Model):
        prod_S_NO = db.Column('S_No', db.Integer(),primary_key=True)
        product_id = db.Column('Product_Id', db.Integer())
        name = db.Column('Product_Name', db.String(30))
        price = db.Column('Product_Price', db.Float())
        quantity = db.Column('Product_Quantity', db.Integer())
        vendor = db.Column('Product_Vendor', db.String(30))
        category = db.Column('Product_Category', db.String(30))
db.create_all()


if __name__ == "__main__":
    app.run(debug=True)

