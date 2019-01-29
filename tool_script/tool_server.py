#encoding=utf-8
#!/usr/bin/python
from ip_tool  import int2ip, ip2int 
from tornado.escape import json_encode, json_decode
import tornado.ioloop
import tornado.web
import sys
import json
from datetime import datetime

class IPHandler(tornado.web.RequestHandler):
    def post(self):
        params = json_decode(self.request.body)
        ip = params.get("ip")
        if ip:
            dd = {'integer': ip2int(ip)}
            self.write(dd)
        else:
            integer = params.get("integer")
            print integer
            dd = {'ip': int2ip(integer)}
            self.write(dd)


application = tornado.web.Application([
    (r"/api/ip", IPHandler),
])

if __name__ == "__main__":
    print 'starting....'
    port = 6060
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
