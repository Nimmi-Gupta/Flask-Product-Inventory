from flask import Flask,request,render_template,session

from login_details import *

@app.route("/", methods =['GET'])
def login_page():
    return render_template('login.html')

@app.route('/home_page')
def home_page():
    if "result" and "result1" and "result2" and "result3" in session:
        result= session['result']
        result1=session['result1']
        result2=session['result2']
        result3=session['result3']
    return render_template("home.html",result=result,result1=result1,result2=result2,result3=result3)

@app.route('/login_page',methods=['POST']) # this link for check the data is matched for not and give login _details page
def user_emid_pass():
    if request.method == 'POST':
        formdata= request.form
        emailid =formdata.get('emailid')
        password= formdata.get('password')
        if emailid and password:
            account = User.query.filter(User.email_id  == emailid, User.password == password).first()
            if account:
                session['result'] = account.email_id
                session['result1'] = account.password
                session['result2'] = account.firstname
                session['result3'] = account.lastname
                message = f'{account.email_id}'
                message1 = f'{account.password}'
                message2 = f'{account.firstname}'
                message3 = f'{account.lastname}'
                db.session.add(account)
                db.session.add(account)
                db.session.commit()
                return render_template('home.html',result=message,result1=message1,result2=message2,result3=message3)
            else:
                message = 'Invalid Credentials'
                return render_template("login.html", result=message)
        else:
            message= "Please Entre Username and Password.."
            return render_template("login.html",result=message)

@app.route('/user/registration', methods=['GET','POST'])
def user_registration():
    message=""
    if request.method == "POST":
        formdata = request.form
        emailid = formdata.get('emailid')
        dupli_email=User.query.filter_by(email_id = emailid).first()
        if dupli_email:
            message = "Duplicate Emailid"
            return render_template('registration.html', result=message)

        if formdata.get('password') == formdata.get('confirm_password'):
            user = User(firstname=formdata.get("firstname"),
                    lastname=formdata.get("lastname"),
                    contact=formdata.get("contact"),
                    address=formdata.get("address"),
                    DOB=formdata.get("dob"),
                    email_id=formdata.get("emailid"),
                    password=formdata.get("password"),
                    conform_password=formdata.get("confirm_password"),
                    gender=formdata.get("gender"),
                    age=formdata.get("age"),
                    country=formdata.get("country"),
                    city=formdata.get("city"))
            db.session.add(user)
            db.session.commit()
            message = "User Registration Successfully...."
        else:
            message = "Password and Confirm Password not Matched..."
    return render_template('registration.html',result=message)

@app.route('/add_product', methods=['GET','POST'])
def add_product():
    message=""
    if request.method == "POST":
        formdata= request.form
        id = int(formdata.get('id'))
        # print(id)
        add_prod=Product.query.filter_by(product_id=id).first()
        if add_prod:
            message = "Duplicate Product Id"
            old_list = Product.query.all()
            return render_template('add_product.html', result=message,result1=old_list)
        else:
            prod = Product( #prod_S_NO =formdata.get(""),
                           product_id=formdata.get("id"),
                               name=formdata.get("name"),
                               price=formdata.get("price"),
                               quantity=formdata.get("quantity"),
                               vendor=formdata.get("vendor"),
                               category=formdata.get("category"))
            db.session.add(prod)
            db.session.commit()
            message = "Product Added Successfully..."
    final_list = Product.query.all()
    return render_template('add_product.html',result=message,result1=final_list)

@app.route('/product_final_list', methods=['GET', 'POST'])
def product_final_list():
    final_list = Product.query.all()
    return render_template('product_final_list.html', result1=final_list)

@app.route('/search_product', methods=['GET', 'POST'])
def search_product():
    return render_template('search_product.html')

