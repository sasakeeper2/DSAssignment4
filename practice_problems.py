"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    x = 0
    for id in product_ids:
        if product_ids.count(id) > 1:
            x += 1
        else:
            continue
    if x > 0:
        return True
    else:
        return False
'''Why this data structure fits the task: I used a list to store the product IDs because it allows for easy iteration and checking of each ID. 
 I stayed away from using sets to avoid losing the count of duplicates, as sets automatically remove duplicates.
 What operations are performed and their expected runtime: The main operation performed is counting occurrences of each ID using the count() method, which has a time complexity of O(n) for each ID. 
 This results in an overall time complexity of O(n^2) in the worst case, which is not optimal for large lists. 
 However, given the constraints of the problem and the need to check for duplicates, this approach is straightforward and easy to implement.'''

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task):
        self.task_queue.append(task)

    def remove_oldest_task(self):
        if self.task_queue:
            return self.task_queue.pop(0)
        return None
'''Why this data structure fits the task: A list is suitable for this task because it maintains the order of insertion, which is essential for a queue-like behavior.
 Lists also allow for easy appending of new tasks at the end.
 What operations are performed and their expected runtime: I used a list to maintain the order of tasks. Adding a task is O(1) since it appends to the end of the list.
 Removing the oldest task is O(n) because it involves shifting all other elements in the list.'''


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.tracker = set()

    def add(self, value):
        self.tracker.add(value)

    def get_unique_count(self):
        return len(self.tracker)

'''Why this data structure fits the task: This data structure is ideal because sets inherently store unique values, making it easy to track and count distinct integers efficiently by simply finding the length of the set.
 this is the most straightforward and efficient way to achieve the goal.
 What operations are performed and their expected runtime: Adding a value to the set is O(1) on average, and getting the count of unique values is also O(1) since it involves checking the length of the set. 
 This ensures that both operations are efficient even as the number of values increases.'''