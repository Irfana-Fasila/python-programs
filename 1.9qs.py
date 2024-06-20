def set_union(set1, set2):
    return set1.union(set2)

def set_intersection(set1, set2):
    return set1.intersection(set2)

def set_difference(set1, set2):
    return set1.difference(set2)

def main():
    set1 = set(map(int, input("Enter elements of the first set separated by space: ").split()))
    set2 = set(map(int, input("Enter elements of the second set separated by space: ").split()))

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    
    union_result = set_union(set1, set2)
    print(f"Union of Set 1 and Set 2: {union_result}")
    
    intersection_result = set_intersection(set1, set2)
    print(f"Intersection of Set 1 and Set 2: {intersection_result}")
    
    difference_result1 = set_difference(set1, set2)
    print(f"Difference of Set 1 - Set 2: {difference_result1}")
    
    difference_result2 = set_difference(set2, set1)
    print(f"Difference of Set 2 - Set 1: {difference_result2}")

if __name__ == "__main__":
    main()
