
head = ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
print(head.val) # not access directly due to it return end node val


while head:
    print(head.next)
    print(head.val)
    head = head.next
# ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
# 1
# ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
# 2
# ListNode{val: 4, next: ListNode{val: 5, next: None}}
# 3
# ListNode{val: 5, next: None}
# 4
# None
# 5


# arr to linklist
# arr = [1,2,3]
# dummy = ListNode()
# curr = dummy
# for val in arr:
#     curr.next = ListNode(val)
#     curr = curr.next
# return dummy.next
