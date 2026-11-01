# We have a list of documents, and we only want to process supported file types.

documents = [
    "company.pdf",
    "employee.docx",
    "image.png",
    "policy.pdf",
    "notes.txt"
]

supported_formats = ["pdf", "docx", "txt"]

for doc in documents:
    
    extension = doc.split(".")[1]

    if(extension in supported_formats):
        print(f"suppoorted format:{doc}")
    else:
        print(f"not supported format:{doc}")

      
    
