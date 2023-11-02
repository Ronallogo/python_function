world =   "aaapppeeeooorrrgeeess,,"
count = 0 
underWorld = []
 
while count < len(world):
    x = world[count]
    if x in world[count + 1 :] :
        underWorld.append(x)
        count += 1
    elif  x not in underWorld and x is not world :
        print(x)
        count += 1     
    else:
        count +=1
        pass
    

