def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} crackers!")
    print("Man that's enough for a party")
    print("Get a blanket!\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variable numbers directly")
amount_of_cheese = 25
amount_of_crackers = 30
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do math inside too:")
cheese_and_crackers(10 + 15, 30+12)

print("And we can combinethe two, variables and math")
cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 15)
