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

    def do_DELETE(self):
        """Handles DELETE requests to remove data."""
        try:
            # Extract the ID from the path, e.g., /1
            path_parts = self.path.strip("/").split("/")
            if len(path_parts) != 1 or not path_parts[0].isdigit():
                self.send_json_response({"error": "Invalid ID in path. Use /<id>"}, status=400)
                return

            item_id = int(path_parts[0])

            # Find the item to delete
            item_to_delete = None
            for i, item in enumerate(data):
                if item.get("id") == item_id:
                    item_to_delete = i
                    break

            if item_to_delete is None:
                self.send_json_response({"error": f"Item with id {item_id} not found"}, status=404)
                return

            # Remove the item from the list
            deleted_item = data.pop(item_to_delete)

            # Send a success response
            self.send_json_response({
                "message": "Data deleted successfully",
                "deleted_item": deleted_item
            })

        except Exception as e:
            self.send_json_response({"error": f"An error occurred: {e}"}, status=500)


def run(server_class=HTTPServer, handler_class=BasicApi, port=8000):
    """Starts the HTTP server."""
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"DELETE Application is running on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
