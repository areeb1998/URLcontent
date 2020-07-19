import requests as req
cont = req.get('https://www.google.com/search?q=python+install&oq=&aqs=chrome.0.69i59l3.1280290j0j7&sourceid=chrome&ie=UTF-8')
filed = open("areeba.rtf", "w")
filed.write(cont.text)
filed.close()

filed = open("areeba.rtf", "r")
print(filed.read())
