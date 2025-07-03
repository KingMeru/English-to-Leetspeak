#main function collects user input and strips all punctuation marks and prints the return of all other functions 
def main():
	user_sentence = input("Enter a sentence: ")
	
	user_sentence_list = []
	for element in user_sentence:
		if element != '.' and element != ',' and element != ';' and element != '?' and element != '!' and element!= '\'':
			user_sentence_list.append(element)
			
	get_upper(user_sentence_list)
	print(get_upper(user_sentence_list))
	print()
	print(get_acronyms(get_upper(user_sentence_list)))
	print()
	print(get_homoglyphs(get_upper(user_sentence_list)))
	
# converts every lower case character to upper case using chr() and ord() function 	
def get_upper(sentence):
	user_sentence_upper = []
	for item in sentence:
		lower_case_check = ord(item)
		if lower_case_check >= 97:
			upper_case = lower_case_check - 32	
			new_letter = chr(upper_case)
			user_sentence_upper.append(new_letter)
		else:
			user_sentence_upper.append(item)
	
	user_sentence_upper2 = ''.join(user_sentence_upper)		
	get_acronyms(user_sentence_upper2)
	get_homoglyphs(user_sentence_upper)
	return user_sentence_upper2

# creates an acronym by taking the first character of every word	
def get_acronyms(sentence):

	new_sentence = sentence.split()
	short_sentence = []
	for element in range(len(new_sentence)):
		if new_sentence[element] == 'BE' and new_sentence[element + 1] == 'RIGHT' and new_sentence[element + 2] == 'BACK':
			short_sentence.append(new_sentence[element][0])
			short_sentence.append(new_sentence[element + 1][0])
			short_sentence.append(new_sentence[element + 2][0])	
			
		if  new_sentence[element] == 'BY' and new_sentence[element + 1] == 'THE' and new_sentence[element + 2] == 'WAY':
			short_sentence += new_sentence[element][0]
			short_sentence += new_sentence[element + 1][0]
			short_sentence += new_sentence[element + 2][0]
			
		if  new_sentence[element] == 'LAUGH' and new_sentence[element + 1] == 'OUT' and new_sentence[element + 2] == 'LOUD':
			short_sentence += new_sentence[element][0]
			short_sentence += new_sentence[element + 1][0]
			short_sentence += new_sentence[element + 2][0]						
		
		if  new_sentence[element] == 'OH' and new_sentence[element + 1] == 'MY' and new_sentence[element + 2] == 'GOD':
			short_sentence += new_sentence[element][0]
			short_sentence += new_sentence[element + 1][0]
			short_sentence += new_sentence[element + 2][0]
					
	

			
	short_sentence2 = ''.join(short_sentence)		
			
			
	return short_sentence2	
	
	
# converts certain characters to homoglyphs	
def get_homoglyphs(sentence):
	new_sentence = []
	
	for item in sentence:
		if item == 'A':
			new_sentence.append('@')
		elif item == 'K':
			new_sentence.append('|<')
		elif item == 'H':
			new_sentence.append('|-|')
		elif item == 'B':
			new_sentence.append('|3')
		elif item == 'O':
			new_sentence.append('0')
		elif item == 'I':
			new_sentence.append('1')		
		else:
			new_sentence.append(item)
			
	new_sentence2 = ''.join(new_sentence)
	
	return new_sentence2						

		
		






main()			 
