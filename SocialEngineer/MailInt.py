
#Copy from github:https://github.com/vysec/MaiInt/edit/master/MaiInt.py
import os,sys,urllib2,urllib,argparse,json,re,requests,csv,codecs
from string import digits

MAIINT_ORGANISATION_CHINESE = ""
MAIINT_ORGANISATION_PINYIN = ""
MAIINT_ORGANISATION_ENCODE = ""
MAIINT_ORGANISATION_ENCODE_BRACES = ""

MAIINT_PROJECT_NAME = ""
MAIINT_ORGANISATION_SUFFIX = ""
MAIINT_ORGANISATION_PREFIX = "lastfirst"
MAIINT_ORGANISATION_TOTAL_COUNT = 0

###   CONFIGURATION   ###

# The following variables can be modified as required

MAIINT_COUNT = 5000
MAIINT_PAGE = 0
MAIINT_COUNT_SET = False
MAIINT_USERAGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153/{iPhone10,4} [iOS 11.2.1]/MaiMai 4.18.0(4.18.0.4)"

# The following variables can be modified as required for authentication
# Phone number must be CC-NNNNNNNNNN (cc: country code, nn: number)
MAIINT_PHONE_NUMBER = "+44-NNNNNNNNNN"
MAIINT_PASSWORD = "000000"

MAIINT_ACCESS_TOKEN = ""
MAIINT_USERID = ""
HUNTER_API_KEY = "YOURKEYHERE"

### CONFIGURATION END ###

def banner():
	print """  __  __    _    ___ ___ _   _ _____ 
 |  \/  |  / \  |_ _|_ _| \ | |_   _|
 | |\/| | / _ \  | | | ||  \| | | |  
 | |  | |/ ___ \ | | | || |\  | | |  
 |_|  |_/_/   \_\___|___|_| \_| |_|  
                                     """
	print "MaiInt V%s" % MAIINT_VERSION
	print "Author: %s (%s)" % (MAIINT_AUTHOR, MAIINT_AUTHOR_TWITTER)


def getPinyin(chinese):
	print chinese
	return pinyin.get(chinese)

def login():
	global MAIINT_PHONE_NUMBER
	global MAIINT_PASSWORD
	global HUNTER_API_KEY
	global MAIINT_ACCESS_TOKEN
	global MAIINT_USERID

	if MAIINT_PHONE_NUMBER == "" or MAIINT_PASSWORD == "" or HUNTER_API_KEY == "":
		print "[!] Please edit the script and insert your MAIMAI Phone number, password and Hunter API Key!"
		exit()
	else:
		if "-" in MAIINT_PHONE_NUMBER and "+" in MAIINT_PHONE_NUMBER:
			# begin login process
			url = "https://open.taou.com/maimai/user/v3/login?account=%s&password=%s" % (urllib.quote_plus(MAIINT_PHONE_NUMBER),MAIINT_PASSWORD)

			f = urllib2.urlopen(url)
		
			json_login_res = f.read()
			json_login = json.loads(json_login_res)

			try:
				MAIINT_ACCESS_TOKEN = json_login["token"]
				MAIINT_USERID = json_login["user"]["id"]
			except:
				print "[!] Login error!"
				exit()

			if MAIINT_ACCESS_TOKEN != "" and MAIINT_USERID != "":
				print "[*] Access Token: %s" % MAIINT_ACCESS_TOKEN
				print "[*] User ID: %s" % MAIINT_USERID
			else:
				print "[!] Login error!"
				exit()
		else:
			print "[!] Invalid phone number? Make sure it starts with + and has a - between country code and number"


