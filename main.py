import requests
import function


#Funky blue text
print("\033[1;36;1m\n")

#User can select either old or new testament
function.oldNewTestaments()
testament = int(input())
print("")

if testament == 1:
  print("Select a group of books")
  function.list_of_old_books()
  
  group = int(input())
  print("")
  if group == 1:
    function.books_1_to_5()
  elif group == 2:
    function.books_6_to_10()
  elif group == 3:
    function.books_11_to_15()
  elif group == 4:
    function.books_16_to_20()
  elif group == 5:
    function.books_21_to_25()
  elif group == 6:
    function.books_26_to_30()
  elif group == 7:
    function.books_31_to_35()
  elif group == 8:
    function.books_36_to_40()
  elif group == 9:
    function.books_41_to_46()
  else:
    print("Please select a book from the list")
    exit()

if testament == 2:
  print("Select a group of books")
  function.list_of_new_books()
  
  print("")
  group2 = int(input())
  print("")
  if group2 == 1:
    function.new_books_1_to_5()
  elif group2 == 2:
    function.new_books_6_to_10()
  elif group2 == 3:
    function.new_books_11_to_15()
  elif group2 == 4:
    function.new_books_16_to_21()
  elif group2 == 5:
    function.new_books_22_to_28()
  else:
    print("Please select a book from the list")
    exit()



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

#more funky colours
print("\033[1;32;1m\n")

#Get the requested book, chapter and verse
response_API = requests.get(f'https://bible-api.com/{book_id}+{chapter}:{verse}')
if response_API.status_code == 200:
  data = response_API.text
#parse_json = json.loads(data)
  bible = [f'{book_id}'],[f'{chapter}'],[f'{verse}']

#Print the name of the book selected, and the chapter/verse numbers
  print(f"{book_id}:{chapter}:{verse}")
#print("")
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

#Problems:
#If the user puts a number too high, an error will appear
#book_id can only take the names of the books, not numbers

#(Possible) Solutions:
#Print out an error message if the requested text can't be printed out "An error appeared"