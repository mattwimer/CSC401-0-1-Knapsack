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
                