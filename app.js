// app.js

const express = require('express');
const app = express();
const PORT = 3000;

// Simple route
app.get('/', (req, res) => {
    res.send('Hello, Express!');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
