def kingdomDivision(n, roads):
    mod = 1000000007
    adj = {}

    # Building the adjacency list for the graph
    for item in roads:
        parent, child = item
        if parent not in adj:
            adj[parent] = []
        if child not in adj:
            adj[child] = []
        adj[parent].append(child)
        adj[child].append(parent)

    # Creating iterators for each node's adjacency list
    iter_list = {key: iter(adj[key]) for key in adj}

    # Start DFS using a stack
    stack = [1]
    good_conf, bad_conf = {}, {}
    visited = {1}
    children = {}

    while stack:
        source = stack[-1]
        iterator = iter_list[source]

        try:
            to = next(iterator)
            if to not in visited:
                stack.append(to)
                visited.add(to)
                if source not in children:
                    children[source] = []
                children[source].append(to)

        except StopIteration:  # Finished exploring a node
            key = stack.pop()
            good_conf[key] = 1
            bad_conf[key] = 1

            if key not in children:
                # Leaf node
                good_conf[key] = 0
                bad_conf[key] = 1
                continue

            # Update configurations for the current node based on its children
            for child in children[key]:
                good_conf[key] = (good_conf[key] * (2 * good_conf[child] + bad_conf[child])) % mod
                bad_conf[key] = (bad_conf[key] * good_conf[child]) % mod

            # Adjusting good configurations to exclude bad ones
            good_conf[key] = good_conf[key] - bad_conf[key]
            while good_conf[key] < 0: 
                good_conf[key] += mod

    # Return the total number of ways to partition the kingdom
    return (good_conf[1] * 2) % mod
