class Twitter:

    def __init__(self):
        self.usertwe = {} # a users tweets
        self.following = {} # who a user follows
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.usertwe[userId] = self.usertwe.get(userId, [])
        self.usertwe[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = [userId] + list(self.following.get(userId, []))
        result = []
        for user in users:
            if user in self.usertwe and self.usertwe[user]:
                index = len(self.usertwe[user]) - 1
                count, tweetid = self.usertwe[user][index]
                heapq.heappush(heap, (count, tweetid, user, index))
        for i in range(10):
            if not heap:
                break
            count, tweet, user, index = heapq.heappop(heap)
            result.append(tweet)
            if index > 0:
                index -= 1
                count, tweetid = self.usertwe[user][index]
                heapq.heappush(heap, (count, tweetid, user, index))
        return result
            



    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId] = self.following.get(followerId, [])
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)