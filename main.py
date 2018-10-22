# import necessary libraries required for the program
import random
import math
import datetime

user_letters = []


# Determine application start time
app_start = datetime.datetime.now()
# Time Formatting
start = '%d/%d/%d %.2d:%.2d:%.2d' % (app_start.day, app_start.month, app_start.year, app_start.hour, app_start.minute, app_start.second)

# Generate a random index
def randindgen(word):
    randindex = ''
    while len(randindex) < len(word):
        curr_num = random.choice(range(len(word)))
        if str(curr_num) not in randindex:
            randindex = randindex + str(curr_num)
    return randindex

# Generate a random list
def randlistgen(word):
    indlst = []
    while len(indlst) < math.factorial(len(word)):
        randind = randindgen(word)
        if randind not in indlst:
            indlst.append(randind)
    return indlst

# Generate a random word
def wordgen(word):
    wordindices = randlistgen(word)
    wordlst = []
    current_word = ''
    for i in wordindices:
        for index in i:
            current_word = current_word + word[int(index)]
        wordlst.append(current_word)
        current_word = ''
    return wordlst

# Read words.txt file to variable words


with open('words.txt', 'r') as words:
    reader = words.read().splitlines()

all_valid = []
all_generated_words = []

for word in reader:
    all_valid.append(word.lower())

gen_valid = []

def gen_valid_words(letters, letter_count = 0):
	a = wordgen(letters)
	if letter_count == 0:

		for words in a:
			if words in all_valid:
				gen_valid.append(words)
				all_generated_words.append(words)

	else:
		for words in a:
			if words[:int(letter_count)] in all_valid:
				gen_valid.append(words[:int(letter_count)])
				all_generated_words.append(words[:int(letter_count)])
		if len(gen_valid) == 0:
			print("No words found.")
		else:
			print("List of Valid words: " + str(set(gen_valid)))
#Current Game State
PLAYING = True
#if no choice is made, loop will keep running until a valid choice is found.
def main():
	global PLAYING
	user_choice = str(input("Welcome to kevinj93's word generator, type 'y' to start, 'type 'x' to exit: "))
	if user_choice == 'x':
		PLAYING = False

	while True and PLAYING == True:

		if user_choice == 'y':
			user_input_letters = input("Please input the letters you want to generate words from (Special characters and/or numbers will be ignored): ")
			input_count = input("How many letter words would you like to generate? ")
			user_input_stripped = ''.join([i.lower() for i in user_input_letters if not i.isdigit() and i.isalnum()])

			try:
				user_input_count = int(input_count)
				if  user_input_count > len(user_input_stripped):
					print("Word letter count can't be greater than the number of given letters, please try again!")
				elif user_input_count <= len(user_input_letters):
					gen_valid_words(str(user_input_stripped), user_input_count)
					gen_valid.clear()
					global user_letters
					user_letters.append(str(user_input_stripped))
				else:
					print("Something is wrong, or no words were found from the given letters, try again!")


			except ValueError:
				print("Invalid letters or letter count. Please try again!")

		user_choice = str(input("'y' to continue/play, 'x' to exit. Invalid Choices not allowed. "))
		if user_choice == 'x':
			PLAYING = False

main()


print("Summary: \n")

print("You have generated a total of " + str(len(all_generated_words)) + " words. \n \n")


print("Thank you for using kevinj93's word generator. To see full log, please refer to full_applog.txt from main app dir. \n")

app_end = datetime.datetime.now()
end = '%d/%d/%d %.2d:%.2d:%.2d' % (app_end.day, app_end.month, app_end.year, app_end.hour, app_end.minute, app_end.second)

total_time = app_end - app_start
total = "You ran the application for %.2d seconds" % total_time.seconds

words.close()

two_letter_words = 0
three_letter_words = 0
four_letter_words = 0
five_or_more = 0

def determinewordcount():
	global two_letter_words
	global three_letter_words
	global four_letter_words
	global five_or_more
	for word in all_generated_words:
		if len(word) < 2:
			continue
		if len(word) == 2:
			two_letter_words += 1
		elif len(word) == 3:
			three_letter_words += 1
		elif len(word) == 4:
			four_letter_words += 1
		else:
			five_or_more += 1


determinewordcount()


logfile = open('full_applog.txt', 'a')

logfile.write(str(start) + ' Application Start \n')
logfile.write(str(end) + ' Application End \n \n')
logfile.write("Total runtime: %.2d seconds \n \n" % total_time.seconds)
if len(all_generated_words) == 0:
	logfile.write("Total Generated words: None \n \n")
else:
	logfile.write("Letters used for word generation: " + str(user_letters) + "\n \n" )
	logfile.write("(Note: 1 letter words don't count towards the generated word count) \n \n")
	logfile.write("Words with 2 letters: %d \n" % two_letter_words)
	logfile.write("Words with 3 letters: %d \n" % three_letter_words)
	logfile.write("Words with 4 letters: %d \n" % four_letter_words)
	logfile.write("Words with 5 letters or more: %d \n \n" % five_or_more)
	logfile.write("Total Generated words: " + str(len(all_generated_words)) + "\n \n")
	logfile.write("Word List: " + str(all_generated_words) + "\n \n")
	logfile.write("Total Generated Unique words: " + str(len(set(all_generated_words))) + "\n \n")
	logfile.write("Unique words list: " + str((set(all_generated_words))) + "\n \n")

logfile.write("\n \n \n \n")
logfile.close()
