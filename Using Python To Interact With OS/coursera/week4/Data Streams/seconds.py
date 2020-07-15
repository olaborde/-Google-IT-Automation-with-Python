def to_seconds(hours, minutes, seconds):
    return hours*3600 + minutes*60 + seconds
print("Welcome to the time converter")

cont ='y'
while(cont.lower() == 'y'):
    hours = int(input("Enter the number of hours: \n"))
    minutes = int(input("Enter the number of minutes: \n"))
    seconds = int(input("Enter the number of seconds: \n"))
    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    cont = input("Do you want to do another conversation? [y to continue] ")
print("Good bye")    