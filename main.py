import json
import httpx

more = False

def display_joke():
    response = httpx.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()

    print(data['setup'])
    print(data['punchline'])


display_joke()
while more == False:
    user_input = input("Do you want to hear another joke? (y/n)")
    if user_input == "y":
        display_joke()
    else:
        more = True
        print("Goodbye!")