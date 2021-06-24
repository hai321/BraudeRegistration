import re
import base64
import requests
from Crypto.Cipher import AES

USERNAME = ""
PASSWORD = ""

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

s = requests.Session()

# Get encrption key/iv
r = s.get("https://info.braude.ac.il/yedion/FireFlyweb.aspx?PRGNAME=Enc", verify=False)
enc_key = base64.b64decode(r.text)
IV = 16 * b'\x00'  # needs to be encoded, too!
# Encrypt password with AES-256
raw = pad(PASSWORD)
cipher = AES.new(enc_key, AES.MODE_CBC, enc_key)
enc_password = base64.b64encode(cipher.encrypt(raw.encode('ascii', 'ignore'))).strip()
encryptedpass = enc_password.decode("utf-8")
# First LoginValidation
r = s.post("https://info.braude.ac.il/yedion/fireflyweb.aspx",
           data={
               "PRGNAME": "LoginValidation",
               "ARGUMENTS": "R1C1,R1C2,-AH,-A,-N,-N,-N,-A,R1C5",
               "R1C1": USERNAME,
               "R1C2": "",
               "R1C5": encryptedpass,
           }, verify=False)
login_arguments = re.findall('name="Arguments" value="([^"]+)"', r.text)[0]

uniq = login_arguments.split(",")[2][3:]
# print uniq
# Final LoginValidation step
r = s.post("https://info.braude.ac.il/yedion/fireflyweb.aspx",
           data={
               "prgname": "LoginValidtion1",
               "Arguments": login_arguments
           }, verify=False)
# print r.text


r = s.post("https://info.braude.ac.il/yedion/fireflyweb.aspx",
           data={
               "APPNAME": "",
               "PRGNAME": "YReg",
               "ARGUMENTS": "TZ,UNIQ,MisparCourse,R1C1,R1C2,MisparKvuza,generatedToken",
               "TZ": USERNAME,
               "UNIQ": uniq,
               "MisparCourse": "",
               "R1C1": "2",
               "R1C2": "1",
               "MisparKvuza": "",
               "generatedToken": ""

           }, verify=False)
r = s.post("https://info.braude.ac.il/yedion/fireflyweb.aspx",
           data={
               "APPNAME": "",
               "PRGNAME": "YReg",
               "ARGUMENTS": "TZ,UNIQ,MisparCourse,R1C1,R1C2,MisparKvuza,generatedToken",
               "TZ": USERNAME,
               "UNIQ": uniq,
               "MisparCourse": "",
               "R1C1": "2",
               "R1C2": "9",
               "MisparKvuza": "",
               "generatedToken": ""

           }, verify=False)
r = s.post("https://info.braude.ac.il/yedion/fireflyweb.aspx",
           data={
               "APPNAME": "",
               "PRGNAME": "YReg",
               "ARGUMENTS": "TZ,UNIQ,MisparCourse,R1C1,R1C2,MisparKvuza,generatedToken",
               "TZ": USERNAME,
               "UNIQ": uniq,
               "MisparCourse": "",
               "R1C1": "2",
               "R1C2": "1",
               "MisparKvuza": "",
               "generatedToken": ""

           }, verify=False)

r = s.post("https://info.braude.ac.il/yedion/fireflyweb.aspx",
           data={
               "APPNAME": "",
               "PRGNAME": "YReg",
               "ARGUMENTS": "TZ,UNIQ,MisparCourse,R1C1,R1C2,MisparKvuza,generatedToken",
               "TZ": USERNAME,
               "UNIQ": uniq,
               "MisparCourse": "",
               "R1C1": "2",
               "R1C2": "1",
               "MisparKvuza": "",
               "generatedToken": ""

           }, verify=False)
r = s.post("https://info.braude.ac.il/yedion/fireflyweb.aspx",
           data={
               "APPNAME": "",
               "PRGNAME": "YReg",
               "ARGUMENTS": "TZ,UNIQ,MisparCourse,R1C1,R1C2,MisparKvuza,generatedToken",
               "TZ": USERNAME,
               "UNIQ": uniq,
               "MisparCourse": "",
               "R1C1": "2",
               "R1C2": "9",
               "MisparKvuza": "",
               "generatedToken": ""

           }, verify=False)


