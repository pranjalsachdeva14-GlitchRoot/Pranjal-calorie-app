# Name: PRANJAL SACHDEVA
# Date: 7 Oct 2025
# Project: Daily Calorie Tracker

print("Welcome to Daily Calorie Tracker!")
print("This program helps you track how many calories you eat in a day.\n")

meals = []
calories = []
n = int(input("How many meals did you have today? "))

for i in range(n):
    meal = input("Enter meal name: ")
    cal = float(input("Enter calories for this meal: "))
    meals.append(meal)
    calories.append(cal)

total = sum(calories)
average = total / n

limit = float(input("\nEnter your daily calorie limit: "))

print("\n------ Summary ------")
print("Meal\tCalories")

for i in range(n):
    print(meals[i], "\t", calories[i])

print("----------------------")
print("Total:\t", total)
print("Average:", round(average, 2))

if total > limit:
    print("Warning! You ate more than your daily limit 😬")
else:
    print("Good job! You are within your daily limit 😊")

# Optional: Save data
save = input("\nDo you want to save this to a file? (yes/no): ")

if save.lower() == "yes":
    file = open("calorie_log.txt", "w")
    file.write("Daily Calorie Tracker Log\n")
    for i in range(n):
        file.write(f"{meals[i]} - {calories[i]} calories\n")
    file.write(f"Total: {total}\nAverage: {round(average, 2)}\n")
    file.close()
    print("Data saved in calorie_log.txt ✅")
else:
    print("Okay, not saved.")
