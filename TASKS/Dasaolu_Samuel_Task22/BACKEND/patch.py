from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = [
    {
        "id": 1,
        "name": "Sam Larry",
        "track": "AI Engineering",
    }
]


class BasicApi(BaseHTTPRequestHandler):
    def send_data(self, data, status=201):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_PATCH(self):
        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)
        patched_data = json.loads(parsed_data)

        if data:
            data[0].update(patched_data)
            self.send_data({
                'Message': 'Data Patched',
                'data': data[0],
            })
        else:
            self.send_data({
                'message': 'Data Not Patched Successfully',
            }, status = 400)

def run(data=None):
    print("Data\n", data)
    HTTPServer(("0.0.0.0", 8080), BasicApi).serve_forever()

while True:
    print("Put Application Running")
    run(data)
