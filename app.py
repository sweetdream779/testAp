
def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = 'Hello world'
    yield response_body.encode()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    from flask import Flask, request, render_template, send_from_directory

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
    #app.run(port=80)
