"""prompt = len(input('Enter a word: '))
count = 0
count_c = 0
consonant = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels ='aeiou'
for counter in prompt:
	if vowels in prompt:
		count += 1
	elif counter in consonant:
		count_c += 1
	
print(count, count_c)"""



def count_vowels_consonants(word):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    seen = set()
    for char in word:
        if char.lower() in vowels and char.lower() not in seen:
            vowel_count += 1
            seen.add(char.lower())
        elif char.isalpha() and char.lower() not in seen:
            consonant_count += 1
            seen.add(char.lower())
    return vowel_count, consonant_count

word = input("Enter a word: ")
vowel_count, consonant_count = count_vowels_consonants(word)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

