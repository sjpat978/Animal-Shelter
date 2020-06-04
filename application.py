import os, requests

from flask import Flask, session, render_template, redirect, request, flash, url_for, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def login_required(f):
    """
    Decorate routes to require login.
    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("email") is None:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    # if GET, show the registration form
    if request.method == "GET":
        return render_template("register.html")

    # if POST, validate and commit to database

    else:
        #if form values are empty show error
        if not request.form.get("first_name"):
            return render_template("error.html", message="Must provide First Name")
        elif not request.form.get("last_name"):
            return render_template("error.html", message="Must provide Last Name")
        elif  not request.form.get("email"):
            return render_template("error.html", message="Must provide E-mail")
        elif not request.form.get("password1") or not request.form.get("password2"):
            return render_template("error.html", message="Must provide password")
        elif request.form.get("password1") != request.form.get("password2"):
            return render_template("error.html", message="Password does not match")
        else :
            ## assign to variables
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            email = request.form.get("email")
            password = request.form.get("password1")
            # try to commit to database, raise error if any
            try:
                db.execute("INSERT INTO users (firstname, lastname, email, password) VALUES (:firstname, :lastname, :email, :password)",
                               {"firstname": first_name, "lastname": last_name, "email":email, "password": generate_password_hash(password)})
            except Exception as e:
                return render_template("error.html", message=e)
            #success - redirect to login
            db.commit()
            return redirect(url_for("login"))

@app.route("/register_staff", methods=["GET", "POST"])
def register_staff():

    # if GET, show the registration form
    if request.method == "GET":
        return render_template("register_staff.html")

    # if POST, validate and commit to database

    else:
        #change according to staff input fields
        #if form values are empty show error
        if not request.form.get("shelter"):
            return render_template("error.html", message="Must provide shelter name")
        elif  not request.form.get("email2"):
            return render_template("error.html", message="Must provide E-mail")
        elif not request.form.get("password3") or not request.form.get("password4"):
            return render_template("error.html", message="Must provide password")
        elif request.form.get("password3") != request.form.get("password4"):
            return render_template("error.html", message="Password does not match")
        else :
            ## assign to variables
            shelter = request.form.get("shelter")
            email = request.form.get("email")
            password3 = request.form.get("password3")
            # try to commit to database, raise error if any
            try:
                db.execute("INSERT INTO users (shelter, email, password3) VALUES (:shelter, :email, :password3)",
                               {"shelter": shelter, "email":email, "password3": generate_password_hash(password3)})
            except Exception as e:
                return render_template("error.html", message=e)
            #success - redirect to login
            db.commit()
            return redirect(url_for("login_staff"))


@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        form_email = request.form.get("email")
        form_password = request.form.get("password")

        # Ensure username and password was submitted
        if not form_email:
            return render_template("error.html", message="must provide username")
        elif not form_password:
            return render_template("error.html", message="must provide password")

        # Query database for email and password
        Q = db.execute("SELECT * FROM users WHERE email LIKE :email", {"email": form_email}).fetchone()

        # User exists ?
        if Q is None:
            return render_template("error.html", message="User doesn't exist")
        # Valid password ?
        if not check_password_hash( Q.password, form_password):
            return  render_template("error.html", message = "Invalid password")

        # Remember which user has logged in
        session["user_id"] = Q.userid
        session["email"] = Q.email
        session["firstname"] = Q.firstname
        session["logged_in"] = True
        return render_template("location.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login-page-staff.html")

@app.route("/login_staff", methods=["GET", "POST"])
def login_staff():

    # Forget any user_id
    session.clear()
#change according to what aditi makes staff register field
    if request.method == "POST":
        form_email = request.form.get("email2")
        form_password = request.form.get("password3")

        # Ensure username and password was submitted
        if not form_email:
            return render_template("error.html", message="must provide username")
        elif not form_password:
            return render_template("error.html", message="must provide password")

        # Query database for email and password
        Q = db.execute("SELECT * FROM users_staff WHERE email2 LIKE :email2", {"email2": form_email}).fetchone()

        # User exists ?
        if Q is None:
            return render_template("error.html", message="User doesn't exist")
        # Valid password ?
        if not check_password_hash( Q.password, form_password):
            return  render_template("error.html", message = "Invalid password")

        # Remember which user has logged in
        session["user_id"] = Q.userid2
        session["email2"] = Q.email2
        session["shelter"] = Q.shelter
        session["logged_in"] = True
        return render_template("location_staff.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login-page-staff.html")


@app.route("/logout")
@login_required
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to login index
    return redirect(url_for("index"))

@app.route("/search_illinois", methods=["GET","POST"])
@login_required
def search_illinois():
    if request.method == "GET":
        return render_template("search_illinois.html")
    else:
        query = request.form.get("search")
        if query is None:
            return render_template("error.html", message="Search field can not be empty!")
        try:
            result = db.execute("SELECT * FROM illinois WHERE LOWER(Breed) LIKE :query OR LOWER(AnimalType) LIKE :query", {"query": "%" + query.lower() + "%"}).fetchall()
        except Exception as e:
            return render_template("error.html", message=e)
        if not result:
            return render_template("error.html", message="None found")
        return render_template("list_illinois.html", result=result)

@app.route("/search_arizona", methods=["GET","POST"])
@login_required
def search_arizona():
    if request.method == "GET":
        return render_template("search_arizona.html")
    else:
        query = request.form.get("search")
        if query is None:
            return render_template("error.html", message="Search field can not be empty!")
        try:
            result = db.execute("SELECT * FROM arizona WHERE LOWER(Breed) LIKE :query OR LOWER(AnimalType) LIKE :query", {"query": "%" + query.lower() + "%"}).fetchall()
        except Exception as e:
            return render_template("error.html", message=e)
        if not result:
            return render_template("error.html", message="None found")
        return render_template("list_arizona.html", result=result)

@app.route("/search_california", methods=["GET","POST"])
@login_required
def search_california():
    if request.method == "GET":
        return render_template("search_california.html")
    else:
        query = request.form.get("search")
        if query is None:
            return render_template("error.html", message="Search field can not be empty!")
        try:
            result = db.execute("SELECT * FROM california WHERE LOWER(Breed) LIKE :query OR LOWER(AnimalType) LIKE :query", {"query": "%" + query.lower() + "%"}).fetchall()
        except Exception as e:
            return render_template("error.html", message=e)
        if not result:
            return render_template("error.html", message="None found")
        return render_template("list_cali.html", result=result)








