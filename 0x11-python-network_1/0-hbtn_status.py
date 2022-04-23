#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://intranet.hbtn.io/status') as ul:
        html = ul.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
