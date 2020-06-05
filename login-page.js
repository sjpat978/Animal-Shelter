const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
//const loginErrorMsg = document.getElementById("login-error-msg");

// When the login button is clicked, the following code is executed
/*loginButton.addEventListener("click", (e) => {
    // Prevent the default submission of the form
    e.preventDefault();
    // Get the values input by the user in the form fields
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    if (username === "user" && password === "web_dev") {
        // If the credentials are valid, show an alert box and reload the page
        alert("You have successfully logged in.");
        location.reload();
    } else {
        // Otherwise, make the login error message show (change its oppacity)
        alert("Access Denied.");
    } 
    var username = document.login.username.value;
    var password = document.login.password.value;
    var valid = false;
    var usernameArray = ["Bob", "Joe"];
    var passwordArray = ["12345", "54321"];
    for (var i = 0; i < usernameArray.length; i++) {
        if ((username == usernameArray[i]) && (password = passwordArray[i])) {
            valid = true;
            break;
        }
    }
    if (valid == true) {
        alert("Login successful");
    }
    else {
        alert("Access Denied");
    }
});*/

function valid() {
    var uname = document.forms["login-form"]["uname"].value;
    var pass = document.forms["login-form"]["pass"].value;
    if (uname == "animalluver") {
        if (pass == "123") {
            alert("login successful");
        }
        else {
            alert("incorrect");
        }
    }
    else {
        alert("incorrect");
    }
}