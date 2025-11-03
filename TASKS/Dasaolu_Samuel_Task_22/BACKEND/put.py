from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Sample data to act as a simple in-memory database
data = [
    {"id": 1, "name": "Sam Larry", "track": "AI Developer"},
    {"id": 2, "name": "Jane Doe", "track": "Frontend Developer"}
]


class BasicApi(BaseHTTPRequestHandler):
    def send_json_response(self, payload, status=200):
        """Sends a JSON response."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_PUT(self):
        """Handles PUT requests to update existing data."""
        try:
            # Extract the ID from the path, e.g., /1
            path_parts = self.path.strip("/").split("/")
            if len(path_parts) != 1 or not path_parts[0].isdigit():
                self.send_json_response({"error": "Invalid ID in path. Use /<id>"}, status=400)
                return

            item_id = int(path_parts[0])

            # Find the item to update
            item_to_update = None
            for i, item in enumerate(data):
                if item.get("id") == item_id:
                    item_to_update = (i, item)
                    break

            if item_to_update is None:
                self.send_json_response({"error": f"Item with id {item_id} not found"}, status=404)
                return

            # Read and parse the incoming JSON data
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            update_payload = json.loads(post_data)

            # Update the data in our list
            item_index = item_to_update[0]
            data[item_index].update(update_payload)

            # Send a success response
            self.send_json_response({
                "message": "Data updated successfully",
                "data": data[item_index]
            })

        except json.JSONDecodeError:
            self.send_json_response({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            self.send_json_response({"error": f"An error occurred: {e}"}, status=500)


def run(server_class=HTTPServer, handler_class=BasicApi, port=8000):
    """Starts the HTTP server."""
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"PUT Application is running on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
