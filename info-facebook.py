""" 
-------------------------------------------------------------------------
- Cod BY : Rocky
- Github : https://github.com/Rocky-Cracker
- Telegram: https://t.me/ROCKYCRACKER
- Telegram: https://t.me/ROCKYCRACKER
-------------------------------------------------------------------------
     
""" 
try:
	import os,sys,time,requests,json
	from time import sleep
except ImportError:
	os.system('pip install requests')
	
	
A = "\033[1;81m"
B = "\033[1;80m"
C = "\033[1;87m"
E = "\033[1;82m"
H = "\033[1;83m"
K = "\033[1;84m"
L = "\033[1;85m"

def baner():
    banera = """ 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : ROCKY
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : @ROCKYCRACKER
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : ROCKY CRACKER
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/ROCKY-CRACKER\033[1;91m
 ---------------------------
""" 

    for sidra in banera.splitlines():
        time.sleep(0.05)
        print(sidra)


def clear():
	if os.name == 'nt':
		os.system('cls')
		os.system('title Cod BY Rocky Cracker ')
	else:
		os.system('clear')
		
def Facebook():
	clear()
	baner()
	TK = input(E+"("+C+"⌯"+E+") "+C+"TOKEN BOT DANE :"+B)
	ID = input(E+"("+C+"⌯"+E+") "+C+"ID TELEGRAM DANE :"+B)
	clear()
	baner()
	token = input(E+"("+C+"⌯"+E+") "+C+"TOKEN FACEBOOK :"+B)
	id = input(E+"("+C+"⌯"+E+") "+C+"ID FACEBOOK INFO :"+B)
	print (E)
	friends = []
	try:
		max = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id, token))
		sidra = (max.json())
		name = (sidra['name'])
	except (KeyError, IOError):
		name = False
	except: pass
	try:
		first_name = (sidra['first_name'])
	except (KeyError, IOError):
		first_name = False
	except: pass
	try:
		last_name = (sidra['last_name'])
	except (KeyError, IOError):
		last_name = False
	except: pass
	try:
		username = (sidra['username'])
	except (KeyError, IOError):
		username = False
	except: pass
	try:
		email = (sidra['email'])
	except (KeyError, IOError):
		email = False
	except: pass
	try:
		phone = (sidra['mobile_phone'])
	except (KeyError, IOError):
		phone = False
	except: pass
	try:
		date = (sidra['birthday'])
	except (KeyError, IOError):
		date = False
	except: pass
	try:
		gender = (sidra['gender'])
	except (KeyError, IOError):
		gender = False
	except: pass
	try:
		link = (sidra['link'])
	except (KeyError, IOError):
		link = False
	except: pass
	try:
		relationship_status = (sidra['relationship_status'])
	except (KeyError, IOError):
		relationship_status = False
	except: pass
	try:
		bio = (sidra['about'])
	except (KeyError, IOError):
		bio = False
	except: pass
	try:
		hometown = (sidra['hometown']['name'])
	except (KeyError, IOError):
		hometown = False
	except: pass
	try:
		stay = (sidra['location']['name'])
	except (KeyError, IOError):
		stay = False
	except: pass
	try:
		timezone = (sidra['timezone'])
	except (KeyError, IOError):
		timezone = False
	except: pass
	try:
		updated_time = (sidra['updated_time'])
		
	except (KeyError, IOError):
		updated_time = False
	except: pass
	try:
		sida = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(id, token))
		xam = (sida.json())
		for i in xam['data']:
			friends.append(i['id'])
		
	except: pass
	try:
		r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(id, token))
		z = (r.json())
		followers = (z['summary']['total_count'])
	except (KeyError, IOError):
		followers = False
	except: pass
	massage = ("• Info Account Facebook ✓ \n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n⌯ username : " +str(username)+"\n⌯ name : " +str(name)+"\n⌯ email : " +str(email)+"\n⌯ followers : " +str(followers)+"\n⌯ friends : " +str(len(friends))+"\n⌯ phone : " +str(phone)+"\n⌯ date : " +str(date)+"\n⌯ bio : " +str(bio)+"\n⌯ first_name : " +str(first_name)+"\n⌯ last_name : " +str(last_name)+"\n⌯ gender : " +str(gender)+"\n⌯ hometown : " +str(hometown)+"\n⌯ stay : " +str(stay)+"\n⌯ username : " +str(username)+"\n⌯ timezone : " +str(timezone)+"\n⌯ updated_time : " +str(updated_time)+"\n⌯ relationship_status : " +str(relationship_status)+"\n⌯ link : " +str(link)+"\n⌯ ID : " +str(id)+"\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n ⌯ Tele : @ROCKYCRACKER")
	requests.get("https://api.telegram.org/bot"+str(TK)+"/sendMessage?chat_id="+str(ID)+"&text="+str(massage))
	print (E+massage)
	sleep (4)
	
	
	


	
Facebook()
        
