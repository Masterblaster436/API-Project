import requests
import json

#Funky blue text 
print("\033[1;36;1m\n")

#User picks one gospel from the list 
def gospels():
  print("Please type in the name of a gospel:")
  print("")
  print("(1) Matthew")
  print("(2) Mark")
  print("(3) Luke")
  print("(4) John")
  print("")
  
gospels()

Matthew = 1
Mark = 2
Luke = 3
John = 4

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

texts = response_API.json()
for text in texts:
  print(f"{texts['text']}")

#Print the text in the verse
#print(f"{data}")