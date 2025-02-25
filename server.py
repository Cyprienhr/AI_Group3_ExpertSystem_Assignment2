import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def parse_form_data(self):
        """Helper method to parse form data."""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        form_data = {}

        # Parse the URL-encoded form data (assuming application/x-www-form-urlencoded)
        for item in post_data.split('&'):
            key, value = item.split('=')
            form_data[key] = value

        return form_data

    def do_POST(self):
        """Handle POST requests."""
        # Get the form data from the POST request
        form_data = self.parse_form_data()

        # Print the form data for debugging purposes
        print("Received form data:", form_data)

        # Check if 'business_age' is in the form data
        business_age = form_data.get('business_age', None)
        
        if business_age is None:
            self.send_response(400)  # Bad Request
            self.end_headers()
            self.wfile.write(b"Error: 'business_age' is missing")
            return

        # Here you can process the data further, like making decisions based on business_age
        response = {
            "message": "Business age received successfully",
            "business_age": business_age
        }

        # Send a successful response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def do_OPTIONS(self):
        """Handle OPTIONS requests (for CORS)."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """Start the server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
