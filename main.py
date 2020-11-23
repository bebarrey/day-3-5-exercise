# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_low = name1.lower()
name2_low = name2.lower()
count_1 = 0
count_2 = 0
count_1 += name1_low.count("t") + name1_low.count("r") + name1_low.count("u") + name1_low.count("e") + name2_low.count("t") + name2_low.count("r") + name2_low.count("u") + name2_low.count("e")
count_2 += name1_low.count("l") + name1_low.count("o") + name1_low.count("v") + name1_low.count("e") + name2_low.count("l") + name2_low.count("o") + name2_low.count("v") + name2_low.count("e")
count_str = str(count_1) + str(count_2)
count_int = int(count_str)
# print(count_int, count_str)
if count_int <= 10 or count_int >= 90:
  print(f"Your score is {count_int}, you go together like coke and mentos.")
elif count_int >=40 and count_int <= 50:
  print(f"Your score is {count_int}, you are alright together.")
else:
  print(f"Your score is {count_int}.")    
