from datetime import datetime

simdi = datetime.now()

products = {'asparagus': [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7],
                 'apples': [20, 5], 'banana': [10, 8], 'berries': [30, 3],
                 'eggs': [50, 2], 'mixed fruit juice': [0, 8], 'fish sticks': [25, 12],
                 'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8], 'grape juice': [10, 9]}


usersdic = {"Ahmet": "1234", "Meryem": "4321"}

baskets = {} # Products = {username:{urun:[amount,price]}}
itemcek = list(baskets)

def loginuser():
    print("****Welcome to Xtreme Online Market****")
    complete = False
    while not complete:
        username = input("Username:")
        password = input("Password:")
        if not username in usersdic.keys():
            print("Input username again!")
            continue
        if password == usersdic[username]:
            print(" Welcome", username, "!")
            complete = True
        else:
            print("Input password again")
    services(username)

def services(username):
    print("Please choose one of the following options by entering the corresponding menu number.")
    print("Please choose one of the following services: \n1. Search for a product \n2. See Basket \n3. Check Out \n4. Logout\n5. Exit\nYour Choice:")
    num = int(input(">>>"))
    complete = False
    while not complete:
        if num == 1:
            Search(username)
            break
        if num == 2:
            SeeBasket(username)
            break
        if num == 3:
            CheckOut(username)
            break
        if num == 4:
            Logout(username)
            break
        if num == 5:
            print("Exited")
            break
        else:
            num = int(input("Please enter valid number"))

def Search(username):

    searching = input("What are you searching for?")
    complete = False
    while not complete:
        temp = []
        for product in products.keys():
            if searching in product:
                temp.append(product)
 
        count = 1
        if temp:
            for product in temp:
                print(f"{count}. {product}")
                count +=1
        
            select = input("Enter the number of the requested product")
            amount, price = products[temp[int(select)-1]][0], products[temp[int(select)-1]][1]
            print(f"Selected Product: {temp[int(select)-1]}, Amount: {amount}, Price: {price}")
            
            
            while True:
                tane= int(input("How many items you need ?"))
                if tane <= amount:
                    products[temp[int(select)-1]][0] -= tane
                    print(f"Adding {tane} of {temp[int(select)-1]} to basket \n going back to main menu")
                    baskets.setdefault(username,{}) # Products = {username:{urun:[amount,price]}}
                    
                    baskets[username][temp[int(select)-1]] = [tane, price]# Products = {username:{urun:[amount,price]}}
                    complete = True
                    break
                    
                else:
                    print("We dont have enough amount")
        
        else:
            searching = input("Your search did not match any items. Please try something else (Enter 0 for main menu):")
        
    services(username)
            


def SeeBasket(username):
    flag = 0
    temp = {}
    print("Your basket now contains:\n")
    for name, dict in baskets.items(): # Products = {username:{urun:[amount,price]}}
        if name == username:
            flag = 1
            count = 1
            for urun, liste in dict.items():
                print(f"{count}. Product:{urun} \t Amount:{liste[0]} \t Price:{liste[1]}")
                temp[count] = [urun, liste[0], liste[1]] # [urun, amount, price]
                count += 1
                
            print()

    if flag:
        print("Please Choose an option:\n1.Update amount\n2.Remove an item\n3.Check out\n4.Go back to main menu.")
        no= int(input("Your selection:"))
        if no == 1:

            complete = False
            while not complete:
                secme=int(input("Please select which item to change its amount: "))
                degis=int(input("Please type the new amount: "))
                if secme in temp:
                    if degis <= products[temp[secme][0]][0] + baskets[username][temp[secme][0]][0]:
                        products[temp[secme][0]][0] += baskets[username][temp[secme][0]][0]
                        products[temp[secme][0]][0] -= degis
                        baskets[username][temp[secme][0]][0] = degis
                        break
                    else:
                        print("we dont have that amount")
            services(username)            
        
        if no == 2:
            complete = False
            while not complete:
                secme=int(input("Please select which item to remove"))
                if secme in temp:
                    products[temp[secme][0]][0] += baskets[username][temp[secme][0]][0]
                    del baskets[username][temp[secme][0]]
                    break
                        
            services(username)            


        if no == 3:
           CheckOut(username)
        if no == 4:
           services(username)
    
    else:
        print("No product in your basket")



def CheckOut(username):
    print("Processing your receipt...\n\n************************************\n******* Xtreme Online Market ********\n************************************\n44 44 0 34\nxtreme.edu.tr\n------------------------------------")
    
    total = 0
    for name, dict in baskets.items(): # Products = {username:{urun:[amount,price]}}
        if name == username:
            
            for urun, liste in dict.items():
                print(f"+ Product:{urun} \t Amount:{liste[0]} \t Price: {liste[0]*liste[1]}")
                total += liste[0]*liste[1]
            print()
    print(f"Total Price: {total}")
    print("         ", simdi.strftime("%Y-%m-%d %H:%M:%S"))
    print("\n------------------------------------\n************************************\n************* Thank You **************\n************************************\n")

    
    services(username)


def Logout(username):

    print(f"Good Bye {username} !")
    loginuser()






loginuser()