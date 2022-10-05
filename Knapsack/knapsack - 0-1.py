#program for 0/1 knapsack
#Time complexity : O(nlogn)
def knapsack(profit,weight,capacity):
    index=list(range(len(profit)))                     #O(1)
    ratio=[p/w for p,w in zip(profit,weight)]          #O(n)
    index.sort(key=lambda i:ratio[i],reverse=True)     #O(nlogn)
    fraction=[0]*len(profit)                           #O(1)
    total_profit=0                                     #O(1)

    for i in index:                                    #O(n)
        if weight[i]<=capacity:
            fraction[i]=1
            capacity=capacity-weight[i]
            total_profit=total_profit+profit[i]

    return total_profit,fraction                      #O(1)

profit = [100,200,350,500]
weight = [6,12,34,48]
capacity = 50
profit,fraction = knapsack(profit,weight,capacity)
print("total Profit: ",profit)
print("fractional part: ",fraction)