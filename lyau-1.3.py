raw_input('Think of a number between 100 and 0, and I will try to guess it.  Hit [Enter] to start.')

#Setting up range of 0-100
min=0
max=100
guess=False

#loop for the guessing.  Starts with finding the midpoint of min and max, which is 50 for the initial guess and narrows down the range incrementally later.  
while not guess:
  midpt=(min+max)/2
  #checks to see if the player is lying by seeing if the min and max have converged to the same number now.
  if round(midpt)==round(max) or round(midpt)==round(min):
      print "Come on! You're not playing fair! Stick with your original number."
      guess=True
  hint= raw_input('Is it '+str(midpt)+ ' (yes/no/quit)? ')
  if hint=='yes':
    print 'I knew it!'
    guess=True
  elif hint=='quit':
    print "Well, you're no fun!"
    guess=True
  #changing min and max depending on whether the guess needs to be higher or lower.
  #If it needs to be higher, then the new min is the previous guess and the new guess will be the midpoint of the new min and previous max.
  elif hint =='no':
    hint2=raw_input('Is it higher or lower than '+str(midpt)+' ? ')
    if hint2=='lower':
        max=midpt
    if hint2=='higher':
        min=midpt
        
        
        
