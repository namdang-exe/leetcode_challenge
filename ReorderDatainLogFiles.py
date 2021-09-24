def test_func(x):
    # return log.split()[1:] + [log.split()[0]]
    print(x.split()[1:] + [str(len(x.split()))] + [x.split()[0]])


test_func("a1 9 2 3 1")


def reorderLogFiles(logs):
    al_logs = []
    dig_logs = []
    for log in logs:
        val_c = log.split()[1][0]
        if val_c.isalpha():
            al_logs.append(log)
        else:
            dig_logs.append(log)
    return sorted(al_logs,
                  key=lambda x: x.split()[1:] + [str(len(x.split()))] +
                  [x.split()[0]]) + dig_logs


logs = [
    "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo",
    "a2 act car"
]

print(reorderLogFiles(logs))

logs = ["let1 art zero can", "let3 art zero"]
print(reorderLogFiles(logs))
