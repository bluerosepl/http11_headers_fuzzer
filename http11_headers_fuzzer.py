import requests
import random

#############
####const####
#############
iterations = 1000
ip = "10.10.10.10"

#############
##variables##
#############
headers_list = {
    "Accept":"",
    "Accept-Charset":"",
    "Accept-Encoding":"",
    "Accept-Language":"",
    "Accept-Datetime":"",
    "Authorization":"",
    "Cache-Control":"",
    "Connection":"",
    "Cookie":"",
    "Content-Length":"",
    "Content-MD5":"",
    "Content-Type":"",
    "Date":"",
    "Expect":"",
    "Forwarded":"",
    "From":"",
#    "Host":"",
    "If-Match":"",
    "If-Modified-Since":"",
    "If-None-Match":"",
    "If-Range":"",
    "If-Unmodified-Since":"",
    "Max-Forwards":"",
    "Origin":"",
    "Pragma":"",
    "Proxy-Authorization":"",
    "Range":"",
    "Referer":"",
    "TE":"",
    "User-Agent":"",
    "Upgrade":"",
    "Via":"",
    "Warning":"",
    "X-Requested-With":"",
    "DNT":"",
    "X-Forwarded-For":"",
    "X-Forwarded-Host":"",
    "X-Forwarded-Proto":"",
    "Front-End-Https":"",
    "X-Http-Method-Override":"",
    "X-ATT-DeviceId":"",
    "X-Wap-Profile":"",
    "Proxy-Connection":"",
    "X-UIDH":"",
    "X-Csrf-Token":"",
    "X-Request-ID":"",
    "X-Correlation-ID":""
}

for iteration_numner in range(1,iterations):
    #how many headers should we pick
    headers_count = random.randint(1,len(headers_list))
    #pick a headers to send
    headers_final = random.sample(headers_list, headers_count)
    headers_dict = {}
    #send loop
    for j in headers_final:
        #build random payload
        my_rand = ""
        bytes_count = random.randint(1,100)
        bytes_list=[]
        for i in range(bytes_count):
            bytes_list.append(random.randint(31,255))

        my_rand = my_rand.join(map(chr, bytes_list))
        #eo build random payload
        headers_dict[j] = my_rand
    url = "http://"+str(ip)+"?iteration="+str(iteration_numner)
    r = requests.get(url, headers = headers_dict)
    print r.status_code, len(r.content)
