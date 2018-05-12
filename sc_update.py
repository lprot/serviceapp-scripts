import urllib2, re, os

list = []

def get(id, key, regex):
	r = re.search(re.compile(regex), h)
	if hasattr(r, 'group'):
		list.append([id, key, r.group(1).replace(' ', '')])
		if id == 'P 010': # for SIS
			list.append(['P 050', key, r.group(1).replace(' ', '')])

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

q = urllib2.Request('http://www.latest-files.com/irdeto-keys.php')
q.add_header('User-Agent', ua)
h = urllib2.urlopen(q).read()
get('I 0604', '04', '060400 04.*?>([0-9A-F ]+)<')
get('I 0604', '06', '060400 06.*?>([0-9A-F ]+)<')

q = urllib2.Request('http://www.latest-files.com/powervu-keys.php')
q.add_header('User-Agent', ua)
h = urllib2.urlopen(q).read()
get('P 030', '00', '12322 V 27500.*?ECMKey0.*?>([0-9A-F ]+)<')
get('P 030', '01', '12322 V 27500.*?ECMKey1.*?>([0-9A-F ]+)<')
get('P 010', '00', '12418-H-27500.*?Keys: 00.*?>([0-9A-F ]+)<')
get('P 010', '01', '12418-H-27500.*?Keys: 01.*?>([0-9A-F ]+)<')

if list:
	#print list
	try: 
		o = open('/usr/keys/SoftCam.new', 'w')
		for line in open('/usr/keys/SoftCam.Key').readlines():
			no_match = True
			for x in list:
				r = re.search(re.compile('^' + x[0] + '(.*?)( ' + x[1] + ' ).*?([0-9A-F]*)(.*)'), line)
				if hasattr(r, 'group'):
					o.write(x[0] + r.group(1) + ' ' + x[1] + ' ' + x[2] + r.group(4) + '\n')
					no_match = False
					break
			if no_match:
				o.write(line)
		o.close()
		os.rename('/usr/keys/SoftCam.Key', '/usr/keys/SoftCam.old')
		os.system('/etc/init.d/softcam restart') 
		os.rename('/usr/keys/SoftCam.new', '/usr/keys/SoftCam.Key')
	except:
		pass
