def unlock_pass(pw):
    def combined(digits):
        out = ""
        for d in digits:
            out += str(d)
        return out

    reminder = []
    while pw != 0:
        reminder.append(pw % 10)
        pw //= 10
    return combined(sorted(reminder))


pw = 35961
print(unlock_pass(pw))
