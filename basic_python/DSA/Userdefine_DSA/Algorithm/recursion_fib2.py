

def fibonnacci(n):
    sequence = [0, 1]
    if n == 1:
        sequence = [0]
    else:
        for i in range(n):
            if len(sequence) > 2:
                sequence.append(sequence[i] + sequence[i+1])
            else:
                sequence.append(sequence[i] + sequence[i+1])
    return sequence


if __name__ == "__main__":
    fibonnacci(4)
