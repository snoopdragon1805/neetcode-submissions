class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId,tweetId])
        if userId not in self.followers:
            self.followers[userId] = [userId]
        elif userId not in self.followers[userId]:
            self.followers[userId].append(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        count = 0
        i=-1
        if userId not in self.followers:
            self.followers[userId] = [userId]
        while count<10 and i!=-(len(self.tweets)+1):
            tweet = self.tweets[i]
            if tweet[0] in self.followers[userId]:
                res.append(tweet[1])
                count+=1
            i-=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = [followerId]
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)         

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followerId != followeeId:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
