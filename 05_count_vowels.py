text=input("Enter a string:").lower()
index=0
vowel_count=0
vowel_set="aeiou"
while(index < len(text)):
    if text[index] in vowel_set:
        vowel_count+=1
    index+=1

print("total number of vowels:",vowel_count)