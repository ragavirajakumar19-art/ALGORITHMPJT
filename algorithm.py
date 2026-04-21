# Portfolio Optimizer using Knapsack

budget = int(input("Enter your budget: "))
n = int(input("Enter number of assets: "))

profits = []
costs = []

# Taking input
for i in range(n):
    c = int(input(f"Enter cost of asset {i+1}: "))
    p = int(input(f"Enter profit of asset {i+1}: "))
    costs.append(c)
    profits.append(p)

# Knapsack DP
dp = [[0]*(budget+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, budget+1):
        if costs[i-1] <= w:
            dp[i][w] = max(profits[i-1] + dp[i-1][w-costs[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print("\nMaximum Profit:", dp[n][budget])

# Find selected items
w = budget
selected = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected.append(i-1)
        w -= costs[i-1]

print("\nSelected Investments:")
total_cost = 0
for i in selected:
    print(f"Asset {i+1} -> Cost: {costs[i]}, Profit: {profits[i]}")
    total_cost += costs[i]

print("\nTotal Cost Used:", total_cost)
print("Remaining Budget:", budget - total_cost)