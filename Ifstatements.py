value = int(input("Enter a price you want to sell at: "))
if value < 100:
    print("You can buy the chair")
elif value == 100:
    print("If you really want you can buy it")
else:
    print("You no need to buy this chair")