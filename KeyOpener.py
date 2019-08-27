import os
from time import sleep


a ='\033[96m'
b ='\033[94m'
c ='\033[0m'
d ='\033[92m'
os.system('clear')
print(a+'_'*50)
print
print(a+'\tFitur Tambahan Termos :V')
print(a+'\tBrebes Noob')
print('\thttps://m.facebook.com/galank.rambu42')
print(a+'_'*50)
print('\nSabar...')
sleep(1)
print(b+'\n[!] membuat properti di directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(d+'[!]Berhasil Bro !')
sleep(1)
print(b+'\n[!] Mengatur..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(d+'[!] Berhasil Bro !')
sleep(1)
print(b+'\n[!] Mengatur...')
sleep(2)
os.system('termux-reload-settings')
print(d+'[!] Berhasil Bro !! :V'+c+'\n\nhubungi https://m.facebook.com/galank.rambu42\nThanks :*\n\n')


# ini cuma shortcut buat bantu para nub
# Brebes Noob
