def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'   # python2可不用byte，python3必须要

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]