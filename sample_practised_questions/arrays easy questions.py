# # # # # # # to find hte largest element in a array
# # # # # # # brute force aproach

# # # # # # class solution:
# # # # # #     def sort_array(self,arr):
# # # # # #         arr.sort()
# # # # # #         return arr[-1]


# # # # # # obj = solution()
# # # # # # result = obj.sort_array([1,2,9,4,7,6,7,8])
# # # # # # print(result)


# # # # # # # optimal approach



# # # # # # class solution:
# # # # # #     def sort_array(self,arr):
# # # # # #         max_ele = arr[0]
# # # # # #         for i in range(1,len(arr)):
# # # # # #             if arr[i] > max_ele:
# # # # # #                 max_ele = arr[i]
# # # # # #         return max_ele

# # # # # # obj = solution()
# # # # # # result = obj.sort_array([1,2,9,4,7,6,7,8])
# # # # # # print(result)


# # # # # # findng the sencod smallest and secong largest element in an array

# # # # # # class solution:
# # # # # #     def sort_array(self,arr):
# # # # # #         arr.sort()
# # # # # #         second_smallest = arr[1]
# # # # # #         second_largest = arr[-2]
# # # # # #         return second_smallest,second_largest

# # # # # # obj = solution()
# # # # # # result = obj.sort_array([1,2,9,4,7,6,7,8])
# # # # # # print(result)


# # # # # # optimal approach

# # # # # class solution:
# # # # #     def sort_rray(self,arr):
# # # # #         arr.sort()
# # # # #         second_smallest = None
# # # # #         second_largest = None

# # # # #         for i in range(1,len(arr)):
# # # # #             if arr[i] != arr [0]:
# # # # #                 second_smallest = arr[i]
# # # # #                 break

# # # # #         for i in range(len(arr)-2,-1,-1):
# # # # #             if arr[i] != arr[-1]:
# # # # #                 second_largest = arr[i]
# # # # #                 break

# # # # #         return second_smallest,second_largest

# # # # # obj = solution()
# # # # # result = obj.sort_rray([1,2,9,4,7,6,7,8])
# # # # # print(result)


# # # # #chcking weather the given array is worted or not

# # # # # class solution:
# # # # #     def check_sorted(self,arr):
# # # # #         for i in range(0,len(arr)):
# # # # #             if arr[i] <= arr[i+1]:
# # # # #                 return True
# # # # #         return False

# # # # # obj = solution()
# # # # # result = obj.check_sorted([1,2,6,4,5])
# # # # # print(result)


# # # # # finding and reovign the duplicats from an array
# # # # class Solution:

# # # #     def remove_duplicates(self, arr):

# # # #         i = 0

# # # #         for j in range(1, len(arr)):

# # # #             if arr[i] != arr[j]:

# # # #                 i += 1

# # # #                 arr[i] = arr[j]

# # # #         return i + 1


# # # # obj = Solution()

# # # # arr = [1,1,2,2,2,3,3]

# # # # k = obj.remove_duplicates(arr)

# # # # print(arr[:k])
# # # # print("Length =", k)


# # # #knowing if array sorted or not

# # # class solution:
# # #     def sorted_array(self,arr):
# # #         for i in range(1,n):
# # #             if arr[i] < arr[i-1]:
# # #                 return False
# # #         return True
    
# # # obj = solution()
# # # arr = [1,2,8,4,5]
# # # n = len(arr)

# # # result = obj.sorted_array(arr)
# # # print(result)


# # # to remove the duplicates values in an array need to do this 

# # class solution:
# #     def remove_duplicate(self,arr):
# #         i = 0
# #         for j in range(1,len(arr)):
# #             if arr[j] != arr[i]:
# #                 i  += 1
# #                 arr[i] = arr[j]
# #         return i+1
    
# # obj = solution()
# # arr = [1,1,2,2,3,3,4,4,5]
# # k = obj.remove_duplicate(arr)
# # print(arr[:k])


# # rotataing the array
# class solution:
#     def rotate_array(self,arr):
#         temp = arr[0]

#         for i in range (1,len(arr)):
#             arr[i-1] = arr[i]
#         arr[-1] = temp
#         return arr
    
# obj = solution()
# arr = [1,2,6,4,5]
# result = obj.rotate_array(arr)
# print(result)


# checking the array is sorted anda rotated or not
# class solution:
#     def check_sorted_rorated(self,arr):
#         n = len(arr)
#         count = 0
#         for i in range(n):
#             if arr[i] > arr[(i+1)%n]:
#                 count += 1
#             if count > 1:
#                 return False
#         return True
    
# obj = solution()
# arr = [3,4,5,1,2]
# result = obj.check_sorted_rorated(arr)
# print(result)


# removing the duplicates for an array
class Solution(object):

    def removeDuplicates(self, nums):

        temp = []

        for num in nums:

            if num not in temp:

                temp.append(num)

        return len(temp), temp


obj = Solution()

print(obj.removeDuplicates([1,1,2,2,3,3,4]))