DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
class Types:
    empty = 0
    blocked = 1
    target = 2
    
class Solution:
    """
    @param targetMap: 
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here
        rows = len(targetMap)
        cols = len(targetMap[0])
        
        # key: points, value: steps
        visited = {}
        
        # add the 1st point (0, 0)
        visited[(0, 0)] = 0
        frontier = [(0, 0)]
        
        while frontier:
            nextFrontier = []
            for x, y in frontier
                for dx, dy in DIRECTIONS:
                    nextX, nextY = x + dx, y + dy
                    # check if out of range
                    if nextX < 0 or nextX >= rows or nextY < 0 or nextY >= cols:
                        continue
                    
                    # check if reachable
                    if targetMap[nextX][nextY] == Types.blocked:
                        continue
                    
                    # check if visited
                    if (nextX, nextY) in visited:
                        continue
                    
                    # check if get to the target
                    if targetMap[nextX][nextY] == 2:
                        return visited[(x, y)] + 1
                        
                    visited[(nextX, nextY)] = visited[(x, y)] + 1
                    
                    nextFrontier.append((nextX, nextY))
                    
            frontier = nextFrontier
        
        return -1
                
            