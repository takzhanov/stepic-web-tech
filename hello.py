def app(environ, start_response):
    s = ""

    for i in environ['QUERY_STRING'].split("&"):
        s = s + i + "\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(s)))
    ])
    return iter([s])
