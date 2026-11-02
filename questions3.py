
# Exercise 1 — Reverse a string

# Input: 'Generative AI'. Output: 'IA evitareneG'. Try slicing first, then solve without slicing.



# Exercise 2 — Remove duplicates

# Given [1, 2, 2, 3, 4, 4, 5], create a list containing only unique values.



# Exercise 3 — Find common elements

# Given two lists of skills, find the common skills using sets.



# Exercise 4 — Dictionary filtering

# Given employee dictionaries, print employees having more than 2 years of experience.



# Exercise 5 — Document metadata

# Create a list of 3 document dictionaries with filename, file type, document ID and tags. Print only PDF documents.




# 1. 

# str = 'Generative AI'

# print("".join(reversed(str)))

# print(str[::-1])

# 2.

# num = [1, 2, 2, 3, 4, 4, 5]

# for i in num:
#     if num.count(i)>1:
#         num.remove(i)
# print(num)

# num = list(set(num))
# print(num)

# 3.

# num1 = ["Python", "React", "RAG", "Azure"]
# num2 = ["Python", "LangChain", "RAG", "Azure"]

# print(set(num1) & set(num2)) #set is used to find the common elements between two lists.


# 4.
# employees = [
#     {"name": "Alice", "role": "Developer", "experience": 4},
#     {"name": "Bob", "role": "Designer", "experience": 1.5},
#     {"name": "Charlie", "role": "Manager", "experience": 5},
#     {"name": "David", "role": "Intern", "experience": 2},
#     {"name": "Emma", "role": "Data Analyst", "experience": 3},
# ]

# print("Employees with more than 2 years of experience:")

# for employee in employees:
#     if employee["experience"] > 2:
#         print(f"Name:{employee['name']}, Role: {employee['role']}, Experience: {employee['experience']} years")

# 5.

documents = [
    {
        "filename": "annual_report.pdf",
        "file_type": "PDF",
        "document_id": "DOC001",
        "tags": ["finance", "corporate", "2026"],
    },
    {
        "filename": "project_timeline.xlsx",
        "file_type": "Excel",
        "document_id": "DOC002",
        "tags": ["management", "schedule"],
    },
    {
        "filename": "resume_candidate.pdf",
        "file_type": "PDF",
        "document_id": "DOC003",
        "tags": ["HR", "hiring", "resume"],
    },
]

for doc in documents:
    if doc["file_type"]=="PDF":
        print(f"Filename: {doc['filename']}, Document ID: {doc['document_id']}, Tags: {', '.join(doc['tags'])}")