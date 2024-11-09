const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

let mentors = [
    {
        email: 'mentor1@example.com',
        password: 'password123'
    }
];

// Endpoint for mentor login
app.post('/mentor/login', (req, res) => {
    const { email, password } = req.body;

    const mentor = mentors.find(mentor => mentor.email === email && mentor.password === password);

    if (mentor) {
        res.json({ success: true, message: 'Login successful!' });
    } else {
        res.json({ success: false, message: 'Invalid credentials' });
    }
});

app.listen(5000, () => {
    console.log('Server is running on http://localhost:5000');
});
