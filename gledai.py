import urllib2, re, sys
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
r = 'http://www.bg-gledai.tv/new/geto2.php?my=' + sys.argv[1]
h = 'www.bg-gledai.tv'
q = urllib2.Request(r)
q.add_header('Host', h)
q.add_header('Referer', 'http://' + sys.argv[2])
q.add_header('User-Agent', ua)
s = urllib2.unquote(re.search(r"unescape\(\'(.*?)\'", urllib2.unquote(urllib2.urlopen(q).read())).group(1))
q = urllib2.Request(s)
q.add_header('Host', h)
q.add_header('Referer', r)
q.add_header('User-Agent', ua)
s = re.search(r"file>(.*?)<", urllib2.urlopen(q).read()).group(1).replace('&amp;','&')
print str(s) + '#Origin=http%3a//www.bg-gledai.tv&Referer=' + r.replace(':','%3a') + '&User-Agent=' + ua