def arguments():
	# python MaiInt.py <target>
	global MAIINT_COUNT
	global MAIINT_ORGANISATION_ENCODE
	global MAIINT_PROJECT_NAME
	global MAIINT_ORGANISATION_SUFFIX
	global MAIINT_ORGANISATION_PREFIX
	global MAIINT_COUNT_SET
	global MAIINT_ORGANISATION_TOTAL_COUNT
	global MAIINT_PAGE
	global MAIINT_ORGANISATION_ENCODE_BRACES
	global MAIINT_ACCESS_TOKEN
	global MAIINT_USERID

	if len(sys.argv) > 1:
		if len(sys.argv) == 3:
			MAIINT_COUNT = sys.argv[2]
			MAIINT_ORGANISATION_CHINESE = sys.argv[1]
			MAIINT_COUNT_SET = True
		elif len(sys.argv) == 2:
			# correct
			MAIINT_ORGANISATION_CHINESE = sys.argv[1]
	else:	# Ask for target company name in Pinyin
		MAIINT_ORGANISATION_CHINESE = raw_input("[!] Please specify a target name (in Chinese): ")

	if MAIINT_ORGANISATION_CHINESE != "":
		#print "[*] TARGET ORGANISATION PINYIN NAME: %s" % (MAIINT_ORGANISATION_CHINESE)
		MAIINT_ORGANISATION_ENCODE = chinese_urlencode(MAIINT_ORGANISATION_CHINESE)
		MAIINT_ORGANISATION_ENCODE_BRACES = chinese_urlencode("[\"%s\"]" % MAIINT_ORGANISATION_CHINESE) 
		#print "[*] URLENCODE: %s" % MAIINT_ORGANISATION_ENCODE
	else:
		print "[!] You need to enter a target organisation name in Chinese format!"
		exit()

	MAIINT_PROJECT_NAME = raw_input("[*] Project Name: ")
	while True:
		MAIINT_ORGANISATION_SUFFIX = raw_input("[*] Enter e-mail domain suffix (eg. contoso.com): ").lower()
		if "." in MAIINT_ORGANISATION_SUFFIX:
			break
		else:
			print "[!] Incorrect domain name? There's no dot character"

	while True:
		MAIINT_ORGANISATION_PREFIX = raw_input("[*] Select a prefix for e-mail generation (auto,full,firstlast,firstmlast,flast,first.last,fmlast,lastfirst): \n").lower()
		if MAIINT_ORGANISATION_PREFIX == "full" or MAIINT_ORGANISATION_PREFIX == "firstlast" or MAIINT_ORGANISATION_PREFIX == "firstmlast" or MAIINT_ORGANISATION_PREFIX == "flast" or MAIINT_ORGANISATION_PREFIX =="first" or MAIINT_ORGANISATION_PREFIX == "first.last" or MAIINT_ORGANISATION_PREFIX == "fmlast" or MAIINT_ORGANISATION_PREFIX == "lastfirst":
			break
		elif MAIINT_ORGANISATION_PREFIX == "auto":
			#if auto prefix then we want to use hunter IO to find it.
			print "[*] Automaticly using Hunter IO to determine best Prefix"
			url = "https://hunter.io/trial/v2/domain-search?offset=0&domain=%s&format=json" % MAIINT_ORGANISATION_SUFFIX
			r = requests.get(url)
			content = json.loads(r.text)
			if "status" in content:
				print "[!] Rate limited by Hunter IO trial"
				url = "https://api.hunter.io/v2/domain-search?domain=%s&api_key=%s" % (MAIINT_ORGANISATION_SUFFIX, HUNTER_API_KEY)
				#print url
				r = requests.get(url)
				content = json.loads(r.text)
				if "status" in content:
					print "[!] Rate limited by Hunter IO Key"
					continue
			#print content
			MAIINT_ORGANISATION_PREFIX = content['data']['pattern']
			print "[!] %s" % MAIINT_ORGANISATION_PREFIX
			if MAIINT_ORGANISATION_PREFIX:
				MAIINT_ORGANISATION_PREFIX = MAIINT_ORGANISATION_PREFIX.replace("{","").replace("}", "")
				if MAIINT_ORGANISATION_PREFIX == "full" or MAIINT_ORGANISATION_PREFIX == "firstlast" or MAIINT_ORGANISATION_PREFIX == "firstmlast" or MAIINT_ORGANISATION_PREFIX == "flast" or MAIINT_ORGANISATION_PREFIX =="first" or MAIINT_ORGANISATION_PREFIX == "first.last" or MAIINT_ORGANISATION_PREFIX == "fmlast" or MAIINT_ORGANISATION_PREFIX == "lastfirst":
					print "[+] Found %s prefix" % MAIINT_ORGANISATION_PREFIX
					break
				else:
					print "[!] Automatic prefix search failed, please insert a manual choice"
					continue
			else:
				print "[!] Automatic prefix search failed, please insert a manual choice"
				continue
		else:
			print "[!] Incorrect choice, please select a value from (full,firstlast,firstmlast,flast,first.last,fmlast,lastfirst)"

	print 

	url = "https://maimai.cn/search/contacts?access_token=%s&u=%s&count=0&page=0&query=%s&searchTokens=%s&jsononly=1&frm=webview#/search/contacts" % (MAIINT_ACCESS_TOKEN, MAIINT_USERID, MAIINT_ORGANISATION_ENCODE, MAIINT_ORGANISATION_ENCODE_BRACES)

	f = urllib2.urlopen(url)

	json_users_res = f.read()
	json_users = json.loads(json_users_res)

	if "error" in json_users["result"]:
		print "[!] The account is rate limited by MaiMai, please wait and try again later"
		exit()
		#"[!] The account is rate limited"

	#print json_users
	
	MAIINT_ORGANISATION_TOTAL_COUNT = int(json_users["data"]["more"])
	
		
	print "[*] Total number of users found: %s" % MAIINT_ORGANISATION_TOTAL_COUNT

	if MAIINT_COUNT_SET == False:
		while True:
			MAIINT_COUNT = int(raw_input("[*] How many records would you like to request?: "))
			if MAIINT_COUNT <= MAIINT_ORGANISATION_TOTAL_COUNT:
				MAIINT_COUNT_SET = True
				break
			else:
				print "[!] Count requested cannot be more than total available!"

	if MAIINT_COUNT_SET == True:
		while True:
			MAIINT_PAGE = int(raw_input("[*] From what page would you like to request the %s records? (Enter 0 for beginning): " % MAIINT_COUNT))
			pageval = MAIINT_COUNT * MAIINT_PAGE
			if (pageval + MAIINT_COUNT) <= MAIINT_ORGANISATION_TOTAL_COUNT:
				print "[*] Requesting records %s to %s of %s" % (pageval, pageval+MAIINT_COUNT, MAIINT_ORGANISATION_TOTAL_COUNT)
				break
			else:
				print "[!] The page number you requested is invalid as it places the requested items above the total available!"


