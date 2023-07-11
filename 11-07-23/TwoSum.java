public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        
        throw new IllegalArgumentException("No two numbers add up to the target sum.");
    }
    
    public static void main(String[] args) {
        TwoSum twoSum = new TwoSum();
        
        int[] nums = {2, 7, 11, 15};
        int target = 13;
        
        int[] result = twoSum.twoSum(nums, target);
        
        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}