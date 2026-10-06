def mobile_data_plans(plans, budget):

    n = len(plans)

    # DP table
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):

        price, data = plans[i - 1]

        for b in range(budget + 1):

            # Don't select the current plan
            dp[i][b] = dp[i - 1][b]

            # Select the current plan if affordable
            if price <= b:
                dp[i][b] = max(
                    dp[i][b],
                    data + dp[i - 1][b - price]
                )

    # Maximum data
    max_data = dp[n][budget]

    # Find selected plans
    selected = []
    b = budget

    for i in range(n, 0, -1):

        if dp[i][b] != dp[i - 1][b]:

            selected.append(i)
            price, data = plans[i - 1]
            b -= price

    selected.reverse()

    return max_data, selected


# Available mobile data plans
plans = [
    (100, 5),    # Plan 1
    (150, 8),    # Plan 2
    (200, 12),   # Plan 3
    (250, 15),   # Plan 4
    (300, 20)    # Plan 5
]

budget = 500

max_data, selected = mobile_data_plans(plans, budget)

print("Budget:", budget)

print("\nSelected Plans:")

total_cost = 0

for i in selected:
    price, data = plans[i - 1]

    print(
        f"Plan {i}: ₹{price} -> {data} GB"
    )

    total_cost += price

print("\nTotal Cost:", total_cost)
print("Maximum Data:", max_data, "GB")
