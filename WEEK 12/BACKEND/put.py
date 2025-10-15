from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = []
next_id = 1  # Start our ID counter at 1


class BasicApi(BaseHTTPRequestHandler):
    def send_data(self, payload, status=201):

    # ... (this method is fine) ...

    def do_POST(self):
        global next_id  # Tell the function we are using the global variable

        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)
        post_data = json.loads(parsed_data)

        # --- New Lines ---
        post_data['id'] = next_id  # Add the ID to the received data
        data.append(post_data)
        next_id += 1  # Increment the ID for the next post
        # -----------------

        self.send_data({
            "Message": "Data Received",
            "data": post_data
        })

# ... (rest of your code) ...
