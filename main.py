from dynamic_programming import dynamic_knapsack
from greedy_algorithm import knapsack_greedy

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
greedy_result = knapsack_greedy(weights, values, capacity)
dynamic_result = dynamic_knapsack(weights, values, capacity)
print("Maximum Value:", greedy_result)
print("Maximum Value:", dynamic_result)