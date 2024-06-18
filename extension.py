
media = input("File name: ")

if media.replace(" ","").lower().endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
    print(media.lower().replace(".", "/"))
    
else:
    print("application/octet-stream")

# i need to ework this script with a better understanding of what is asked.