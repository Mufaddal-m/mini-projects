// Import the built-in HTTP module
const http = require('http');

// Define the port to listen on
const PORT = 3000;

// Create a server
const server = http.createServer((req, res) => {
    // Set the response header
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    // Check the URL path
    if (req.url === '/') {
        res.end('Hello, welcome to the home page!');
    } else if (req.url === '/about') {
        res.end('This is the about page!');
    } else {
        res.writeHead(404);
        res.end('404 Not Found');
    }
});

// Start the server
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
