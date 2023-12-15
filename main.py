def knapsack(items, weights, values, capacity):
    n = len(items)
    dp = [[0 for j in range(capacity+1)] for i in range(n+1)]

    for i in range(n+1):
        for w in range(capacity+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    selected_items = []
    i = n
    w = capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i)
            w = w - weights[i-1]
        i = i-1
    
    #       total value,     indices of items
    return (dp[n][capacity], selected_items)

items = ["genie's lamp", "pot lid", "umbrella", "gold bar", "dollar bill"]
weights = [5, 10, 3, 25, 1]
values = [40, 5, 7, 100, 1]
print(knapsack(items, weights, values, 12))
print(knapsack(items, weights, values, 13))
print(knapsack(items, weights, values, 20))
print(knapsack(items, weights, values, 26))
