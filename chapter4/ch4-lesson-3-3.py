#
# Read line by line from my_dairy.txt
# This example covers with keyword also. With 
with open('s_my_diary.txt') as book:
    for page in book.readlines():
        print(page.strip())  # Remove extra spaces
book.close()