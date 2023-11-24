import heapq

def minWait(allOrders):
    totalWaitTime = 0  # Initialize total waiting time to 0
    numOrders = len(allOrders)  # Get the number of orders
    if numOrders == 0:  # If there are no orders, return 0
        return 0
    pendingOrders = []  # Initialize a list for pending orders
    currentTime = allOrders[0][0]  # Set current time to the arrival time of the first order

    loop = True  # Start a loop to process orders
    while loop:  # Continue looping until all orders are processed
        while len(allOrders) != 0 and allOrders[0][0] <= currentTime:
            # Move orders from allOrders to pendingOrders if their arrival time is less than or equal to the current time
            order = heapq.heappop(allOrders)  # Pop the earliest order from allOrders
            heapq.heappush(pendingOrders, (order[1], order[0]))  # Push the order to pendingOrders based on cooking time
        if len(pendingOrders) != 0:
            # If there are pending orders, process the one with the shortest cooking time
            minWaitOrder = heapq.heappop(pendingOrders)  # Pop the order with the shortest cooking time
            waitTime = currentTime - minWaitOrder[1] + minWaitOrder[0]  # Calculate waiting time for this order
            totalWaitTime += waitTime  # Add the waiting time of this order to the total waiting time
            currentTime += minWaitOrder[0]  # Increment current time by the cooking time of the processed order
        else:
            # If there are no pending orders, increment current time
            currentTime += 1
        if len(pendingOrders) == 0 and len(allOrders) == 0:
            # If both allOrders and pendingOrders are empty, end the loop
            loop = False
    return totalWaitTime // numOrders  # Return the average waiting time

# Reading input and processing orders
n = int(input())  # Read the number of orders
allOrders = []
for i in range(n):
    line = input().split()  # Read each order
    l, t = int(line[0]), int(line[1])  # Parse arrival time and cooking time
    heapq.heappush(allOrders, (l, t))  # Add the order to allOrders heap based on arrival time
print(int(minWait(allOrders)))  # Print the integer part of the minimum average waiting time
