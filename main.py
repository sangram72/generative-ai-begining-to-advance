# print("hello world")




# skills = ["Python", "React", "AI"]

# print(skills)  



# employee = {
#     "name": "John",
#     "role": "Developer"
# }

# print(type(skills))



# name = input("Enter your name: ")

# print("Hello " + name + "!")


# age = input("Enter your age: ")

# print(int(age) + 5)


# name= input("Enter your name: ")

# age = input("Enter your age: ")

# experience = input("Enter your experience: ")

# user_skills = input("Enter your skills (comma separated): ")
# skills = []

# for i in user_skills.split(","):
#     skills.append(i.strip())


# print(name)
# print(age)
# print(experience)
# print(skills)


# print(10 / 3)
# print(10 // 3)




# is_logged_in = False

# if not is_logged_in:
#     print("Please login")
# else:
#     print("Welcome back!")


# skills = ["Python", "React", "LangChain", "Azure"]

# print("Python" in skills)  # True


# a = [1, 2, 3]

# b = a

# c = [1, 2, 3]


# print(a==b)

# print(a is c)

# print(1 in a)


# count = 1

# while count<=5:

#       print(count)
#       count+=1


# strings 

# text = "GENERATIVE AI GENERATIVE GENERATIVE AI"

# print(text[:2])
# print(text.count("GENERATIVE"))
# print(text.replace("GENERATIVE", "GENAI"))
# print(text.split(" "))


# list 

# skills = ["Python", "React"]

# skills.append("langchain")
# skills.extend(["RAG", "Azure"])
# skills.insert(1, "AI")
# skills.remove("React")
# skills.pop(0)
# print(skills.index("Azure"))
# skills.sort()
# print(skills)

# tuples

# employee = ("Sangram", 26, "Developer")

# # whatever you write as idetifier it will be the exact value how you assign it to the tuple.
# fbhbbfuu, age, role = employee

# print(fbhbbfuu)


# # sets 

# user1 = {"Python", "React", "RAG"}

# user2 = {"Python", "Azure", "LangChain"}

# print(user1 | user2)  # union returns unique values
# print(user1 & user2)  # intersection returns common values
# print(user1 - user2) # difference returns values in user1 but not in user2


employee = {
    "name": "Sangram",
    "age": 26,
    "role": "Software Engineer",
    "skills": ["Python", "React", "RAG"]
}

print(employee["name"])
print(employee.get("age")) #this is a safer way to access values in a dictionary. If the key doesn't exist, it returns None instead of raising an error.
     




