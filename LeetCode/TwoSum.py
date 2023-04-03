def twoSum(nums: list[int], target: int) -> list[int]:
        checked = {}
        i = 0
        while target - nums[i] not in checked:
            checked[nums[i]] = i
            i += 1

        return [checked[target - nums[i]], i]

print(twoSum([2,3,5,7,11,15], 9))