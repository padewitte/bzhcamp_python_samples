import os
import requests

__author__ = 'padewitte'

if __name__ == '__main__':
    r = requests.get('https://pypi.python.org/pypi/requests/json', auth=('user', 'pass'))
    print(r.status_code)
    print(r.headers['content-type'])
    os.system("pause")
    print(r.text)
    os.system("pause")
    print(r.json()['releases']['1.0.4 '])