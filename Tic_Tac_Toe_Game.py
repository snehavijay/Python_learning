class drawing:
    
   def __init__(self):      
        self.poslist = ["1","2","3","4","5","6","7","8","9"]
        self.userlist = {}
        self.userposlist = [" "," "," "," "," "," "," "," "," "]
   def drawsmall(self):
      a = ('___' * 3)
      b1 = ("| %s| %s| %s|" %( self.userposlist[0],self.userposlist[1], self.userposlist[2]))
      b2 = ("| %s| %s| %s|" %( self.userposlist[3],self.userposlist[4], self.userposlist[5]))
      b3 = ("|%s | %s| %s|"%( self.userposlist[6],self.userposlist[7], self.userposlist[8]))
      print ("\n".join((a,b1,a,b2,a, b3, a)))
    
   def user_input(self,pos, user):
        self.poslist.remove(pos)
        self.userposlist[int(pos)-1] = user
        if user not in self.userlist:
           self.userlist.update({user:[]})
        self.userlist[user].append(pos)  
        return self.poslist
   def result(self, user):
       winner = False
       while not winner:
            for i in range(0,9,3):
               if (self.userposlist[i] == self.userposlist[i+1] == self.userposlist[i+2]) and self.userposlist[i] != " ": 
                   print ("Winner is %s" % user)
                   winner = True
                   break
            if winner == True:
                break   
            for j in range(3):
                if (self.userposlist[j] == self.userposlist[j+3] == self.userposlist[j+6]) and self.userposlist[j] != " ":
                    print ("Winner is %s" % user)
                    winner = True
                    break
            if winner == True:
                break
            if ((self.userposlist[0] == self.userposlist[4] == self.userposlist[8]) or  (
                self.userposlist[2] == self.userposlist[4] == self.userposlist[6])) and self.userposlist[4] != " ":
                    print ("Winner is %s" % user)
                    winner = True
            break
                    
       if winner:
          #stop execution as we found winner  
          print("Game End. Well Played !!!")        
          exit(0)
   
            
if __name__ == '__main__':
    
    import random
    obj = drawing()
    obj.drawsmall()
    print("Play with \n 1. Computer \n 2. Friend \nChoose 1 or 2 : ")
    choice = int(input().strip())
    print(choice)
    if choice not in [1,2]:
        print("wrong input")
        exit()    
    print("User1, Enter your name: ")
    user1 = input() 
    user_choice = []      
    user_choice.append(user1.upper())   
    print("Welcome %s ! Your move is X" % user_choice[0])
    print("\nUser2, Enter your name: ")
    if choice == 2:
        user2 = input()           
    else:
        user2 = "computer"
    user_choice.append(user2.upper())
    print("Welcome %s ! Your move is O" % user_choice[1])    
        
    option_list = ["X", "O"]   
    for i in range(5):
        for user in option_list:
            user_name = user_choice[option_list.index(user)]
            print("%s \t Select your position from %s: " % (user_name, obj.poslist))
            if user_name == "COMPUTER":                
                pos = random.choice(obj.poslist)
                print ("Number selected : %s" % pos)
            else:
                pos = input()    
            if pos not in obj.poslist:
                print("Wrong selection.\n Select your position %s: " % obj.poslist)       
                pos = input()
            obj.user_input(pos,user)
            obj.drawsmall()
            obj.result(user_choice[option_list.index(user)])
            if i == 4:
               print("Game End. Well Played !!!")
               break 