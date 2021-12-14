photos={"camera":10,"watsapp images":25,"canva":1,"screenshots":150}
photos["snap chat"]=11
photos["sweetsnap"]=7
photos["snapseed"]=13 
photos["bs12"]=9
photos["retrica"]=5
print(photos)
if isinstance(photos,dict)==True:
    print("entry is correct")
else :
    raise TypeError("entered datatype is wrong")
for i in photos.items():
    print(i)
instagram={"filter":12,"reels":14,"slide":29}
instagram["party filter"]=3
instagram["tiktok"]=6
instagram["moj"]=9
print(instagram)
if isinstance(instagram,dict)==True:
    print("entry is correct")
else :
        raise TypeError("entered datatype is wrong")
for i in instagram.items():
    print(i)
