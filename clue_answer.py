from msvcrt import getche, getch, getwch, getwche
from os import system

debug=False
dev=False
hint=False
ans=False

def clue_ans(clue = 'dr suess book',  answe = 'cat in the hat'):
  """
  main function of this class.
  accepts parameters:
    clue: clue to be displayed
    answe: string (words in the string should be seperated by spaces, no punctuation)
  """
  answer = answe.upper().split()
  ans=[]
  choice = ''
  cntr=0
  while 1:
    refresh(clue,answer,ans)
    result=checkans(ans,answer)
    if result == 'N':
      return('Q')
    elif result =='Y':
      ans=[]
      continue;
    elif result=='Correct':
      print("Answer:",' '.join(ans),"\nCorrect!")
      return('C')      
    char = getwch()
    if char=='à':#F12
      if input("Enter password to invoke Developer mode\n")=='Alan Rules':
        setdev(True)
        continue
    
    elif char in('\x08', 'à'):#backspace, delete
      ans=ans_delete(ans)
    
    else:
      ans=ans_append(char.upper(), answer,ans)
    for words in ans:
      if words in (' ', '\c', 'n', '\r', '\t'):
        ans.remove(words)
    if debug:
      cntr+=1
      print("\nEnd of iteration #",cntr,"\nans=",ans)
      getch()

def setdev(tog):
  global dev
  global debug
  global hint
  dev=tog
  option=''
  while (option!='x'):
    print('Developer Mode [a] = ',dev, '\nDebug Mode [b] = ',debug, '\nHint [c] = ',hint, '\nExit [x]')
    option=input('\nEnter choice to toggle variables:')
    if option == 'a':
      dev=not dev
    elif option == 'b':
      debug = not debug
    elif option == 'c':
      hint = not hint
    

def checkans(ans,answer):
  """
  Parameters:
  ans: list of strings of user-inputted answer
  answer list of strongs of correct answer
  """
  if len(' '.join(ans))==len(' '.join(answer)):
    if ans==answer:
      return 'Correct'
    else:
      choice = input("Incorrect!\nTry again? (y/n)\nAns: ")
      return (choice.upper())
  else:
    return ''

def ans_append(char,answer,ans):
  """
  accepts a character and appends it to the list of words the user has entered so far, 
  or to the end of a word, if the word is not yet complete.
  parameters:
  Character (single char)
  Correct Answer (list of strings)
  User-inputted answer (list of strings)
  """
  if debug:
    print("in answ_apend")
  if len(ans)==len(answer) and len(ans[len(ans)-1])==len(answer[len(answer)-1]):
    return ans
  if ans==[]:
    ans+=char
    return ans
  if debug:
    print(ans,len(ans))
  i=len(ans)-1
  j=len(ans[i])-1
  if debug:
    print('\ni==',i,'\nj=',j)
  
  
  if j+1==len(answer[i]):
    if debug:
      print(answer[i])
      print("option1")
      getch()
    ans+=char
  else:
    if debug:
      print("option2")
      print(ans)
      print (i)
      print (answer)
      print(ans[i])
      getch()
    ans[i]+=char
  return ans

def ans_delete(ans):
  """
  deletes the last charachter in the answer
  """
  if ans==[]:
    return ans
  
  i=len(ans)-1
  j=len(ans[i])-1
  
  if j>=1:
    ans[i]=ans[i][:j]
  else:
    ans.remove(ans[i])
  return ans

def refresh(clue,answer,ans):
  """
  prints the clue, and the number of blank spaces for the answer. 
  It also prints all the characters filled in
  Called by passing:
  the clue (character string), 
  the correct answer (as a list of words), 
  and the list of words entered by the user so far (list of words)
  """
  i=0
  system('cls')
  print(clue)
  print("Enter Answer")
  while i<len(answer):
    if debug:
      print ('\ni iteration #:',i)
    j=0
    while j<len(answer[i]):
      if debug:
        print ('\nj iteration #:',j)
      if i<len(ans) and j<len(ans[i]):
           print(ans[i][j],'', end = '') 
      else:
        print_blank()
        
        if debug:
          print('j+1=',j+1)
        if (j+1)==len(answer[i]):
          print (' ',end='')
      j+=1
    print (' ',end='')
    i+=1
  print ()
      
def print_blank(end = ''):
  """
  Prints an underscore and space, and by default remains on the same line.
  """
  if end == '':
    print('_ ', end = '')
  else:
    print('_ ')    