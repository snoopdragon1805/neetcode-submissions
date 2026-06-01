class Solution {
    public boolean hasDuplicate(int[] nums) {
        for(int i=0;i<nums.length-1;i++){
            int a = nums[i];
            for(int j = i+1;j<nums.length;j++){
                if(nums[j]==a)
                return true;
            }
            
        }
        return false;
    }
}
