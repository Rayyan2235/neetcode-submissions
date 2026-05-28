class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Arr of Cpu tasks where tasks[i] = Upper case letters from A-Z
        1 cycle = 1 cpu task, order doesnt matter
        same tasks cant be side by side, must be seperated by n cpu cycles
        return min number of CPU cycles to complete all tasks

        '''

        count = Counter(tasks) # Hashmap that stores the count of items too
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        time = 0 # To track time
        q = deque() #init an empty queue, # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time+=1 

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # we are adding 1 because we are removing 1 instance from the item
                if cnt: # Only if the cnt is non 0 if it is then we dont pass it to queue
                    q.append([cnt, n + time]) # The Queue will contain the cnt of the item after its been picked once and with its wait time (Or pos where its allowed to be returned again)
                    #appending a pair of values
            if q and q[0][1] == time:

                popped = q.popleft()[0] # Going to pop the pair of values but we only want the cnt
                heapq.heappush(maxHeap, popped)
        return time



        
        