#!C:/Users/1chi/AppData/Local/Microsoft/WindowsApps/python.exe
import codecs
import json
import os
import sys
import urllib.parse

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

envsUl =  "<ul>" + ''.join("<li>%s = %s</li>" % (k,v) for k,v in os.environ.items()) + "</ul>"

envs = {
    k: v for k, v in os.environ.items()
    if k in ('REQUEST_METHOD', 'QUERY_STRING', 'REQUEST_URI')
}

headers = {
    (k[5:] if k.startswith('HTTP_') else k).lower().replace("_", "-"): v
    for k, v in os.environ.items()
    if k.startswith('HTTP_') or k in ('CONTENT_TYPE', 'CONTENT_LENGTH')
}

query_string = urllib.parse.unquote(envs['QUERY_STRING'], encoding="utf-8")
query_parameters = dict(
    pair.split('=', maxsplit=1) if '=' in pair else (pair, None)
    for pair in query_string.split('&') if pair
)

body_parameters = {}
body = sys.stdin.read()

def send_error(code=400, phrase="Bad Request", explain=None):
    print(f"Status: {code} {phrase}")
    print("Access-Control-Allow-Origin: *")
    print("Content-Type: text/plain; charset=utf-8")
    print()
    print(explain if explain else phrase)
    exit()

def parse_multipart_form_data(body, content_type):
    """Parses multipart/form-data."""
    boundary = "--" + content_type.split("boundary=")[1]
    parts = body.split(boundary)
    parts = parts[1:-1]
    parsed_data = {}

    for part in parts:
        if not part.strip():
            continue
        headers, content = part.split("\r\n\r\n", maxsplit=1)
        content = content.rstrip("\r\n")

        # Parse headers
        headers_dict = {}
        for header_line in headers.split("\r\n"):
            if ": " in header_line:
                key, value = header_line.split(": ", maxsplit=1)
                headers_dict[key.lower()] = value

        # Extract field name from Content-Disposition
        disposition = headers_dict.get("content-disposition", "")
        if "name=" in disposition:
            field_name = disposition.split('name="')[1].split('"')[0]
            parsed_data[field_name] = content

    return parsed_data

if body:
    content_type = headers.get('content-type', '')
    if content_type == 'application/json':
        try:
            body_parameters = json.loads(body)
        except json.JSONDecodeError:
            send_error(400, "Bad Request", "Invalid JSON format")
    elif content_type == 'application/x-www-form-urlencoded':
        body_parameters = dict(
            pair.split('=', maxsplit=1)
            for pair in urllib.parse.unquote(body).split('&') if '=' in pair
        )
    elif content_type.startswith('multipart/form-data'):
        body_parameters = parse_multipart_form_data(body, content_type)
    else:
        send_error(415, "Unsupported Media Type",
                   "Supported types: application/json, application/x-www-form-urlencoded, multipart/form-data")




def parse_multipart_form_data(body, content_type):
    """Parses multipart/form-data."""
    boundary = "--" + content_type.split("boundary=")[1]
    parts = body.split(boundary)
    parts = parts[1:-1]
    parsed_data = {}

    for part in parts:
        if not part.strip():
            continue
        headers, content = part.split("\r\n\r\n", maxsplit=1)
        content = content.rstrip("\r\n")

        # Parse headers
        headers_dict = {}
        for header_line in headers.split("\r\n"):
            if ": " in header_line:
                key, value = header_line.split(": ", maxsplit=1)
                headers_dict[key.lower()] = value

        # Extract field name from Content-Disposition
        disposition = headers_dict.get("content-disposition", "")
        if "name=" in disposition:
            field_name = disposition.split('name="')[1].split('"')[0]
            parsed_data[field_name] = content

    return parsed_data



path = envs['REQUEST_URI']
if '?' in path:
    path = path[:path.index('?')]


print("Content-Type: applicatin/json; charset=utf-8")
#print("Content-Type: text/html; charset=utf-8")
print()
#print(json.dumps(headers), end="")
print(json.dumps(body_parameters,ensure_ascii=False), end="")
#print(envsUl, end="")

