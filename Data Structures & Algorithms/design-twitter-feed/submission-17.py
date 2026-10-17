from collections import defaultdict, deque
import heapq

class Twitter:

    def __init__(self):
        self.users = {} # userId:([followingIds], [tweetIds])
        self.tweets = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets += 1
        if userId in self.users:
            self.users[userId][1].append((-self.tweets, tweetId))
        else:
            self.users[userId] = ([], deque([(-self.tweets, tweetId)]))
        
        if len(self.users[userId][1]) > 10:
            self.users[userId][1].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
            
        tweets = [tup for tup in self.users[userId][1]]
        heapq.heapify(tweets)

        for followingId in self.users[userId][0]:
            for tup in self.users[followingId][1]:
                heapq.heappush(tweets, tup)
        
        acc = []
        for _ in range(10):
            if tweets:
                tup = heapq.heappop(tweets)
                acc.append(tup[1])
        
        return acc


    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.users:
            if followeeId not in self.users[followerId][0]: 
                self.users[followerId][0].append(followeeId)
        else:
            self.users[followerId] = ([followeeId], deque())

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.users:
            if followeeId in self.users[followerId][0]:
                self.users[followerId][0].remove(followeeId)
