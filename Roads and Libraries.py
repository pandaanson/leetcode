# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_lib <= c_road:
        # Cheaper to build a library in each city
        return n * c_lib

    def dfs(city, adj_list, visited):
        visited.add(city)
        for neighbour in adj_list[city]:
            if neighbour not in visited:
                dfs(neighbour, adj_list, visited)

    adj_list = {city: [] for city in range(1, n + 1)}
    for u, v in cities:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = set()
    libraries = 0
    for city in range(1, n + 1):
        if city not in visited:
            dfs(city, adj_list, visited)
            libraries += 1

    roads = n - libraries
    return libraries * c_lib + roads * c_road

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
