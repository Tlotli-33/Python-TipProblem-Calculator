meal = input("How much has the meal? ") # User enters: $85.50 as an example
percent = input("what percentage would like to tip? ") #user enters: 15% as an example
#your code below
# Step 1: Remove the $ from meal and convert to float
meal = meal[1:]
meal = float(meal)
#Step 2: Remove the % from percent, convert to float, then turn into a decimal
percent = percent[:-1]
percent = float(percent)
percent = percent / 100
#Step 3: Calculate the tip
tip = meal * percent
# Step 4: Print the result
print(f"Leave ${tip:.2f}")
