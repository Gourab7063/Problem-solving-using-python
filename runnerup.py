# Read input
n = int(input("Enter the number of scores: "))
scores = list(map(int, input("Enter the scores separated by space: ").split()))

# Find the maximum score
max_score = max(scores)

# Remove all occurrences of the maximum score
while max_score in scores:
    scores.remove(max_score)

# Find the runner-up score
runner_up_score = max(scores)

print(runner_up_score)

