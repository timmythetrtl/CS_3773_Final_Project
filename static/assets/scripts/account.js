document.addEventListener('DOMContentLoaded', function() {
    window.onload = function() {
        // login form
        function openLoginForm() {
            document.getElementById("login-form-container").style.display = "flex";
            document.getElementById("login-overlay").style.display = "block";
        }

        function closeLoginForm() {
            document.getElementById("login-form-container").style.display = "none";
            document.getElementById("login-overlay").style.display = "none";
        }

        document.getElementById("login-button").onclick = function () {
            openLoginForm();
        };

        document.getElementById("login-close-button").onclick = function () {
            closeLoginForm();
        };

        document.getElementById("login-form").onsubmit = submitLoginForm;

        function submitLoginForm(event) {
            // prevent the form from submitting in the traditional way
            event.preventDefault();

            var username = document.getElementById("login-username").value;
            var password = document.getElementById("login-password").value;

            // create data object to send with AJAX request
            var data = {
                "login-username": username,
                "login-password": password
            };

            // send AJAX request to Flask server
            fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Successful login, close the form
                    closeLoginForm();
                    updateNavigationForLoggedInUser(username);
                    //location.reload()
                } else {
                    // Failed login, display the error message
                    document.querySelector('.error-message').innerHTML = data.error || "Invalid username or password";
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }

        function updateNavigationForLoggedInUser(username) {
            var loginButton = document.getElementById("login-button");
            var signupButton = document.getElementById("signup-button");
            var usernameButton = document.createElement("span");
            var logoutButton = document.createElement("a");

            loginButton.style.display = "none";
            signupButton.style.display = "none";

            usernameButton.innerText = username;
            usernameButton.className = "nav-link link-body-emphasis px-2";
            logoutButton.href = "/logout";
            logoutButton.innerText = "Log out";
            logoutButton.className = "nav-link link-body-emphasis px-2";

            var nav = document.querySelector('.nav');
            nav.appendChild(usernameButton);
            nav.appendChild(logoutButton);

        }

        //makes sure that if someone is logged in, they dont sign out for any reason
        function checkLoginStatus() {
        fetch("/check_login_status") // Add a Flask route to check login status
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Update navigation if the user is logged in
                    updateNavigationForLoggedInUser(data.username);
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }

        checkLoginStatus();

        // signup form
        function openSignupForm() {
            document.getElementById("signup-form-container").style.display = "flex";
            document.getElementById("signup-overlay").style.display = "block";
        }

        function closeSignupForm() {
            document.getElementById("signup-form-container").style.display = "none";
            document.getElementById("signup-overlay").style.display = "none";
        }

        function submitSignupForm(event) {
            // prevent the form from submitting in the traditional way
            event.preventDefault();

            var username = document.getElementById("signup-username").value;
            var password = document.getElementById("signup-password").value;

            // create data object to send with AJAX request
            var data = {
                "signup-username": username,
                "signup-password": password
            };

            // send AJAX request to Flask server
            fetch("/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                closeSignupForm();
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }

        document.getElementById("signup-form").onsubmit = submitSignupForm;

        document.getElementById("signup-button").onclick = function () {
            openSignupForm();
        };


    };
});