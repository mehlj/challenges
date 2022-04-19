func twoSum(nums []int, target int) []int {
    
    anchor := 0
    solution := []int{}
    
    for anchor < len(nums) {
        for i := 0; i < len(nums); i++ {
            if anchor != i {
                if nums[anchor] + nums[i] == target {
                    return []int{anchor,i}
                }
            } 
        }
        anchor = anchor + 1
    }
    
    return solution
}
