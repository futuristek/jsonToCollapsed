import sys

def combine():
    if len(sys.argv) < 2:
        sys.exit("Example usage: python combineSVG.py first.svg second.svg third.svg")

    html_page = []
    html_page.append("<html><body>")

    svgs = sys.argv[1:]
    for svg in svgs:
        html_page.append("<div>")
        iframe = "<iframe src="
        iframe += svg
        iframe += " width=1920>"
        html_page.append(iframe)
        html_page.append("</iframe>")
        html_page.append("</div>")

    html_page.append("</body></html>")

    with open("index.html", 'w') as f:
        for line in html_page:
            f.write(line + '\n')

if __name__ == "__main__":
    combine()