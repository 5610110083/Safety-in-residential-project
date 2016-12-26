#!/usr/bin/python 
print("Content-type: text/html") 
print("")  
print("<html><head>") 
print("") 
print("</head><body>") 
print("Hello from Python.") 



infile = r"alert.log" 
with open(infile) as f:
    f = f.readlines()

def readLog():
  for line in f:
      line = '<p>'+line+'</p>'
      print line

readLog()

print("</body></html>") 
