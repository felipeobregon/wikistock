import wikipedia

# Set the language of the Wikipedia search (optional, defaults to English)
wikipedia.set_lang("en")

# Perform a Wikipedia search for "Bananas flying over new york"
search_results = wikipedia.search("Bananas flying over new york")

# Get the Wikipedia page object for the first search result
page = wikipedia.page(search_results[0])

# Print the URL of the first search result
print(page.url)
