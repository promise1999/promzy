import formatters
total = 0
items=[]
while True:
    item_name = input("enter the name of item purchase: ")
    amount = float(input("enter the amount in pounds: "))
    cost_per_pound = float(input("enter the cost per pound: "))
    
    total_cost = cost_per_pound * amount
    total += total_cost

    d={"name":item_name,"amount":amount,"cost":cost_per_pound,"all_cost":total_cost}
    # Add the dictionary d to the items list
    items.append(d)
    
    cont = input("do you wish to continue: Y or N ")
    if cont.lower() != "y":
        break 
    
#Print out all values entered
    for item in items:
        print("Item name: {}".format(item["name"]))
        print("Item amount: {}".format(formatters.as_weight_in_pounds(item["amount"])))
        print("Item cost: {}".format(formatters.as_dollars(item["cost"])))
        print("Total cost per item: {}".format(formatters.as_dollars(item["all_cost"])))
    
        print("Total Cost: {}".format(formatters.as_dollars(total)))
    