from msvcrt import getche, getch, getwch
from os import system
def clue_ans(clue = 'dr suess book',  answe = 'cat in the hat'):
  answer = answe.split()
  ans=[]
  choice = ''
  #getwch()
  #cntr=0
  while 1:
    refresh(clue,answer,ans)
    result=checkans(ans,answer)
    if result == 'N':
      break
    elif result =='Y':
      ans=[]
      continue;
    elif result=='Correct':
      print("Answer:",' '.join(ans),"\nCorrect!")
      break;      
    char = getwch()
    ans=ans_append(char, answer,ans)
    for words in ans:
      if words in (' ', '\c', 'n', '\r', '\t'):
        ans.remove(words)
    #cntr+=1
    #print("\nEnd of iteration #",cntr,"\nans=",ans)
    #getwch()
    #break
  print("Press any key to exit...")
  getch()

def checkans(ans,answer):
  if len(' '.join(ans))==len(' '.join(answer)):
    if ans==answer:
      return 'Correct'
    else:
      choice = input("Incorrect!\nTry again? (y/n)\nAns: ")
      return (choice.upper())
  else:
    return ''

def ans_append(char,answer,ans):
  if len(ans)==len(answer) and len(ans[len(ans)-1])==len(answer[len(answer)-1]):
    return ans
  if ans==[]:
    ans+=char
    return ans
  #print(ans,len(ans))
  i=len(ans)-1
  j=len(ans[i])-1
  #print("in answ_apend", '\ni==',i,'\nj=',j)
  
  
  if j+1==len(answer[i]):
    #print(answer[i])
    #print("option1")
    #
    #getwch()
    ans+=char
  else:
    #print("option2")
    #print(ans)
    #print (i)
    #print (answer)
    #print(ans[i])
    #getwch()
    ans[i]+=char
  return ans

def refresh(clue,answer,ans):
  i=0
  system('cls')
  print(clue)
  print("Enter Answer")
  while i<len(answer):
    #print ('\ni iteration #:',i)
    j=0
    while j<len(answer[i]):
      #print ('\nj iteration #:',j)
      if i<len(ans) and j<len(ans[i]):
           print(ans[i][j],'', end = '')
          # if i+1==len(answer) and j+1==len(answer[i]):
          #   if answer!=ans:
          #     print("Incorrect!\nTry again? (y/n)")
          #     choice = getche()
          #     print(choice)              
      else:
        print_blank()
        #print('j+1=',j+1)
        if (j+1)==len(answer[i]):
          print (' ',end='')
      j+=1
    print (' ',end='')
    i+=1
    #getwch()
  print ()
      
"""
          print (ans[j],'', end = '')
          j+=1
        while j<len(answer):
          print ('_ ', end = '')
          j+=1
        print ()
        #char = input('enter a letter')
        char = getwch()
        #print(ord(char))
        #print ('i=',i,'j=',j,'i-j=',i-j)
        ans+=char
        #print (ans[i-j])
        i +=1 
    system('cls')
    print (" Answer: ", ans)
    if ans == answer:
      print ('Correct!')
      break;
    else:
      print ('Incorrect!')
      getwch()
      ans=''
      i=0
  
  print("Press any key to exit...")
  getwch()

#clue_ans()
#clue_ans(clue = '16x16', answer = '256')
    
def multi_word(answer='alan polson'):
  print("Enter Answer")
  #answer = 'cat in a hat'
  answer1 = answer.split()
  words = len(answer1)
  for x in range(0, words):
    letters =len(answer1[x])
    for y in range(0,letters):
      print ('_ ',end='')
    print (' ',end='')
    
def outer_question(clue = '1+1',  answer = '2'):
  ans=[]
  i=0
  while ans != answer:
    while i<len(answer):
        system('cls')
        print(clue)
        print("Enter Answer")
        answer1=answer.split()
        for i in range(0,len(answer1)):
          ans.append(single_ans(answer1[i]))
        print (ans)
        getwch()
def single_ans(answer = '256'):
  ans=''
  i=0
  while ans != answer:
    while i<len(answer):
        #system('cls')
        #print(clue)
        #print("Enter Answer")
        j=0
        while j<len(ans):
          print (ans[j],'', end = '')
          j+=1
        while j<len(answer):
          print ('_ ', end = '')
          j+=1
        print ()
        #char = input('enter a letter')
        char = getwch()
        #print(ord(char))
        #print ('i=',i,'j=',j,'i-j=',i-j)
        ans+=char
        #print (ans[i-j])
        i +=1 
        return(ans)
    #system('cls')
    print (" Answer: ", ans)
    if ans == answer:
      print ('Correct!')
      break;
    else:
      print ('Incorrect!')
      getwch()
      ans=''
      i=0
  
  print("Press any key to exit...")
  getwch()
"""
def print_blank(end = ''):
  if end == '':
    print('_ ', end = '')
  else:
    print('_ ')
    