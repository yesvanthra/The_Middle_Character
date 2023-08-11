import re
def stringsplittingwithdelimiter(text, delimiters):
    result=re.findall('[^%s]+' % re.escape(delimiters), text)
    print(result)
stringsplittingwithdelimiter("sdfkdjsadfsd diweiw;1231:foo", ' ;:')