document.getElementById('mentor-login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const email = document.getElementById('mentor-email').value;
    const password = document.getElementById('mentor-password').value;

    // Perform client-side validation (optional)
    if (email === "" || password === "") {
        alert("Please fill in all fields");
        return;
    }

    // Example: Send a request to the back-end for mentor login
    const mentorLoginData = {
        email: email,
        password: password
    };

    fetch('https://education-counselling-server.vercel.app/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(mentorLoginData),
    })
   // .then(response => {response.json();console.log("The response is",response);})
   .then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json(); 
})
.then(data => {
    console.log("Response data:", data); 
})
.catch(error => {
    console.error('Error:', error);
    // .then(data => {
    //     if (data.success) {
    //         alert('Login successful!');
    //         window.location.href = '/mentor-dashboard.html';  // Redirect to the mentor dashboard
    //     } else {
    //         alert('Login failed: ' + data.message);
    //     }
    // })
    
    });
});