def to_utf8(text):
	if isinstance(text, unicode):
		# unicode to utf-8
		return text.encode('utf-8')
	try:
		# maybe utf-8
		return text.decode('utf-8').encode('utf-8')
	except UnicodeError:
		# gbk to utf-8
		return text.decode('gbk').encode('utf-8')

def request_users(count, query):
	# https://maimai.cn/search/contacts?count=100&page=1&query=jingdong&dist=1000&cid=&company=&forcomp=0&searchTokens=%5B%22%E4%BA%AC%E4%B8%9C%22%5D&highlight=true&school=&profession=&major=&province=&city=&me=1&jsononly=1&frm=webview%23%2Fsearch%2Fcontacts

	# Cookie: access_token=1.158e8ebfcb18e3e284c4a27f4744feb2; u=140271776;
	# User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153/{iPhone10,4} [iOS 11.2.1]/MaiMai 4.18.0(4.18.0.4)


	# First grab to see how many results there are in total
	global MAIINT_COUNT_SET
	global MAIINT_COUNT
	global MAIINT_ORGANISATION_PREFIX
	global MAIINT_ORGANISATION_TOTAL_COUNT

	# https://maimai.cn/search/contacts?query=%E4%BA%AC%E4%B8%9C&dist=3&searchTokens=%5B%22%E4%BA%AC%E4%B8%9C%22%5D&me=1&highlight=true&frm=webview%23%2Fsearch%2Fcontacts&appid=4&vc=11.2.1&push_permit=1&version=4.18.0&channel=AppStore&net=wifi&jsononly=1&imei=6468899B-1E82-4635-9DB2-FEA6B2443080&open=icon&density=2&u=140271776&device=iPhone10%2C4&access_token=1.158e8ebfcb18e3e284c4a27f4744feb2&ts=1514374514503

	if MAIINT_COUNT_SET == False:
		url = "https://maimai.cn/search/contacts?access_token=%s&u=%s&count=%s&page=0&query=%s&searchTokens=%s&jsononly=1&frm=webview#/search/contacts" % (MAIINT_ACCESS_TOKEN, MAIINT_USERID, MAIINT_ORGANISATION_TOTAL_COUNT, query, MAIINT_ORGANISATION_ENCODE_BRACES)
		print "[*] Requesting all %s Users!" % MAIINT_ORGANISATION_TOTAL_COUNT
	else:
		count = min(int(count),int(MAIINT_ORGANISATION_TOTAL_COUNT))
		url = "https://maimai.cn/search/contacts?access_token=%s&u=%s&count=%s&page=0&query=%s&searchTokens=%s&jsononly=1&frm=webview#/search/contacts" % (MAIINT_ACCESS_TOKEN, MAIINT_USERID, count, query, MAIINT_ORGANISATION_ENCODE_BRACES)
		print "[*] Requesting %s Users!" % (MAIINT_COUNT)
	
	#print url

	f = urllib2.urlopen(url)

	json_users_res = f.read()
	json_users = json.loads(json_users_res)

	return json_users

def chinese_urlencode(chinese):
	return urllib.quote(to_utf8(chinese))

def parse_users(jsonObj):
	### TO BE IMPLEMENTED!!! ###
	print "[*] Parsing Users"
	print "Found %s users" % len(jsonObj["data"]["contacts"])

	items = []

	for a in jsonObj["data"]["contacts"]:
		# print a["contact"]["avatar"]
		# item = avatar, py, name, title, city, company
		item = (a["contact"]["avatar"], a["contact"]["py"], a["contact"]["name"], a["contact"]["position"], a["contact"]["city"], a["contact"]["company"])
		items.append(item)
	return items

