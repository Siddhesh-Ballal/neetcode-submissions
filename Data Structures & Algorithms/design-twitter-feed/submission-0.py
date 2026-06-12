class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)    # userid -> set of followers
        self.tweetMap = defaultdict(list)    # userid -> list of ([count][tweetid])


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1        # (Python minheap -> most recent on top) if Java or other language, we could've used maxheap and incremented count instead


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []     # ordered from most recent to least recent
        minheap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minheap.append([count, tweetId, followeeId, index - 1])
        
        heapq.heapify(minheap)

        while minheap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: self.followMap[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)