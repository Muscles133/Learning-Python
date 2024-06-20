def extension_id(ext):

    if ext.endswith(".gif"):
        return "image/gif"

    elif ext.endswith(".jpg"):
        return "image/jpeg"

    elif ext.endswith(".jpeg"):
        return "image/jpeg"

    elif ext.endswith(".png"):
        return "image/png"

    elif ext.endswith(".pdf"):
        return "application/pdf"

    elif ext.endswith(".zip"):
        return "application/zip"

    elif ext.endswith(".txt"):
        return "text/plain"

    else:
        return "application/octet-stream"

def main():
    ext = input("File name: ").replace(" ","").lower()
    result = extension_id(ext)
    print(result)

main()

#can be  done with assert condtional (statement??)