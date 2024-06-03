while True:
    destination = input()
    if destination == "End":
        break
    
    budget = float(input())
    saved_amount = 0.0
    
    while saved_amount < budget:
        saved_amount += float(input())
    
    print(f"Going to {destination}!")