import heapq
from typing import List


class TaskManager:
    ## Approach: HashMap + Max Heap
    ## Intuition: We can use a hashmap to store the taskId to (priority, userId) mapping
    ## and a max heap to get the task with the highest priority
    ## For edit and remove operations, we can use lazy deletion in the heap
    ## TC: O(log n) for add, edit, execTop and O(1) for rmv
    ## SC: O(n) for the hashmap and heap

    def __init__(self, tasks: List[List[int]]):
        self.taskMap = {}
        self.priorityHeap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (priority, userId)
        heapq.heappush(self.priorityHeap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = (self.taskMap[taskId])[1]
        self.taskMap[taskId] = (newPriority, userId)
        heapq.heappush(self.priorityHeap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        self.taskMap.pop(taskId)

    def execTop(self) -> int:
        # Lasy Deletion
        while len(self.priorityHeap) > 0 and (-self.priorityHeap[0][1] not in self.taskMap or -self.priorityHeap[0][0] != self.taskMap[-self.priorityHeap[0][1]][0]):
            heapq.heappop(self.priorityHeap)
        
        if len(self.priorityHeap) == 0:
            return -1
        
        _,taskId = heapq.heappop(self.priorityHeap)
        userId = self.taskMap[-taskId][1]
        self.taskMap.pop(-taskId)
        return userId
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()