with open("Output.ini", "a") as text_file:
    text_file.write("\nPurchase Amount: %s" % 5)
with open("Output.ini", "r") as text_file:
    print text_file.read()