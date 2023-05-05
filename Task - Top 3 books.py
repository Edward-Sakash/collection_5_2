"""Task - Top 3 books
You have a dict with a list of book titles as keys and their sales numbers as values. Implement a method that prints the top 3 books from this dict to the screen.

Input:
books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}
Output:
1.Harry Potter And The Sorcerer's Stone: 1241100000
2.Harry Potter And The Deathly Hallows : 652200000
3.Harry Potter And The Goblet Of Fire: 645600000"""

print("_________________________________________________")

#Solution 1
books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}

# sort the books by their sales numbers in descending order
sorted_books = sorted(books.items(), key=lambda x: x[1], reverse=True)

# print the top 3 books
for i, (title, sales) in enumerate(sorted_books[:3], start=1):
    print(f"{i}.{title}: {sales}")

print("_________________________________________________")

# Solution 2
books = {
    'Harry Potter And The Sorcerer\'s Stone': 1241100000,
    'Harry Potter And The Chamber Of Secrets': 771300000,
    'Harry Potter And The Prisoner Of Azkaban': 65210000,
    'Harry Potter And The Goblet Of Fire': 645600000,
    'Harry Potter And The Order Of The Phoenix': 635600000,
    'Harry Potter And The Half Blood Prince': 661300000,
    'Harry Potter And The Deathly Hallows ': 652200000,
}

# Sort the dictionary by value in descending order
sorted_books = sorted(books.items(), key=lambda x: x[1], reverse=True)

# Loop over the first 3 elements and print them
for i, book in enumerate(sorted_books[:3], start=1):
    print(f"{i}.{book[0]}: {book[1]}")

print("_________________________________________________")

# Solution 3
books = {
    'Harry Potter And The Sorcerer\'s Stone': 1241100000,
    'Harry Potter And The Chamber Of Secrets': 771300000,
    'Harry Potter And The Prisoner Of Azkaban': 65210000,
    'Harry Potter And The Goblet Of Fire': 645600000,
    'Harry Potter And The Order Of The Phoenix': 635600000,
    'Harry Potter And The Half Blood Prince': 661300000,
    'Harry Potter And The Deathly Hallows ': 652200000,
}

# Sort the dictionary by value in descending order
sorted_books = sorted(books.items(), key=lambda x: x[1], reverse=True)

# Loop over the first 3 elements and print them
for i, book in enumerate(sorted_books[:3], start=1):
    print("{0}.{1}: {2}".format(i, book[0], book[1]))
