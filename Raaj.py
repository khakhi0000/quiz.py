h1 = ' Welcome to the Quiz Game '
print(h1.center(90))

score = 0

# Question 1
print("\nWhat is the capital city of France?")
print("a) Madrid \nb) Berlin \nc) Paris \nd) Rome")
Answer = input("Enter the answer: ").lower()
if Answer == 'c' or Answer == 'paris':
    print("Right! ✅")
    score += 1
else:
    print("Wrong ❌, The correct answer is 'c' (Paris)\n")

# Question 2
print("\nWhich programming language is known for its simplicity and is widely used for web development and automation?")
print("a) JavaScript \nb) Python \nc) Swift \nd) C++")
Answer = input("Enter the answer: ").lower()
if Answer == 'b' or Answer == 'python':
    print("Right ✅")
    score += 1
else:
    print("Wrong ❌, The correct answer is 'b' (Python)\n")

# Question 3
print("\nWhich is the largest planet in our solar system?")
print("a) Earth \nb) Mars \nc) Jupiter \nd) Venus")
Answer = input("Enter your answer: ").lower()
if Answer == 'c' or Answer == 'jupiter':
    print("Right ✅")
    score += 1
else:
    print("Wrong ❌, The correct answer is 'c' (Jupiter)\n")

# Final Result
print(f"\n🎯 Your total score is: {score}/3")

if score == 3:
    print("Perfect Sir! 🏆")
elif score == 2:
    print("Not bad, Sir 👍")
elif score == 1:
    print("Nice try 😅")
else:
    print("Keep trying, Sir! 💪")
