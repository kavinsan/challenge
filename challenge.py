
#N the number of supplier rates (1 < N < 1,000,000)
#The next N lines will contain the CITY,SUPPLIER,PRICE <= no spaces only commas

supplier_rates  = int(input("Enter the number of supplier rates: "))

while True:
    if((supplier_rates > 1) & (supplier_rates < 1000000)):
        break;
    else:
        supplier_rates = int(input("Enter the number of supplier rates between 1 and 1,000,000: "))


count = 0
supplies = []

while True:
    #Make sure only N inputs are taken
    if(count == int(supplier_rates)):
        break;
    
    supply = input()
    
    #Separating every concatentation of lines with a space but every supply rate line by commas
    supply = supply.split(',')
    if(len(supply) != 3):
        print("Incorrect format!")
    else:
    
        supplies.append(supply)
        #Only count if entry is successful
        count = count + 1


num_queries = int(input("Enter the number of queries: "))

while True:
    if((num_queries > 1) & (num_queries < 100)):
        break;
    else:
        num_queries = int(input("Enter the number of supplier rates between 1 and 1,000,000: "))

count = 0
queries = []

while True:
    #Make sure only N inputs are taken
    if(count == int(num_queries)):
        break;
    
    query = input()
    
    query = query.split(',')
    if(len(query) != 2):
        print("Incorrect format!")
    else:
        queries.append(query)
        #Only count if entry is successful
        count = count + 1        

    query(queries,supplies)

def query(queries, supplies):
    resultsA = [];
    resultsB = [];
    resultsC = [];
    resultsD = [];

    for queries in queries:
        city = queries.pop();
        days = int(queries.pop());

        for supply in supplies:
            citySupply = supply[0];
            supplier = supply[1];
            price = float(supply[2]);

            if(supplier == 'A'):
                if(days == 1):
                    price *= 2;
                    resultsA.append(round(price,2))

            elif(supplies == 'B'):
                if(days < 3):
                    resultsB.append(None)
                else:
                    resultsB.append(round(price,2))

            elif(supplies == 'C'):
                if(days >= 7):
                    price -= (price * 1/10);
                    resultsC.append(round(price,2))

            elif(supplies == 'D'):
                if(days < 7):
                    price += (price * 1/10);
                    resultsD.append(round(price,2))

    print(resultsA.sort())
    print(resultsB.sort())
    print(resultsC.sort())
    print(resultsD.sort())


# Q: The number of user queries (1 < Q < 100) 
#Query: CITY,DATE,PRICE separated by commas NOT spaces
#Days D until check-in is 1 <= D <= 20

