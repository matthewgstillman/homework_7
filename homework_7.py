#Homework 7
#1. Create 2 dictionaries: one for the day of the week and another for the month.
#day_of_week = {1:‘Monday’,2: ‘Tuesday’ ……}
#month = {1:‘January’,2: ‘February’:…….}
days_of_week = {
  1 : 'Monday',
  2 : 'Tuesday',
  3 : 'Wednesday',
  4 : 'Thursday',
  5 : 'Friday',
  6 : 'Saturday',
  7 : 'Sunday'
}

months = {
  1 : 'January',
  2 : 'February',
  3 : 'March',
  4 : 'April',
  5 : 'May',
  6 : 'June',
  7 : 'July',
  8 : 'August',
  9 : 'September',
  10 : 'October',
  11 : 'November',
  12 : 'December',
}
#2. Use the dictionaries from 1 and the function randint()to randomly assign a birthday to these
#fictional emoji characters: Gene, Hi-5, Jailbreak, Smiler
#Hint:
# You run randint the first time to generate a random number from 1 to 12 (1 means Jan, 2
#means February).
# You need to run randint three times
#Sample output:
#Gene was born on Monday, January 31
#Hi-5 was born on Thursday, February 14
#…
#Note: Some months have 31 days. Some have less. February 31 is not a valid date.
emojis = ['Gene', 'Hi-5', 'Jailbreak', 'Smiler']

for i in range(0, len(emojis)):
  emoji = emojis[i]
  birth_month = random.randint(1,12)
  month = months[birth_month]
  birthday_of_week = random.randint(1,7)
  day_of_week = days_of_week[birthday_of_week]
  if month in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
    birthdate = random.randint(1,32)
  elif month in ['April', 'June', 'September', 'November']:
    birthdate = random.randint(1,30)
  elif month == 'February':
    birthdate = random.randint(1,29)
  print("{} was born on {}, {} {}".format(emoji, day_of_week, month, birthdate))


#3. Do some research online to see what the function ord()do.
#Write a program that calculates the distance between any 2 english words
#For example,
#The distance between the 2 words, an and it, is 14.
#AI : Distance is 8
#NT: Distance is 6

#Hint:
# You use the function ord() to convert from a letter to a number

#You need to ask users for 2 English words
#You convert all letters to lowercase or uppercase
first_word = input("Enter Your First Word: ").lower()
second_word = input("Enter Your Second Word -  (Make Sure it is the same length as the first word or it will be edited):").lower()

#If user enters words with a different number of letters
if len(first_word) > len(second_word):
  first_word = first_word[:len(second_word)]
elif len(second_word) > len(first_word):
  second_word = second_word[:len(first_word)]

print("First Word: {}".format(first_word))
print("Second Word: {}".format(second_word))

# Convert the distance to an absolute value
distance_sum = 0
for i in range(0, len(first_word)):
  # Use this function letter by letter to calculate the distance.
  distance = abs(int(ord(first_word[i])) - int(ord(second_word[i])))
  # Add these absolute values together and print out the distance
  distance_sum += distance
print("The Distance Between {} and {} is {}".format(first_word.title(), second_word.title(), distance_sum))