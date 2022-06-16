import (
    "strings"
)


func reverseSwapRunes(s string) string {
    chars := []rune(s)
    for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
        chars[i], chars[j] = chars[j], chars[i]
    }
    return string(chars)
}


/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    
    var llSlice []int
    llSlice = append(llSlice, head.Val)
    
    nxt := head.Next
    
    // build []int from linked list
    for {
        if nxt != nil {
            llSlice = append(llSlice, nxt.Val)
            nxt = nxt.Next // increment nxt
        } else {
            break
        }
	}
    
    // convert []int to String
    llString := strings.Trim(strings.Replace(fmt.Sprint(llSlice), " ", "", -1), "[]")
    
    //fmt.Printf("Comparing %v and %v\n", llString, revStr(llString))
        
    // check if value is the same after reversing (palindrome test)
    if llString == reverseSwapRunes(llString) {
        return true
    }
        
    return false
}