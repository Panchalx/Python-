def count_digit(message):
    digit_count=0
    for character in message:
        if character in "1234567890":
            digit_count+=1
    return digit_count

message=input("Enter a text:")
print(count_digit(message))
    