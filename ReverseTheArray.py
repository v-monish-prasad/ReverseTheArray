def reverseTheArray(array):
    if not array:
        return "Empty Array."

    i = 0
    j = len(array) - 1

    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    return array


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    print(reverseTheArray(array))
