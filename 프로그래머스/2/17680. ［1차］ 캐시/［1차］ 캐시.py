def solution(cacheSize, cities):
    if cacheSize == 0 :
        return len(cities) * 5;
    
    class Cache:
        def __init__(self, size):
            self.size = size
            self.cache = dict()
        def put(self, time, entry):
            if self.size == len(self.cache):
                min_key = min(self.cache, key=self.cache.get)
                del self.cache[min_key]
            self.cache[entry] = time
        def get(self, time, entry):
            if entry in self.cache:
                self.cache[entry] = time
                return True
            else:
                return False;
    
    cache = Cache(cacheSize)
    answer = 0
    for idx in range(0, len(cities)):
        next = cities[idx].lower()
        if cache.get(idx, next):
            answer+=1
        else:
            cache.put(idx, next)
            answer+=5
        
        
    return answer

