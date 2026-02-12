a = 'kamal'
b ='KAMAL@143'

print(a.upper())
print(b.lower())
print(a.capitalize())

# check number or not
print(a.isalnum()) # alpha numeric
print(b.isalnum()) # alpha numeric

print(a.isalpha()) # alpha
print(b.isalpha()) # alpha

print(a.isdigit()) # digit
print(b.isdigit()) # digit

# check numbers
mobile = "7148823014"

numberMasked = mobile[:2] + "******" + mobile[8:]
print("Masked mobile number: ", numberMasked)

numberMasked = mobile[:2] + "******" + mobile[-2:]
print("Masked mobile number: ", numberMasked)


song = 'jai Ho'
artist = 'ar RAHMAN'
formated = f"{song.title()} - {artist.title()}"
print(formated)

location = 'chennai'
fixed_location = location.replace('chennai', 'coimbatore')
print(fixed_location) # replace the string with another string replace(old, new)

message = 'Your uber booking id is: UBER1234567890. and your otp is 123456 and your driver name is Kamal'

# split the string by space and take the 6th element and remove the dot
print('My Booking ID:', message.split(' ')[5].strip('.'))

# split the string by colon and take the 2nd element and remove the dot
print('My Booking ID:', message.split(':')[1].split('.')[0].strip())


# Delimiter
data = "kamal,hassan,25,chennai"

# split the string by comma and take the 2nd element and remove the dot
print(data.split(','))

# search string
promo_msg = 'Use zomoto100 to get 100rs off on your first order'

# check if the string contains 'zomoto100' using 'in' operator
if 'zomoto100' in promo_msg:
    print('Promo code applied')
else:
    print('Promo code not applied!')

# check if the string contains 'zomoto100' using 'find' method

if promo_msg.find('zomoto100') != -1:
    print('Promo code applied!')
else:
    print('Promo code not applied!')

# check if the string contains 'zomoto100' using 'index' method

if promo_msg.index('zomoto100') != -1:
    print('Promo code applied!')
else:
    print('Promo code not applied!')


# check if the string contains 'zomoto100' using 'find' position
print('Promo code position:', promo_msg.find('zomoto100'))

# # check if the string contains 'zomoto100' using 'index' position
# print('Promo code position:', promo_msg.index('zomoto100'))

# # check if the string contains 'zomoto100' using 'rfind' position
# print('Promo code position:', promo_msg.rfind('zomoto100'))

# # check if the string contains 'zomoto100' using 'rindex' position
# print('Promo code position:', promo_msg.rindex('zomoto100'))

# # check if the string contains 'zomoto100' using 'count' position
# print('Promo code position:', promo_msg.count('zomoto100'))

# # check if the string contains 'zomoto100' using 'startswith' position
# print('Promo code position:', promo_msg.startswith('zomoto100'))

# # check if the string contains 'zomoto100' using 'endswith' position
# print('Promo code position:', promo_msg.endswith('zomoto100'))

# # check if the string contains 'zomoto100' using 'strip' position
# print('Promo code position:', promo_msg.strip('zomoto100'))

# # check if the string contains 'zomoto100' using 'lstrip' position
# print('Promo code position:', promo_msg.lstrip('zomoto100'))

# # check if the string contains 'zomoto100' using 'rstrip' position
# print('Promo code position:', promo_msg.rstrip('zomoto100'))

# # check if the string contains 'zomoto100' using 'replace' position
# print('Promo code position:', promo_msg.replace('zomoto100', 'zomoto100'))

# # check if the string contains 'zomoto100' using 'split' position
# print('Promo code position:', promo_msg.split('zomoto100'))

# # check if the string contains 'zomoto100' using 'join' position
# print('Promo code position:', promo_msg.join('zomoto100'))

# # check if the string contains 'zomoto100' using 'partition' position
# print('Promo code position:', promo_msg.partition('zomoto100'))

# # check if the string contains 'zomoto100' using 'rpartition' position
# print('Promo code position:', promo_msg.rpartition('zomoto100'))

# #check if the string contains 'zomoto100' using 'splitlines' position
# print('Promo code position:', promo_msg.splitlines('zomoto100'))

# # check if the string contains 'zomoto100' using 'splitlines' position
# print('Promo code position:', promo_msg.splitlines('zomoto100'))

# name to character
name = "kamal hassan"
initials = name.split()
print(initials[0][0] + initials[1][0])

# name for loop
nameData = ([word[0].upper() for word in name.split()])
print(nameData)
print("".join(nameData))

# clean text
name = "  kamal hassan  "
print(name.strip()) # remove both side space
print(name.lstrip()) # remove Left space
print(name.rstrip()) # remove Right space

# check line word counts
paragraphs = 'use string methods to count the number of words in the string and print the count of each word'
print(paragraphs.split())
count_para = len(paragraphs.split())
print('words count:', count_para)

# check line word inside the string counts
paragraphs = 'use string methods to count the number of words in the string and print the count of each word'
print(paragraphs.split('words')) # split the string by 'words' and print the result
count_para = len(paragraphs.split('words'))
print('inside words count:', count_para)