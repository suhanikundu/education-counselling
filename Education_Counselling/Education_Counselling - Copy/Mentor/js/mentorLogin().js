function mentorLogin() {
    var email = document.forms["mentorForm"]["mentorEmail"].value;
    var password = document.forms["mentorForm"]["mentorPassword"].value;

    if (email == "") {
        document.getElementById("mentorEmail").style.backgroundColor = "yellow";
        alert("Please fill the email field");
    }

    if (password == "") {
        document.getElementById("mentorPassword").style.backgroundColor = "yellow";
        alert("Please fill the password field");
    }

    if (email !== "" && password !== "") {
        // Example: Hardcoded validation (replace with server-side validation)
        const mentorEmails = ["john.doe@example.com", "rhitwika@example.com", "debak@example.com", "debosmita@example.com", "suhani@example.com", "suprakash@example.com"];
        
        if (mentorEmails.includes(email)) {
            // Save mentor's email in localStorage and redirect to dashboard
            localStorage.setItem("loggedInMentor", email);
            window.location.href = 'mentor-dashboard.html';
        } else {
            alert("Invalid login credentials.");
        }
    }
}
