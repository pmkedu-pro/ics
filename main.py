from ics import Calendar
import requests

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())

def run(server_class=HTTPServer, handler_class=HttpGetHandler):
  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

def load_calendar():
    url = "https://urlab.be/events/urlab.ics"
    c = Calendar(requests.get(url).text)
    e = list(c.timeline)[0]
    "Event '{}' started {}".format(e.name, e.begin.humanize())


def create_calendar():
    c = Calendar()
    e = Event()
    e.name = "My cool event"
    e.begin = '2014-01-01 00:00:00'
    c.events.add(e)


def save_calendar():
    with open('my.ics', 'w') as f:
        f.writelines(c.serialize_iter())

def main():
    run()

if __name__ == "__main__":
    main()
