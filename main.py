'''Socket Programming in Python'''

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# equivalent to `ping www.github.com`
ip = socket.gethostbyname('www.github.com')
print(ip)