
media = input("File name: ")

if media.replace(" ","").lower().endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
    print(media.lower().replace(".", "/"))
    
else:
    print("application/octet-stream")
