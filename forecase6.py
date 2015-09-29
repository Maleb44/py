    #Budapest


#s = 'valami {a},{b}-{d}////{c}'
#s.format(a=1,b=5, c='valami', d= {b}

import requests
import json
import pylab

## 47.562129, 19.045849
#latitude = 47.53
#logitude = 19.05
# Kazal
latitude = 47.562129
logitude = 19.045849

apikey='42da0dc3bcc494d1981a501f9415a5e0'

url_template = 'https://api.forecast.io/forecast/{api}/{lat},{lon}'


url = url_template.format(api=apikey,lat=latitude,lon=logitude)
print url




par ={'units': 'si'}
print par['units']
r = requests.get(url,params=par)

print r.ok
d_in = r.json()
d_daily = d_in ['daily']
d_data  = d_daily['data']


def temp():
    l_plot_min=[]
    l_plot_max=[]
    for elem in d_data:    
    
 #   print 'Min homerseklet: ' + str(elem['temperatureMin'])
 #   print 'Max homerseklet: ' + str(elem['temperatureMax'])
        l_plot_min.append(elem['temperatureMin'])
        l_plot_max.append(elem['temperatureMax'])
    print l_plot_min
    print l_plot_max
    
    pylab.plot(l_plot_min,label = 'min temp')
    pylab.plot(l_plot_max,label = 'max temp')
    pylab.xlabel('time (day )')
    pylab.ylabel('degree (C)')
    pylab.legend()
    pylab.title('Min/max temperature forcase')
temp()
pylab.savefig("TempMaxMin.png")
pylab.grid()
pylab.show()
print 'Vege'
