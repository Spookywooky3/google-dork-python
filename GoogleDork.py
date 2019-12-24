try:
    from googlesearch import search
    from enum import Enum
except ImportError:
    print("Error importing search module...")

dork = input("Please enter the search query you'd like to use: ")
amount = input("Please enter the amount of websites to display: ")
interval = input("Please enter the time interval between requests: ")
req = 0

for i in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=int(interval)):
    print(i)
    req += 1
    if req >= int(amount):
        break;
