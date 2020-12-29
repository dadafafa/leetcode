class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)  # type = set
        # write your code here
        queue = collections.deque([(start,0)])
        visited = [start]
        distance = 0
        curr_layer = -1
        while queue:
            
            next_word,layer = queue.popleft()
            if layer != curr_layer:
                curr_layer = layer
                distance  +=1

            if next_word == end:
                return distance
            else:
                possible_word=self.possibleWord(next_word)
            for pw in  possible_word:
                if pw in dict:
                    dict.remove(pw)
                    queue.append((pw,curr_layer+1))
        return 0
    def possibleWord(self,word):
        words=[]
        for idx,wrd in enumerate(word):
            for new in "abcdefghijklmnopqrstuvwxyz":
                if new == wrd:
                    continue
                else:
                    new_word = word[:idx]+new+word[idx+1:]
                    words.append(new_word)
        return words
