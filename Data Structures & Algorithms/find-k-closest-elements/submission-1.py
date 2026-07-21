class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # we can calucalte the total distance by having a window of size k
        # calculate the distance btwn each value in k
        #   check if its the minimum size (or strictly less than the prev min val)
        #   if so, update 2 pointers that have an end and start for hte answer


        # create the window

        # find the distance of values in the window

        # check if its minimum 
        #   if yes update global pts if it is
        #   no then keep iterating to the next values doing the whole thing over again

        # after loop
        # create the res array by iterating from global_start to global_end and add into array
        # return the res


        global_start, global_end = 0, k-1

        # case when the k is equal to the size of the array --> return the whole array
        if k-1 == len(arr):
            return arr
        
        min_distance = 0
        for i in range(k):
            min_distance += abs(x - arr[i])
        print(min_distance)

        l = 0
        distance = min_distance
        for r in range(k, len(arr)):
            # update the min distances
            distance = min_distance + abs(x-arr[r]) - abs(x-arr[l])
            l += 1  
            # check if lower than prev min_distanace   
            if distance < min_distance:
                min_distance = distance
                global_start, global_end = l, r

        res = []
        print(global_start, " ", global_end)
        for i in range(global_start, global_end+1):
            res.append(arr[i])
        
        return res
