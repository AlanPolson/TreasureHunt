def clue_ans(clue = '1+1',  answer = '2'):
  from msvcrt import getwch 
  from os import system
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
clue_ans(clue = '16x16', answer = '256')
def word_sep(a='alan polson'):
  sep = a.split()
  for words in sep:
    print (words)
    for letters in words:
      print (letters)

#word_sep()