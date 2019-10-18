from msvcrt import getwch 
from os import system
def clue_ans(clue = '1+1',  answer = '2'):
  ans=''
  i=0
  while ans != answer:
    while i<len(answer):
        system('cls')
        print(clue)
        print("Enter Answer")
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
  
  def print_blank(end = 0):
    if end == 0:
      print('_ ', end = '')
    else:
      print print('_ ')
    