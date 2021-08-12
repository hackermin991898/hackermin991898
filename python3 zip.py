CARA BUAT SCRIPT DARI PYTHON3 || #Coding_Python

import zipfile
import sys
import 05
b = "/x1b[1 ; 94m"
y = "/x1b[1 ; 93m"
w = "/x1b[1 ; 97m"
g =  "/x1b[1 ; 92m"
# untuk memghapus text dari layar
05.system("clear")
print("Xs[*]   %s7 XsAuthor Xs: XsAquaCode"%(b, w, y))
print("Xs[*] XsGithub Xs: XsAquaCodeOfficial/nXs"%(b, w, y, w))
# input untuk membuka file zip dan wordlist
print(" Xscontoh : Xs/sdcard/file/zipXs"%(b, w, w, g, w))
wordlist = input("wordlist : ")
if filezip == "":
print(" Xscontoh : Xs/sdcard/%word.txt%s"%(b, w, w, g, w))
if filezip == "": 
print"File wordlist tidak di temukan")
sys.exit()
else:
 pass
# untukmemberituhukan bahwa variabel filezip itu
# file berinteks ( zip )
# untuk menampilkan/mebuka list dari wordlist
filezip = zipfile.ZipFile(filezip)
listword = len(list(open(wordfile. "rb")))
# untuk memcetak list dari variabel wordfile
print("Password yang terkumpul ":, listword)
# membuka file wordlist
with open(wordfile, "rb") as wordfile:
   for i in wordfile: #untuk sengulang sampai password ketemu
       try:
# jika password di temukan akan langsung di exstrak
         filezip.extractall(pwd.i())
      except:
# jika terjadi error akan terus di lanjutkan
         continue
      else:
# kalau password di temukan akan lansung di cetak ke print ini
          print("password di temukan ":,i.decode().strip())
          sys.exit() # kalau password ketemu akan langsung close
 [*] contoh : /sdcard/filezip
file zip : /host-rootfs/sdcard/aquacode.zip
[*] contoh /sdcard/word.txt
wordlist : txt
Password yang terkumpul :
Password tidak ditemukan :
