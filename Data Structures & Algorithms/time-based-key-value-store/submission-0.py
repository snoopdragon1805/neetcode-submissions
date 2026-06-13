class TimeMap:

    def __init__(self):
        self.timemap = []
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.append([key,value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        for i in self.timemap:
            if i[0] == key and i[2] <=timestamp:
                res = i[1]
        return res

