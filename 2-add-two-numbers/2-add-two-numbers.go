import (
    "strings"
    "math/big"
)

type linkedList struct {
    length int
    head *ListNode
    tail *ListNode
}


func (l linkedList) Display() {
	for l.head != nil {
		fmt.Printf("%v -> ", l.head.Val)
		l.head = l.head.Next
	}
	fmt.Println()
}


func strToInt(s string) *big.Int{
    bi := big.NewInt(0)
    
    if _, ok := bi.SetString(s, 10); ok {
        return bi
    } else {
        fmt.Printf("error parsing line %#v\n", s)
    }
    
    return bi
}


func (l *linkedList) PushBack(n *ListNode) {
	if l.head == nil {
		l.head = n
		l.tail = n
		l.length++
	} else {
		l.tail.Next = n
		l.tail = n
		l.length++
	}
}


func sliceToInt(s []int) int {
    res := 0
    op := 1
    for i := len(s) - 1; i >= 0; i-- {
        res += s[i] * op
        op *= 10
    }
    return res
}

func reverseString(str string) string{
   byte_str := []rune(str)
   for i, j := 0, len(byte_str)-1; i < j; i, j = i+1, j-1 {
      byte_str[i], byte_str[j] = byte_str[j], byte_str[i]
   }
   return string(byte_str)
}



// lSumSlice = intToSlice(int64(lSum), lSumSlice)
// ----- lSumSlice = intToSlice(807, empty_slice[])
// ----- n = 807, sequence = empty_slice[]

func intToSlice(n int64, sequence []int64) []int64 {
    if n != 0 {
        i := n % 10
        sequence = append(sequence, i) // reverse order output
        //sequence = append([]int64{i}, sequence...)
        return intToSlice(n/10, sequence)
    }
    return sequence
}


/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    
    ctr := 100
    
    l1List := []int{}
    l1List = append(l1List, l1.Val)
    
    nxt := l1.Next
    
    for i := 0; i <= ctr; i++ {
        if nxt != nil {
            l1List = append(l1List, nxt.Val)
            nxt = nxt.Next // increment nxt
        } else {
            break
        }
	}
    
    l2List := []int{}
    l2List = append(l2List, l2.Val)
    
    nxt = l2.Next
    
    for i := 0; i <= ctr; i++ {
        if nxt != nil {
            l2List = append(l2List, nxt.Val)
            nxt = nxt.Next // increment nxt
        } else {
            break
        }
	}

    // reverse both lists
    revl1List := []int{}
    
    for i := len(l1List) - 1; i >= 0; i-- {
        revl1List = append(revl1List, l1List[i])
    }
    
    revl2List := []int{}
    
    for i := len(l2List) - 1; i >= 0; i-- {
        revl2List = append(revl2List, l2List[i])
    }
    
    // add lists together to create sum
    str_int1 := strings.Trim(strings.Replace(fmt.Sprint(revl1List), " ", "", -1), "[]")
    str_int2 := strings.Trim(strings.Replace(fmt.Sprint(revl2List), " ", "", -1), "[]")
    
    var_int1 := strToInt(str_int1)
    var_int2 := strToInt(str_int2)
    var_int_sum := big.NewInt(0).Add(var_int1, var_int2)
    
    // check is sum is zero and return if so
    if var_int_sum == big.NewInt(0) {
        return &ListNode{Val: 0, Next: nil}
    }
        
    // convert big.Int back to String for later iteration
    var_str_sum := var_int_sum.String()
    
    // reverse string
    var_str_sum_rev := reverseString(var_str_sum)
            
    // build linked lists
    solution := linkedList{}
    
    for index, character := range var_str_sum_rev {
        fmt.Printf("Start Index: %d Value:%s\n", index, string(character))
        sliceNode := &ListNode{Val: int(character - '0')}
        solution.PushBack(sliceNode)
    } 
    
    solution.Display()
    return solution.head
}