def write_html(parsedUsers):

	global MAIINT_PROJECT_NAME
	global MAIINT_ORGANISATION_SUFFIX
	global MAIINT_ORGANISATION_PREFIX

	prefix = MAIINT_ORGANISATION_PREFIX
	#prefix = "lastfirst"
	suffix = MAIINT_ORGANISATION_SUFFIX

	#csv = []
	body = ""

	css = """<style>
	#employees {
		font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
		border-collapse: collapse;
		width: 100%;
	}

	#employees td, #employees th {
		border: 1px solid #ddd;
		padding: 8px;
	}

	#employees tr:nth-child(even){background-color: #f2f2f2;}

	#employees tr:hover {background-color: #ddd;}

	#employees th {
		padding-top: 12px;
		padding-bottom: 12px;
		text-align: left;
		background-color: #4CAF50;
		color: white;
	}
	</style>

	"""

	header = """<center><table id=\"employees\">
	<tr>
	<th>Photo</th>
	<th>Name</th>
	<th>Email</th>
	<th>Job</th>
	<th>Company</th>
	<th>Location</th>
	</tr>
	"""

	foot = "</table></center>"

	# EACH USER
	outfile = MAIINT_PROJECT_NAME

	print "[*] Writing CSV Report to %s.csv" % outfile
	f = open('{}.csv'.format(outfile), 'wb')
	f.write(codecs.BOM_UTF8)
	w = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
	w.writerow(["First Name".encode('utf-8'),"Last Name".encode('utf-8'),"Position".encode('utf-8'),"Email".encode('utf-8')])

	for i in parsedUsers:
	# item = avatar, py, name, title, city, company
		py = re.sub(r'[^\x00-\x7F]+',' ', i[1])
		py = re.sub(r'[0-9]+', '', py)
		parts = py.split()

		fname = ""
		mname = ""
		lname = ""

		if len(parts) == 4:
			fname = parts[2]
			mname = parts[3]
			lname = parts[0] + parts[1]

		elif len(parts) == 3:
			fname = parts[1]
			mname = parts[2]
			lname = parts[0]

		elif len(parts) == 2:
			fname = parts[1]
			lname = parts[0]
		elif len(parts) == 1:
			fname = parts[0]
		
		fname = re.sub('[^A-Za-z]+', '', fname)
		mname = re.sub('[^A-Za-z]+', '', mname)
		lname = re.sub('[^A-Za-z]+', '', lname)

		if len(fname) == 0 or len(lname) == 0:
			continue

		if prefix == "full":
			user = '{}{}{}'.format(fname,mname,lname)
		if prefix == "firstlast":
			user = '{}{}{}'.format(fname,mname,lname)
		if prefix == "firstmlast":
			if len(mname) == 0:
				user = '{}{}{}'.format(fname, mname, lname)
			else:
				user = '{}{}{}'.format(fname, mname[0], lname)
		if prefix == "flast":
			user = '{}{}'.format(fname[0], lname)
		if prefix == "first.last":
			user = '{}{}.{}'.format(fname,mname,lname)
		if prefix == "fmlast":
			if len(mname) == 0:
				user = '{}{}{}'.format(fname[0], mname, lname)
			else:
				user = '{}{}{}'.format(fname[0], mname[0], lname)
		if prefix == "lastfirst":
			user = '{}{}{}'.format(lname,fname,mname)

		email = '{}@{}'.format(user,suffix)

		body += "<tr>" \
		"<td><img src=\"%s\" width=200 height=200></td>" \
		"<td>%s</td>" \
		"<td>%s</td>" \
		"<td>%s</td>" \
		"<td>%s</td>" \
		"<td>%s</td>" \
		"<a>" % (i[0], i[2], email, i[3], i[5], i[4])

		w.writerow([i[2].encode('utf-8'),i[4].encode('utf-8'),i[3].encode('utf-8'),email])
	
	f.close()			

	print "[*] Writing HTML Report to %s.html" % outfile


	f = open('{}.html'.format(outfile), 'wb')
	f.write(css)
	f.write(header)
	f.write(body.encode('utf-8'))
	f.write(foot)
	f.close()
	
	
	return

def write_csv(parsedUsers):
	### TO BE IMPLEMENTED!!! ###
	print "[*] Writing CSV Report"
	return

def write_reports(parsedUsers):
	### TO BE IMPLEMENTED!!! ###
	write_html(parsedUsers)
	#write_csv(parsedUsers)




if __name__ == "__main__":
	banner()
	login()
	arguments()

	jsonUsers = request_users(MAIINT_COUNT, MAIINT_ORGANISATION_ENCODE)
	parsedUsers = parse_users(jsonUsers)
	write_reports(parsedUsers)
