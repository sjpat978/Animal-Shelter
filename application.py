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
        ## end validation
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
def register():

    # if GET, show the registration form
    if request.method == "GET":
        return render_template("register_staff.html")

    # if POST, validate and commit to database

    else:
        #if form values are empty show error
        if not request.form.get("first_name_2"):
            return render_template("error.html", message="Must provide First Name")
        elif not request.form.get("last_name_2"):
            return render_template("error.html", message="Must provide Last Name")
        elif  not request.form.get("email_2"):
            return render_template("error.html", message="Must provide E-mail")
        elif not request.form.get("password1_2") or not request.form.get("password2"):
            return render_template("error.html", message="Must provide password")
        elif request.form.get("password1_2") != request.form.get("password2"):
            return render_template("error.html", message="Password does not match")
        if not request.form.get("shelter_2"):
            return render_template("error.html", message="Must provide shelter name")
        ## end validation
        else :
            ## assign to variables
            first_name_2 = request.form.get("first_name_2")
            last_name_2 = request.form.get("last_name_2")
            email_2 = request.form.get("email_2")
            password_2 = request.form.get("password1_2")
            shelter_2 = request.form.get("shelter_2")
            # try to commit to database, raise error if any
            try:
                db.execute("INSERT INTO users_staff (firstname2, lastname2, email2, password2, shelter2) VALUES (:firstname2, :lastname2, :email2, :password2, :shelter2)",
                               {"firstname2": first_name_2, "lastname2": last_name_staff, "email2":email, "password2": generate_password_hash(password), "shelter2": shelter_staff})
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
            return render_template("error.html", message="User doesn't exists")
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
        return render_template("login.html")

@app.route("/login_staff", methods=["GET", "POST"])
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
            return render_template("error.html", message="User doesn't exists")
        # Valid password ?
        if not check_password_hash( Q.password, form_password):
            return  render_template("error.html", message = "Invalid password")

        # Remember which user has logged in
        session["user_id"] = Q.userid
        session["email"] = Q.email
        session["firstname"] = Q.firstname
        session["logged_in"] = True
        return render_template("location_staff.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")








