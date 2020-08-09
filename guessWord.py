print("Hi")
DesiredWord = "Shubham"

limit = 3
userWord = list()
def compare(input,name):
  return sorted(guessWord(input)) == sorted(guessWord(name))

def guessWord(word):
  return list(set([word for word in word]))

while limit > 0 : 
  val = input("Enter your guess Character:")
  if DesiredWord.find(val) == -1 :
    limit = limit - 1
  else:
    userWord.append(val)
    if compare(DesiredWord, userWord) :
      print("Congrats , You Won !! The Word was : " + DesiredWord)
      break;

if limit <= 0 :
  print("Sorry, You Couldn`t Guess the Word " + DesiredWord)

