def check_sequence(seq:list):
    check_list = []
    for i in range(1, len(seq)):
        if seq[i-1] == seq[i]:
            return 0
        elif seq[i-1] < seq[i]:
            check_list.append(True)
        elif seq[i-1] > seq[i]:
            check_list.append(False)
    if all(check_list):
        return 1
    elif not any(check_list):
        return -1
    else:
        return 0