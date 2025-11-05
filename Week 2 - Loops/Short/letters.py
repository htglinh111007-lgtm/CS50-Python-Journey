def main():
    names = ["Mario", "Daisy", "Luigi", "Yoshi", "Bowser"]
    for i in range (len(names)):
        print(write_letters(names[i],"Princess Peach"))
def write_letters(receiver, sender):
    return f"""
    Dear {receiver}, 
    Your are cordially invited to a ball at
    Peach's Castle this evening at 7:00 PM.
    Sincerely
    {sender}
    """
main()