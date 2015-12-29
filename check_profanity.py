import urllib

#Open the movie quotes file 
movie_file = open("/Users/Akshay/downloads/movie_quotes.txt")

#Read the quotes
quotes = movie_file.read()

#print(quotes)

#Make a connection to the URL for checking profane words
connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + quotes)

#Fetch response from the profanity check link
response = connection.read()
print(response)
#Print response
if("true" in response):
    print("Profanity Alert !!")
else:
    print("No profane word found in the list !!")
print(connection.code)
print(connection.headers)

connection.close()
