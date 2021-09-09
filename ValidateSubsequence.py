from collections import deque

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

sequence = deque(sequence)
for num in array:
    if num in sequence:
        sequence.popleft()

if len(sequence) == 0:
    print(True)
else:
    print(False)

# validation = True
# for num in sequence:
#     if len(sequence) >= len(array):
#         validation = False
#     if not num in array:
#         validation = False
