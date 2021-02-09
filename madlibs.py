# Python project: madlibs

print("Welcome to madlibs game\n")
print("Madlibs is phrasal template word game which consists of one player prompting others for a list of words to substitute for blanks in a story before reading aloud.")



name = input("What is your name? ")
age = input("How old are you? ")
dreamJob = input("What is your dream job? ")
reason = input("Why you choose " + dreamJob + "? ")
hobby = input("What is your hobby? ")
famousPeople = input("Who is your favorite famous person? ")
reason2 = input("Why do you like " + famousPeople +"? ")

madlibs = f"Hi, my name is {name}, i'm {age} years old. I want to be {dreamJob} because {reason}. My Hobby is {hobby}. I really like {famousPeople} because\
    {reason2} and i really like that. Drink water, stay hydrated, and stay productive, {name}"


print(madlibs)
