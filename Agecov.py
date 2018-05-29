def AgeCoversion():
    seconds_or_years = input("Give me seconds(s) or years(y):")
    if seconds_or_years == "s":
        user_value = input("Enter no of seconds you lived for :")
        print("You lived for {} years".format(int(user_value)/60/60/24/365))
    elif seconds_or_years == "y":
        user_value = input("Enter no of years you lived for:")
        print("You lived for {} seconds".format(int(user_value)*60*60*24*365))

AgeCoversion()