'''3. Remove Duplicates (Keep Order)
Return the values in the order they first appeared, without duplicates.
Input: ["apple", "banana", "apple", "kiwi", "banana"]
Output: ["apple", "banana", "kiwi"]'''

def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

"""What structure you chose and why: I chose a set to track items because it provides O(1) average time complexity for lookups, making it efficient for checking duplicates. The list is used to maintain the order of first appearances. Sets autimatically handle duplicates, which simplifies the logic significantly.

How the time limit shaped your decision: The time limit forced me to find a solution quickly and efficiently, leading me to use a set for fast membership testing. It seemed intuitive so I followed my first instinct. Honestly I didn't need the time limit to make this decision, but it reinforced my choice. 
I used very little of the total time figuring out what I wanted to do, I spent and the time limit never really came into being a factor as this took me a total of like 5 minutes.

What trade-offs or compromises you made under time pressure: I prioritized simplicity and clarity over more complex data structures that might offer marginally better performance in specific scenarios. This approach ensures the code is easy to understand and maintain.
I think even with a longer time limit I would have made the same choice, as it is the most straightforward and effective solution."""