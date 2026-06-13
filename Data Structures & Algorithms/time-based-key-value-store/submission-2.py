class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        l = 0
        if key in self.timemap:
            r = len(self.timemap[key])-1
        else:
            return ""
        while(l<=r):
            mid = (l+r)//2
            if self.timemap[key][mid][1] == timestamp:
                return self.timemap[key][mid][0]
            elif self.timemap[key][mid][1]>timestamp:
                r = mid-1
            else:
                l=mid+1
        return self.timemap[key][r][0] if r>-1 else ""

