def findCheapestPrice(n,flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """

    # Adjacency list as a hash map
    flight_map = collections.defaultdict(list)
    for origin, destination, cost in flights:
        flight_map[origin].append((destination, cost))

    # Initially push 'src' into the heap with stops=-1 and cost=0
    heap = []
    heapq.heappush(heap, (0, -1, src))  # (cost,stops,destination)
    visited = set()  # Use a set to avoid unnecessary nodes in the heap, in case the graph has cycles
    while heap:
        cost, stops, city = heapq.heappop(heap)
        visited.add(city)

        if city == dst:
            return cost

        if stops < K:  # can add another stop
            for next_city, flight_cost in flight_map[city]:
                if next_city not in visited:
                    # pushes the next city into the heap and increse total cost and stops
                    heapq.heappush(heap, (cost + flight_cost, stops + 1, next_city))

    return -1

