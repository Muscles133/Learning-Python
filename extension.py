
media = input("File name: ")

if media.lower().endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
    print(media.lower().replace(".", "/"))
    
else:
    print("application/octet-stream")
