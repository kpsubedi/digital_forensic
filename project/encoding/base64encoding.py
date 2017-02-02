import base64

encoded = base64.b64encode('welcome to forensic')

print encoded


decoded = base64.b64decode(encoded)

print decoded 

