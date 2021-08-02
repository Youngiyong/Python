def solution(nums1, n1, nums2, n2):

    del nums1[n1:]
    del nums2[n2:]
    nums1 += nums2
    nums1.sort()
    return nums1

print(solution([1,2,3,0,0,0],3, [2,5,6], 3))