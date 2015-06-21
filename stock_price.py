import pycurl
import StringIO

curl = pycurl.Curl()
curl.setopt(pycurl.URL, "http://hq.sinajs.cn/list=sh601006")

string = StringIO.StringIO()
curl.setopt(pycurl.WRITEFUNCTION,string.write)
curl.setopt(pycurl.FOLLOWLOCATION, 1)

curl.perform()
print curl.getinfo(pycurl.EFFECTIVE_URL)
html = string.getvalue();
#print html