def knapsack_0_1(weights, values, capacity):
    n = len(weights)
    # Inisialisasi tabel DP dengan ukuran (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Membangun tabel DP
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Mengembalikan nilai maksimum yang dapat diambil dari knapsack
    return dp[n][capacity]

# Contoh Penggunaan
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
result = knapsack_0_1(weights, values, capacity)
print("Maximum Value:", result)