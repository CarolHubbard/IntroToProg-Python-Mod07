# ------------------------------------------------------- #
# Title: Demo of pickling
# Description: Demonstrates the use of the pickle function
# Change Log: Created script, 11/27/2022
# Carol Hubbard, 11/27/2022
# ------------------------------------------------------- #
# ------------------- Data Section ---------------------- #
import pickle  #imports the pickle module

lstPickle = []
strGiftFile = "XmasGiftList.dmp"
strRecipient = input("Please enter the gift recipient: ")

# Continue to prompt user for an age until a valid response is received
while(True):
  try:
    intAge = int(input("Please input the recipient's age: "))
  except ValueError:
    print("Please use whole numbers only for recipient's age") # If anything other than an integer is returned print this message
    continue
  break

strGift = input("Please input a gift idea for this person: ") # User inputs gift idea for recipient
lstGifts = [strRecipient,intAge,strGift] # Recipient, age and gift are placed into a list for pickling

# -----------------Processing Section ---------------------- #

# Store user-provided information into a pickle dump file
objFile = open(strGiftFile,'ab') #Creates file and opens it in append mode
pickle.dump(lstGifts,objFile) # Dumps the list contents to the file
objFile.close() #closes the file when done writing to it

strGo = input("\nPress any key to unpickle the data...\n") # Unpauses the script

objFile = open(strGiftFile, 'rb') # Reads the contents of the dump file

# Each unpickled triplet will be appended to this list
while True:
  try:
   pklData = pickle.load(objFile) # Get the next name/age/gift triplet
   lstPickle.append(pklData)    # Append it to our list of recipients
  except EOFError:
   break

# Once we reach the end of file, close the file
objFile.close()

# ----------------- Presentation Section ------------------- #
print("These gherkins are unpickled!!")
print("-"*30)

# Traverse the recipient list, printing each name/age/gift triplet to the display
for pklData in lstPickle:
  print(pklData)

strExit = input("\nPress any key to exit script...\n")