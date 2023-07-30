word=input("Enter a word:")
count=0
vowels=['a','e','i','o','u']
for letter in word:
    if letter.lower() in vowels:
        count+=1
print("Number of vowels is:",count)