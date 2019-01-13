import wikipedia

var1 = input("Search Keyword: ")
print("Search: \n", wikipedia.search(var1))
try:

    print("Summary: \n", wikipedia.summary(var1))
except wikipedia.exceptions.DisambiguationError as e:
    print(e.option)

page = wikipedia.page(var1)
print("Page: ", page)
print("URL: ", page.url)
print("Title: ", page.title)
