class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Given an array 'height' of length 'n', where each element represents the height of a vertical line
        drawn at index 'i', this function finds two lines that together with the x-axis form a container
        that can store the maximum amount of water. The function returns the maximum water that this
        container can store. The container cannot be slanted.
        """
        
        left, right = 0, len(height) - 1  # Initialize two pointers
        max_water = 0  # Variable to store the maximum water

        while left < right:
            # Calculate the width of the container
            width = right - left
            # Calculate the height of the container (minimum of the two heights)
            container_height = min(height[left], height[right])
            # Update max_water if the current area is greater
            max_water = max(max_water, width * container_height)

            # Move the pointers
            if height[left] < height[right]:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left

        return max_water
