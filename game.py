import random
#computer's guess
def compguess(lowerval,higherval,randno,count=0):
    if higherval > lowerval:
         guess = lowerval + (higherval-lowerval) // 2
         #guess in middle
         if guess == randno:
            return count
         #if guess is greater than num it must  be founf in the lower half between the lowerval and guess
         elif guess > randno:
              count = count+1
              return compguess(lowerval,guess-1,randno,count)
         #or the no will be in the upper half btw guess and upper half
         else:
             count = count +1
             
             return compguess(guess+1,higherval, randno , count)
    else:
        return -1  
      
     
#generate a random number b/w 0,100
randno=random.randint(1, 101)

count = 0
guess = -1
while (guess !=randno):
    #guess an number
    guess = (int)(input('Enter a number between 0 and 100:'))
    if guess < randno:
        print('enter a bigger number!')
    elif guess > randno:
        print('enter a smaller number!')
    #elif  guess > 101:
        #print('please enter a number between 0 and 100')
    else:
        print('congrats u guessed it!')
        break
    count =count+1
#end of loop
print('you took ' + str(count) + ' steps to guess')
print('the computer took '+str(compguess(0,100,randno))+' steps!')




    
    
    
    
    
    
    
    
    
      
 
        
        
        
    

    
    