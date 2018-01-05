import re
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
def validae_url(url):
    if re.match(r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$',url):
        
        req = Request(url)
        try:
            response = urlopen(req)
            code = response.getcode()
            return code
        except HTTPError as code:
            return code
        except URLError as code:
            return code
        else:
            return code
    else:
        return "Invalid URL"


url = input("Enter the url:")
print (validae_url(url))
        