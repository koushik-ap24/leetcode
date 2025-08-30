from typing import List, Tuple


def time_to_minutes(t: str) -> int:
    h, m = map(int, t.split(":"))
    return h * 60 + m

def findLunchMates(slots: List[Tuple[int, int, str]], availability: Tuple[int, int]):
    ## Interval overlap
    slots_in_minutes = [
        (time_to_minutes(start), time_to_minutes(end), employee)
        for start, end, employee in slots
    ]
    avail_start, avail_end = time_to_minutes(availability[0]), time_to_minutes(availability[1])

    slots_in_minutes.sort(key=lambda x: x[1])  # sort by end time
    res = []

    for start, end, employee in slots_in_minutes:
        if end >= avail_start and (start < avail_end):
            overlapX, overlapY = max(start, avail_start), min(end, avail_end)
            if overlapY - overlapX >= 20:
                res.append((employee, overlapY - overlapX))
        
    
    # Rank suitable employees based on minutes, then alphabetical
    res.sort(key=lambda x: (-x[1], x[0]))
    return res

# Test the above function
slots = [
    ("13:00", "14:00", "Alice"),
    ("13:30", "14:10", "Bob"),
    ("14:00", "15:00", "Charlie"),
    ("12:00", "13:20", "David"),
    ("13:50", "14:30", "Eve"),
    ("14:50", "15:30", "Bruh")
]
availability = ("13:20", "14:20")
print(findLunchMates(slots, availability))

