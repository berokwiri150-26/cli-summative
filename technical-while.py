# goal_steps = 10000

# while True:
#     user_input = input("Enter the number of steps you have taken: (or type 'exit' to quit) ")

#     if user_input == "exit" :
#         break

#     current_steps = int(user_input)

#     if current_steps < 0:
#         print("Please enter a positive number of steps.")
#         continue 
#     if current_steps >= 5000:
#         print("Halfway there! Keep it up!")

#     if current_steps >= goal_steps:
#         print("Congratulations! You've reached your daily goal!")
#         break

#     print("Keep going! You're doing great!")

goal_steps = 10000

while True:
    user_input = input("Enter the number of steps taken (or type q to quit) = ")

    if user_input == "q":
        break

    current_steps = int(user_input)

    if current_steps < 0:
        print("Please enter a positive number of steps.")
        continue

    if current_steps >= 5000:
        print("Halfway there, keep on steppin'!")

    if current_steps > 5001:
        print("Racking up those steps, nice work!")

    if current_steps >= goal_steps:
        print("Well in trekkie! You've reached your daily goal!")

        print("Kee going! You're doing great!")
        print("Remember to stay hydrated and take breaks if needed.")