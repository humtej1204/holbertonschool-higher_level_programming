#!/usr/bin/python3
"""
 displays the value of the X-Request-Id
 variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    r = request.Request(argv[1], data)
    with request.urlopen(r) as r:
        print(r.read().decode('utf-8'))
