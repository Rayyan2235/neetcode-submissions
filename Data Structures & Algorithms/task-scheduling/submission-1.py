class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        '''
        1st: all the letters in tasks -assign them to a specific letter and have a count for how many times its been called
        I want to second take the first TYPE of letter in the tasks and add it once
        Then fill in n gaps, then input that same letter the amount of times called in tasks

        '''

        count = Counter(tasks) # Find the count for each letter. NOTE COUNTER is a pref hashmap
        #Max heap
        maxH = [-cnt for cnt in count.values()]
        heapq.heapify(maxH)
        # Created a min heap with negative val

        #Creating a q to make it more organized 
        q = deque() # Storing pairs of [-cnt, idleTime] idleT = time + n
        time = 0
        while maxH or q:
            time += 1
            if maxH:
                cnt = 1 + heapq.heappop(maxH)
                if cnt:
                    # Update the q
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxH, q.popleft()[0])
        return time


        