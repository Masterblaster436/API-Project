import requests

print("\033[1;36;1m\n")

print("")
print("Type out the name of a book:")
print("")
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

print("\033[1;32;1m\n")

response_API = requests.get(f'https://bible-api.com/{book_id}+{chapter}:{verse}')
if response_API.status_code == 200:
  data = response_API.text
  bible = [f'{book_id}'],[f'{chapter}'],[f'{verse}']

#Print the name of the book selected, and the chapter/verse numbers
  print(f"{book_id}:{chapter}:{verse}")
  number = 0
  texts = response_API.json()
  for text in texts:
  #Make sure that the text isn't printed out many times
    if number >= 1:
      break
  print(f"{texts['text']}")
  number += 1

elif response_API.status_code == 404:
  print(f"The chapter/verse number your looking for does not exist please try a different number!: {response_API.status_code} - {response_API.reason}")
  

else: 
  print(f"something went wrong  {response_API.status_code} - {response_API.reason}")