def removeElement(nums: list[int], val: int) -> int:
    tracker = 0
    for item in nums:
        if item != val:
            print(f"item: {item} != val: {val}")
            nums[tracker] = item
            print(f"item[{tracker}]: {nums[tracker]} is now {item}")
            tracker +=1
            print(f"tracker: {tracker-1} is now {tracker}")
            x = input("next step")
        else:
            print(f"item: {item} == val: {val}, skipping it")
    print(nums)
    return tracker

# removeElement([3,2,3,2],3)

def removeElements(nums, val):
    nums.insert(0,None)
    for items in nums[1:]:
        if items != val:
            nums.insert(0,items)
    print(len(nums[0:nums.index(None)])) 
    return len(nums[0:nums.index(None)])


# print(removeElements([3,2,3,2],3))

if __name__ == "__main__":
    pass