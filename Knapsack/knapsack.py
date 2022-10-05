# #Time complexity : O(nlogn)
def fractionalknapsack(profit,weight,capacity):
    index=list(range(len(profit)))                     #O(1)
    ratio=[p/w for p,w in zip(profit,weight)]          #O(n)
    #sort the index w.r.t. ratio in descending order
    index.sort(key=lambda i:ratio[i],reverse=True)     #O(nlogn)
    fraction=[0]*len(profit)                           #O(1)
    total_profit=0                                     #O(1)
    
    for i in index:                                    #O(n)
        if weight[i]<=capacity:
            fraction[i]=1
            capacity=capacity-weight[i]
            total_profit=total_profit+profit[i]
        else: #fractional/partial selection of the product
            fraction[i]=capacity/weight[i]
            total_profit=total_profit+(profit[i]*fraction[i])
            break
        
    return total_profit,fraction                      #O(1)
    
profit=[100,60,120]
weight=[20,10,30]
capacity=50
profit,fraction=fractionalknapsack(profit,weight,capacity)
print("total profit: ",profit)
print("fractional part: ",fraction)








# #program instead of fractional knapsack do 0/1 knapsack

# def knapsack(profit,weight,capacity):
#     index = list(range(len(profit)))
#     ratio = [p/w for p,w in zip(profit,weight)]
#     index.sort(key = lambda i:ratio[i], reverse = True)
#     fraction = [0]*len(profit)
#     totalProfit = 0

#     for i in index:
#         if weight[i] <= capacity:
#             fraction[i] = 1
#             capacity = capacity - weight[i]
#             totalProfit = totalProfit + profit[i]

#     return totalProfit, fraction

# profit = [50,100,150,200]
# weight = [8,16,32,40]
# capacity = 64
# profit,fraction = knapsack(profit,weight,capacity)
# print("total Profit: ",profit)
# print("fractional part: ",fraction)