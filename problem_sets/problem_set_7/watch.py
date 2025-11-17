# Extracting a youtube link from a html text, and then reformatting it to a much shorter link

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
                            # initilal: matches = re.search(r"http[s]?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)", s)     optional s, optional www. and we allow only alphanumeric char for address, also grouped to use in formatting
    matches = re.search(r'<iframe .*src="http[s]?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"', s)
    if matches:
        address = matches.group(2)
        result = "https://youtu.be/" + address
        return result


if __name__ == "__main__":
    main()
