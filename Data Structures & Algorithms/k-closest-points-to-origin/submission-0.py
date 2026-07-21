class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        dist_points = defaultdict(list)

        for i in range(len(points)):
            coord = points[i]
            distance = self.eculideanDistance(coord)
            
            dist_points[distance].append(coord)
            heapq.heappush(min_heap, distance)
        
        print(min_heap)        
        
        res = []
        for i in range(k):
            min_dist = heapq.heappop(min_heap)
            
            for coord in dist_points[min_dist]:
                res.append(coord)
                if len(res) == k:
                    return res 

        return res
        
    def eculideanDistance(self, coord):
        x2,y2 = coord[0], coord[1]
        return math.sqrt(((0 - x2) ** 2) + ((0 - y2) ** 2)) 