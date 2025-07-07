import httpx

def get_joke():
    wantofjoke = input("What type of joke do you want? (General, Programming, Knock-knock): ").lower()
    valid_types = ["general", "programming", "knock-knock"]

    if wantofjoke not in valid_types:
        print("That's not a valid joke type.")
        return

    url = f"https://official-joke-api.appspot.com/jokes/{wantofjoke}/random"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()[0] 
        print(f"\n({data['type']})")
        print(data['setup'])
        print(data['punchline'])
        global jokes_seen
        jokes_seen += 1
    else:
        print("Error, Too many uses, try again in around 15 minutes.")

jokes_seen = 0

more = True
while more == True:
    get_joke()
    user_input = input("Do you want to hear another joke? (y/n)")
    if user_input == "n":
        more = False
        print(f"You have seen {jokes_seen} jokes.")
        print("Goodbye!")
    else:
        more = True
       
