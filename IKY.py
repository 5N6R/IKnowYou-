#I Know You! version 0.5 beta (c) 2017, coded by 5n6r
#Under MIT License
#!/usr/bin/env python3
import requests,time,urllib.request,json,sys
print("\033[1;32mI Know You! (IKY) версия 0.5 бета "+chr(169)+" 2017, программирование 5n6r\033[0;0m")
numG=int(input("Введите номер группы, участники которых вас интересуют: "))
opener=urllib.request.build_opener()
opener.addheader=[("User-agent","Mozilla/5.0")]
url = "https://api.vk.com/method/groups.getById?group_id=" + str(numG)
rrr = requests.get(url)
sss=rrr.json()
nmg=sss["response"][0]["name"]
print("Название группы: "+nmg)
genG=int(input("Введите пол участников(1-для девушек, 2-для парней, 0-выход из скрипта): "))
if genG==0:
 sys.exit(0)
r = requests.get("https://api.vk.com/method/groups.getMembers",params={"group_id":numG})
s=r.json()
try:
 rr=s["response"]["users"]
except KeyError:
 err=s["error"]["error_msg"]
 print("Sorry, but... "+err)
 sys.exit(0)
i=len(rr)
print("Всего в группе "+nmg+" "+str(i)+" челловек.")
for ii in range(0,i-1):
 r2 = requests.get("https://api.vk.com/method/users.get",params={"user_ids":rr[ii],"fields":"sex,photo_max_orig,bdate"})
 u=r2.json()
 sx=u["response"][0]["sex"]
 nm=u["response"][0]["first_name"]
 pht=u["response"][0]["photo_max_orig"]
 idu=u["response"][0]["uid"]
 if sx==genG and pht!="https://vk.com/images/deactivated_400.png" and pht!="http://vk.com/images/camera_400.png" and pht!="https://vk.com/images/deactivated_400.png":
  print("\033[1;33mСкачивю "+nm+" \033[0;0m "+pht)
  #urllib.request.urlretrieve(pht,nm+"_id_"+str(idu)+".jpg")
  client=opener.open(pht)
  f=open(nm+"_id_"+str(idu)+".jpg","wb")
  f.write(client.read())
  f.close()
  client.close()
 else:
  print("\033[1;33mПропускаю ненужных участников группы.. \033[0;0m ")
 time.sleep(0.1)
print("Готово!")
