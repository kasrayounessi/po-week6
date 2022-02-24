from collections import defaultdict

def findLargestPandigit(num):
    products = defaultdict()
    digitIncluded = defaultdict()

    for i in range(1,10):
        products[i] = []
        digitIncluded[i] = []

    for i in range(1, num+1):
        current_product = str(num*i)
        starting_digit = int(current_product[0])
        acceptable_entry = True
        
        for char in current_product:
            if current_product.count(char) > 1:
                acceptable_entry = False
                break
            if '0' in current_product:
                acceptable_entry = False
                break
            digitIncluded[int(char)].append(current_product)

        if acceptable_entry:
            products[starting_digit].append(current_product)
    
    all_products = []
    for i in reversed(range(1, 10)):
        if products[i]:
            products[i] = sorted(products[i], reverse=True)
            all_products += products[i]
    
    if not all_products:
        return 'No pandigit exists'
    
    return all_products



        

            
         

    print(all_products)
    print(digitIncluded)

    # products = set()
    # highest_digit = 
    # for i in range(num+1):
    #     if i == 0:
    #         continue
    #     products.add(num*i)
    

print(findLargestPandigit(99))

