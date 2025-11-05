
def convert(time_strg):
    hour, minute = time_strg.split(":")
    hour = float(hour)
    minute = float(minute)
    return hour + (minute/60)
def main():
    time_strg = input("What time is it? ")
    time = convert(time_strg)
    if 7 <= time <= 8:
        print ("It's your breakfast time! ")
    elif 12<= time <= 13:
        print ("It's your lunch time! ")
    elif 18<= time <= 19:
        print ("It's your dinner time! ")
    else:
        print ("Not pretty a good time for a meal ")
main()
