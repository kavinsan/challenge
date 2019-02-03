"""
    PLEASE NOTE THAT THIS VERSION OF THE COMMIT WAS AFTER THE TIME LIMIT!!!
    This commit was only for practicing without a stressful time limit

    Refer to older commit for the submitted version. Or this one if you'd like
"""

supplies = []
queries = []

results = []


def search(queries,supplies):
    #supplies => CITY,SUPPLIER,PRICE
    #query => CITY,DAY 

    for query in queries:
        cityQuery = query[0]
        day = int(query[1])
        queryResult = []
        for supply in supplies:
            citySupply = supply[0]
            supplier = supply[1]
            price = int(supply[2])

            if(supplier == 'A') & (day == 1) & (citySupply == cityQuery):
                price = price * 2
                queryResult.append(price)
                
            elif(supplier == 'B') & (day < 3) & (citySupply == cityQuery):
                queryResult.append(None)

            elif(supplier =='C') & (day >= 7) & (citySupply == cityQuery):
                price = price - (price*1/10)
                queryResult.append(price)

            elif(supplier =='D') & (day < 7) & (citySupply == cityQuery):
                price = price + (price*1/10)
                queryResult.append(price)


        results.append(sorted(queryResult, key=lambda x: (x is None, x)))
    
    [print(result) for result in results]


supply_rates = int(input("Enter the number of supply rates"))

count = 0
#Get the list of supply rates in the format of CITY,SUPPLIER,PRICE
while(count < supply_rates):

    supply = input(f"{count + 1}: ")
    if(len(supply.split(',')) != 3):
        continue
    else:
        supplies.append(supply.split(','))
        count = count + 1

num_queries = int(input("Enter the number of queries"));

count = 0
while(count < num_queries):

    query = input(f"{count + 1}: ")
    if(len(query.split(',')) != 2):
        continue
    else:
        queries.append(query.split(','))
        count = count + 1

search(queries,supplies)