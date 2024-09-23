import re

def main():
    #html = r'<iframe width="560" height="315" src="https://www.youtube.com/embed/DyoVVSggPjY?si=lKDyUT7Qpi24u4KS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([^"?]+)', s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"
    return None

if __name__ == "__main__":
    main()