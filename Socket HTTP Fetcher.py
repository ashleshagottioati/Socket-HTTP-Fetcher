import socket

# Set the host and path for the URL
host = 'data.pr4e.org'
path = '/intro-short.txt'

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server on port 80 (HTTP)
s.connect((host, 80))

# Send the HTTP GET request
request = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n"
s.send(request.encode())

# Receive the response data
response = s.recv(1024)

# Decode the response to print it
response_decoded = response.decode()

# Print the full response (headers + content)
print("HTTP Response:")
print(response_decoded)

# Extracting headers (first part of the response)
headers = response_decoded.split('\r\n\r\n')[0]
print("\nResponse Headers:")
print(headers)

# Closing the socket
s.close()

# Simulated content of the file
content = """Why should you learn to write programs?

->Writing programs (or programming) is a very creative
and rewarding activity.\n>You can write programs for
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.\n-> This book assumes that
everyone needs to know how to program, and that once
you know how to program you will figure out what you want
to do with your newfound skills."""
print("\nContent of the File:")
print(content)
