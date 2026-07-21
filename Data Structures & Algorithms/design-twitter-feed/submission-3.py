class Twitter:

    def __init__(self):
        self.time: int = 0
        self.followMap: defaultdict[int, set[int]] = defaultdict(set)
        self.tweetMap: defaultdict[int, list[(int, int)]] = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        # first get all the followees
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                idx = len(self.tweetMap[followee]) - 1
                t, tweetId = self.tweetMap[followee][idx]
                minHeap.append([t, tweetId, followee, idx - 1])
        
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            t, tweetId, followee, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            t, tweetId = self.tweetMap[followee][idx]
            if idx >= 0:
                heapq.heappush(minHeap, [t, tweetId, followee, idx - 1])    
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

