def dfs(graph, initiateState, goal):
    explored = []
    stack = [[initiateState]]
    if initiateState == goal:
        return "OK"

    while stack:
        state = stack.pop(-1)
        node = state[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_state = list(state)
                new_state.append(neighbour)
                stack.append(new_state)
                if neighbour == goal:
                    return new_state
            explored.append(node)
    return "Sorry, the node you selected does not exist"


if __name__ == '__main__':
    peta = {'A': {'B'},
            'B': {'C', 'A'},
            'C': {'H', 'B', 'I', 'D'},
            'D': {'C', 'E', 'H', 'F'},
            'E': {'D'},
            'F': {'D', 'G'},
            'G': {'F', 'H'},
            'H': {'L', 'C', 'G', 'D'},
            'I': {'C', 'J', 'K'},
            'J': {'I'},
            'K': {'L', 'I'},
            'L': {'K', 'H'}}
    start = input("Start with: ")
    end = input("End with: ")
    print(dfs(peta, start, end))
