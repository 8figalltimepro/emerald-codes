# WAP to count the number of times a char accurs in a string
str = input("Enter a String: ")
# ch = input("Enter the character to be searched: ")
# count = 0
#
# for i in str:
#     if i == ch:
#         count += 1
# print(f"Number of characters in {str} : {count}")

msg = ""
for i in str:
    count = 0
    if msg.__contains__(f"\"{i}\""):
        continue
    for j in str:
        if i == j:
            count += 1
    msg += f"Number of characters, \"{i}\" in {str} : {count}\n"
print(f"{msg}")