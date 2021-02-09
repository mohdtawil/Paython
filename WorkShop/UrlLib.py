import urllib.request as web1
url = input("Please Enter a URL : ")
fp = web1.urlopen(url)

data = str(fp.read())

fp.close()

countNum ={}
for e in data:
    if e in '1234567890':
        if e not in countNum:
            countNum[e] =1
        else:
            countNum[e] +=1

            
print(countNum)
import pprint as ppp
ppp.pprint(countNum)
fp = open('result.txt' , 'a')
ppp.pprint(countNum, stream=fp)
fp.close()
