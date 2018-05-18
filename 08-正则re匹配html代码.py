import re
s = '<html><head><title>Title<p><h2>hello word</h2></p></title></head></html>'
reg = re.compile(r"<title>(.*?)<p><h2>(.*?).*?")
# print(reg.findall(s))

print(s)
print(re.match(r'<.*>',s))
print(re.match(r'<.*?>',s))