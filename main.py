import urllib
from urllib import request, parse
from urllib.parse import urlparse, urljoin
from urllib.request import Request
from html.parser import HTMLParser
import re


link = 'http://enigmatic-scrubland-4484.herokuapp.com/'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

print(link)
try:
  req = Request(link, headers={'User-Agent': agent}, method='HEAD')
  status = request.urlopen(req).getcode()
  print(status)
  
except urllib.error.HTTPError as e:
  print(f'HTTPError: {e.code} - {link}')  # (e.g. 404, 501, etc)
except urllib.error.URLError as e:
  print(f'URLError: {e.reason} - {link}')  # (e.g. conn. refused)
except ValueError as e:
  print(f'ValueError {e} - {link}')  # (e.g. missing protocol http)
   # if self.verbose:
   #   print(f'{status} - {link}')
   # if self.home in link:
   #   self.pages_to_check.appendleft(link)

p = re.compile('^\w+')
while True :
  svr_line = req.readline()
  if svr_line:
    if p.match(svr_line):
      c = re.compile(',').split(svr_line)
      ip = c[1]
      country = c[6]
      config_base64 = c[-1]
      config = base64.b64decode(config_base64)
#                print ip, country, config
      print (ip, country)

        # get tcp port from config_file
      p_tcp = re.compile('^proto tcp', re.MULTILINE)
      p_port = re.compile('^remote [.|\d]+ (\d+)', re.MULTILINE)
      if p_tcp.search(config) :
        m_port = p_port.search(config)
        if m_port :
          port = int(m_port.group(1)) # 80 is num, '80' is str, it's different betwen perl and python
#                        print ip, port
          if tcp_port_is_open(ip, port) :
            print ("GOOD: ", ip, port)
            if not country in result :
              result[country] = []
            else :
              result[country].append({'ip':ip, 'config':config})
                            
          else :
            print ("TIMEOUT: ", ip, port)