@app.route('/search_product_id', methods=['GET','POST'])
def search_product_id():
    message=""
    search_product = ""
    if request.method == 'POST':
        formdata = request.form
        id= formdata.get('id')
        search_product = Product.query.filter_by(product_id=id).all()
        if search_product:
            db.session.commit()
            message="Product is Present"
            return render_template('search_product_id.html', result=message, result1=search_product)
        else:
            message = "Product Id is Not Present..."
    return render_template('search_product_id.html',result=message,result1=search_product )

@app.route('/search_product_name', methods=['GET','POST'])
def search_product_name():
    message=""
    search_product = ""
    if request.method == 'POST':
        formdata = request.form
        nd= formdata.get('name')
        search_product = Product.query.filter_by(name=nd).all()
        if search_product:
            db.session.commit()
            message="Product is Present"
            return render_template('search_product_name.html', result=message, result1=search_product)
        else:
            message = "Product Name is Not Present...."
    return render_template('search_product_name.html',result=message,result1=search_product )

@app.route('/delete_product', methods=['GET', 'POST'])
def delete_product():
    return render_template('delete_product.html')

@app.route('/delete_product_id', methods=['GET', 'POST'])
def delete_product_id():
    message=""
    if request.method == 'POST':
        formdata = request.form
        d_id = formdata.get('id')
        if Product.query.filter_by(product_id= d_id).delete():
            db.session.commit()
            message="Product Deleted"
        else:
            message="Product ID is Not Present..."
    final_list = Product.query.all()
    return render_template('delete_product_id.html', result=message, result1= final_list)

@app.route('/delete_product_name', methods=['GET', 'POST'])
def delete_product_name():
    message = ""
    if request.method == 'POST':
        formdata = request.form
        n_id = formdata.get('name')
        if Product.query.filter_by(name=n_id).delete():
            db.session.commit()
            message = "Product Deleted"
        else:
            message = "Product Name is Not Present"
    final_list = Product.query.all()
    return render_template('delete_product_name.html', result=message, result1=final_list)

@app.route('/update_product', methods=['GET', 'POST'])
def update_product():
    return render_template('update_product.html')

@app.route('/update_product_id', methods=['GET','POST'])
def update_product_id():
    message = ''
    final_list = Product.query.all()
    if request.method == 'POST':
        formdata = request.form
        u_id = formdata.get('id')
        update_prod=Product.query.filter_by(product_id=u_id).first()
        if update_prod:
            update_prod.product_id = formdata.get("id")
            update_prod.name = formdata.get("Name")
            update_prod.price = formdata.get("Price")
            update_prod.quantity = formdata.get("Quantity")
            update_prod.vendor = formdata.get("Vendor")
            update_prod.category = formdata.get("Category")
            message = "Update Successfully"
            db.session.commit()
            return render_template('update_product_id.html', result=message,result1=final_list)
        else:
            message="Product ID Not Present "
    return render_template('update_product_id.html',result=message,result1=final_list)

@app.route('/update_product_name', methods=['GET','POST'])
def update_product_name():
    message = ''
    final_list = Product.query.all()
    if request.method == 'POST':
        formdata = request.form
        n_id = formdata.get('name')
        update_prod=Product.query.filter_by(name=n_id).first()
        if update_prod:
            update_prod.product_id = formdata.get("id")
            update_prod.name = formdata.get("Name")
            update_prod.price = formdata.get("Price")
            update_prod.quantity = formdata.get("Quantity")
            update_prod.vendor = formdata.get("Vendor")
            update_prod.category = formdata.get("Category")
            message = "Update Successfully"
            db.session.commit()
            return render_template('update_product_name.html', result=message,result1=final_list)
        else:
            message="Product Name Not Present "
    return render_template('update_product_name.html',result=message,result1=final_list)


@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('result', None)
    session.pop('result1', None)

    result2=session['result2']
    result3=session['result3']

    session.pop('result2', None)
    session.pop('result3', None)
    message = 'You have Successfully Logout..'
    return render_template("login.html",result1= message,result2=result2,result3=result3)


if __name__ == "__main__":
    app.run(debug=True, port= 5006)