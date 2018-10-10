import sys

def combine():
    if len(sys.argv) < 2:
        sys.exit("Example usage: python combineSVG.py first.svg second.svg third.svg")

    html_page = []
    html_page.append("<html><body>")

    svgs = sys.argv[1:]
    for svg in svgs:
        html_page.append("<div>")
        obj = "<object type=image/svg+xml data="
        obj += svg
        html_page.append(obj)
        html_page.append("></object>")
        html_page.append("</div>")

    html_page.append("</body></html>")

    with open("index.html", 'w') as f:
        for line in html_page:
            f.write(line + '\n')

if __name__ == "__main__":
    combine()