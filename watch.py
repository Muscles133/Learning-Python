import re
import sys


def main():

    html = r'<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=Bq_NljtVZera5Mk2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    #print(html)
    #print(parse(input("HTML: ")))

    print(parse(html))


def parse(s):
    if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", s):

        print(f"Username : ", matches.group(1))



if __name__ == "__main__":
    main()