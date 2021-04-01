import random
print("****************************************\n*** 		Breaking the Code	  ***\n****************************************\n")
name = input("Enter your name: ") #Asks for the users name
print (name.capitalize(), ", enter a phrase for the computer to guess (letters, numbers, and spaces only):") #Intro, takes name and capitalizes it.
#Makes the users name capitalized and asks for a new variable.
while(True): #Forces user to only input letters numbers and spaces
    password = input()
    chars = set('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,1,2,3,4,5,6,7,8,9,0, ,')
    if all((c in chars) for c in password):
        break
    else:
        print("Letters, numbers, and spaces only!")
items = ('abcdefghijklmnopqrstuvwxyz1234567890 ')
attemptcounter = 0
password = password.lower() #Makes the password non case sensitive
staticlength = len(password)
counter = staticlength
passguess = ""
Blank = ""
while (counter > 0):
    Blank = Blank + "*"
    counter = counter - 1
while (password != passguess):
    passguess = ""
    counter = 0
    while (counter < staticlength):#--
        if (Blank[counter] == "*"):
            passguess = passguess + random.choice(items) #BLANK INACTIVE, GUESS WRONG
            if passguess[counter] == password[counter]: #BLANK INACTIVE, GUESS RIGHT
                if (counter < (staticlength-1)):
                    Blank = Blank[:counter] + password[counter] + Blank[counter+1:staticlength]
                else:
                    Blank = Blank[:counter] + password[counter]
        else:
            passguess = passguess + Blank[counter]

        counter = counter + 1#--

    print (passguess)
    attemptcounter = attemptcounter + 1#--
    counter = staticlength#--

print ("Phrase matched! That took ", attemptcounter, " attempt(s).")
