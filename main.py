("\n File Handling")
#1: Creating a file if it doesnt eXIT
file = open("Bucket-list.txt", "w")
file.write("1. Go and visit my friend")
file.write("2. Go to Dodowa to visit my grandmom.")
file.write("3. Vist places.")
file.close()
print('Bucket list saved to Bucket list.txt!')
file = open("Bucket-list.txt ","r")
print()

print("/n-------------Reading the full file------------")
file = open("Bucket-list.txt","r")
content = file.read()
print("\n----My Bucket list----")
print(content)
file.close()

#3
print("\n-------Counting items--------")
file = open("Bucket-list.txt","r")
lines = file.readlines()
print(f"You have {len(lines)} items on your list.")
file.close()

#4
print("\n -----Adding more items-----(apppend)\n")
file = open("Bucket-list.txt", "a")
file.write ("4. Become fit by the end of the year")
file.write("5. Establish a bank account")
file.close()
print ("\n2 more items added")
#5
print("\n--------Reading the updated file")
file = open ("Bucket-list.txt", "r")
print("\n========UPDATED Bucket List")
print(file.read())
file.close()