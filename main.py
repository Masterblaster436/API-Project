import requests
import json

#Funky blue text 
print("\033[1;36;1m\n")

def oldNewTestaments():
  print("Select a testament:")
  print("")
  print("Old")
  print("New")
  print("")

oldNewTestaments()
testament = input()
print("")

if testament == "Old":
  print("Please type in the name of a book")
  
elif testament == "New":
  print("Please type in the name of a book")

#User picks one gospel from the list 
def gospels():
  print("Please type in the name of a gospel:")
  print("")
  print("Matthew")
  print("Mark")
  print("Luke")
  print("John")
  print("")
  
gospels()

#Matthew = 1
#Mark = 2
#Luke = 3
#John = 4

#The bible by default is organized into books, chapters, and verses
book_id = input()
print("")

#User picks the chapter number
print("Enter a chapter number:")
print("")
chapter = input()
print("")

#User picks the verse number
print("Enter a verse number:")
print("")
verse = input()
print("")

#Get the requested book, chapter and verse
response_API = requests.get(f'https://bible-api.com/{book_id}+{chapter}:{verse}')
data = response_API.text
#parse_json = json.loads(data)
bible = [f'{book_id}'],[f'{chapter}'],[f'{verse}']

#Print the name of the book selected, and the chapter/verse numbers
print(f"{book_id}:{chapter}:{verse}")
print("")
number = 0
texts = response_API.json()
for text in texts:
  #Make sure that the text isn't printed out many times
  if number >= 1:
    break
  print(f"{texts['text']}")
  number += 1

#Print the text in the verse
#print(f"{data}")

#Problems:
#If the user puts a number too high, an error will appear
#There are in total 73 books in the (Catholic) Bible, which is too large to put into a list
#book_id can only take the names of the books, not numbers
  
#(Possible) Solutions:
#Separate the 73 books into the Old and New Testaments respectively 
#Print out an error message if the requested text can't be printed out "An error appeared"
#Separate the books further by the order they come in. For example, the user can pick a group of books and then pick from that group