n = int(input())
s = input()

# Initialize a set to store the unique fish species
unique_species = set()

# Initialize a dictionary to store the frequency of each fish species
species_freq = {}

# Calculate the frequency of each fish species
for fish in s:
    if fish not in species_freq:
        species_freq[fish] = 0
    species_freq[fish] += 1

# Initialize the maximum ecological score
max_score = 0

# Iterate through all possible partition points
for i in range(1, n):
    # Add fish species in the left partition to unique_species set
    for j in range(i):
        unique_species.add(s[j])

    # Calculate the ecological score of the left partition
    left_score = len(unique_species)

    # Calculate the ecological score of the right partition
    right_score = len(species_freq) - left_score

    # Update the maximum ecological score if necessary
    if left_score + right_score > max_score:
        max_score = left_score + right_score

    # Remove fish species in the left partition from unique_species set
    for j in range(i):
        unique_species.discard(s[j])

# Print the maximum ecological score
print(max_score)

----

n = int(input())
s = input()

max_score = 0

for i in range(1, n):
    left_set = set(s[:i])
    right_set = set(s[i:])
    score = len(left_set.intersection(right_set))
    max_score = max(max_score, score)

print(max_score)


---

# 힌트추가하니까 바로맞춤..
#힌트안쓰니까 못맞췄음 .,.

#2월 10일 누적합 서식지 분할
n = int(input())
s = input()

# Store frequency counts of each alphabet
freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1

# Compute maximum ecological score
left_freq = [0] * 26
right_freq = freq.copy()
max_score = 0
for i in range(1, n):
    # Move fish to left section
    c = s[i-1]
    left_freq[ord(c) - ord('a')] += 1
    right_freq[ord(c) - ord('a')] -= 1

    # Compute number of different fish species in each section
    left_count = sum(1 for f in left_freq if f > 0)
    right_count = sum(1 for f in right_freq if f > 0)

    # Update max score
    max_score = max(max_score, left_count + right_count)

print(max_score)