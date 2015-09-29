#import util
import codecs
import json
import requests



r1 = requests.get('http://paste.ee/r/laxjw')
if r1.status_code:
    
    str_cc=r1.json()
   # print type(str_cc)
    count = 0
    count_ver = 0
    
    for people in str_cc:
        if people['creditcard']:
            count_ver +=1
            print people['name'] + ',' + people['creditcard']
        count +=1
   
    print 'count_total    :' + str(count) 
    print 'count_processed:' + str(count_ver)
