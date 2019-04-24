from flask_session_cookie_manager import FSCM

# https://github.com/semente/python-baseconv
from baseconv import base2, base16, base36, base56, base58, base62, base64, BaseConverter  

import pyperclip

import time

# from my img2.py
PROGRAM_NAME = "quickDecode"
PROGRAM_NAME_SHORT = "kwdec"

BAD = "Inconvertable :("

ASCII = ''.join(chr(x) for x in range(256))
ASCII_base = BaseConverter(ASCII, sign='ё') # umlaut e is for failsafe

# https://stackoverflow.com/a/3368991
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""


def main():
	HOW_TO = """Just copy stuff to clipboard and check console!"""
	
	print(PROGRAM_NAME+" "+"greets you!")
	print("How to:")
	print(HOW_TO)

	recent_value = ""
	# print for user
	print(PROGRAM_NAME+" is up & running")
	print("")
	
	try:
		while True:
			tmp_value = pyperclip.paste()
			if tmp_value != recent_value:
				raw = find_between(tmp_value, "MoodleSessionLMS2=", "; path=/")
				if(len(raw)):
					what_to_log = "[+] Input: "+raw
					print(what_to_log)

					ret = ""
					
					try:
						b02 = ASCII_base.encode(base2.decode(raw))
						ret += "base02: "+b02+"\n"
					except Exception:
						pass

					try:
						b16 = ASCII_base.encode(base16.decode(raw))
						ret += "base16: "+b16+"\n"
					except Exception:
						pass
					
					try:
						b36 = ASCII_base.encode(base36.decode(raw))
						ret += "base36: "+b36+"\n"
					except Exception:
						pass
						
					try:
						b56 = ASCII_base.encode(base56.decode(raw))
						ret += "base56: "+b56+"\n"
					except Exception:
						pass
						
					try:
						b58 = ASCII_base.encode(base58.decode(raw))
						ret += "base58: "+b58+"\n"
					except Exception:
						pass

					try:
						b62 = ASCII_base.encode(base62.decode(raw))
						ret += "base62: "+b62+"\n"
					except Exception:
						pass

					try:
						b64 = ASCII_base.encode(base64.decode(raw))
						ret += "base64: "+b64+"\n"
					except Exception:
						pass
					
					try:
						flask = FSCM.decode(raw)
						ret += "Flask: "+flask+"\n"
					except Exception:
						pass
					
					what_to_log = ret
					print(what_to_log)
				else:
					what_to_log = "[-] New paste, but no raw detected :("
					print(what_to_log)
				
				recent_value = tmp_value
				
			time.sleep(0.1)
	except KeyboardInterrupt:
		print('cya!')



if __name__ == '__main__':
	main()