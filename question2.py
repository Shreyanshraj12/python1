def distributeCandies(candyType):
    max_types = len(candyType) // 2
    unique_types = set()

    for candy in candyType:
        unique_types.add(candy)
        if len(unique_types) >= max_types:
            break

    return len(unique_types)


candyType = [1, 1, 2, 2, 3, 3]
print(distributeCandies(candyType))  
