// Given an array of non-negative integers representing an elevation map,
// compute how much water it can trap after raining.

// Define a method called trapWater that takes an array of non-negative integers
// (heights) as input and returns an integer representing the total amount of
// water trapped.
// Inside the trapWater method, initialize two variables: totalWater to keep
// track of the accumulated water and leftMax and rightMax to store the maximum
// heights on the left and right sides, respectively. Initialize them to 0.
// Define two pointers, left and right, pointing to the start and end of the
// heights array.
// While left is less than or equal to right, do the following:
// Check if heights[left] is less than or equal to heights[right]:
// If true, compare heights[left] with leftMax:
// If heights[left] is greater than leftMax, update leftMax to heights[left].
// If heights[left] is less than or equal to leftMax, calculate the water
// trapped at the current position (left) as leftMax - heights[left] and add it
// to totalWater.
// Increment left by 1.
// If false, do the same steps as above, but with heights[right] instead of
// heights[left].
// Finally, return the totalWater calculated.