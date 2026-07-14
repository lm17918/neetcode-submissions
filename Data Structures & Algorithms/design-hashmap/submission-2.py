class MyHashMap:

    def __init__(self):
        self.dictmap={}
        

    def put(self, key: int, value: int) -> None:
        self.dictmap[key]=value
        

    def get(self, key: int) -> int:
        if key not in self.dictmap:
            return -1
        
        return self.dictmap[key]

    def remove(self, key: int) -> None:
        if key in self.dictmap:
            self.dictmap[key]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)