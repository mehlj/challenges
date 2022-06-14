func revInt(x int) int {
    y := 0
    
    for x > 0 {
        remainder := x % 10
        y = (y * 10) + remainder
        x /= 10
    }
    
    return y
}


func isPalindrome(x int) bool {    
    
    // negative number never will be a palindrome
    if x < 0 {
        return false
    }
    
    if x != revInt(x) {
        return false
    }
    
    return true
}