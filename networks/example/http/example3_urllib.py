from urllib import request


response = request.urlopen('http://example.com')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
print(response.headers)
print(response.getheaders())
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))
