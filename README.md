7-----------
先將數字的絕對值以string的方式倒過來([::-1]),再進行判斷是否要加負號以及是
否有超過題目範圍


56----------
num的判斷：目前的值和目前的值加上前面累積的值挑大的,若是加上累積的值較大
則會不段累積下去,反之則從從目前的值重新開使給下一次累積判斷
ans的判斷：num是不斷的累積下去,ans是截至目前的最大值,兩個互相比較看誰較大

61----------
用array紀錄最後要加入的value順序,再依序放入ListNode的val

62----------
用高中排列組合解

63----------
先開一個和input一樣大的matrix,裡面都放0, 並設立兩個bool以便之後在判斷第一列
或第一行是否被堵住用,接下來就是把matrix填滿,ＤＰ的部分是每一個位置都是上面的
路線和左邊的路線相加,由此將整個matirx建完畢

64----------
每一個點考慮左邊和右邊加上自己值的最小狀況(min(tmp_up,tmp_left)),first_row只需要考慮左邊的值;
first_column只需要考慮上面的值;start([0][0])的位置則不管,以此建出整個matrix

70----------
用bottom up的方式先建立0,1,2的值,接下來的值用optimal substructure的方式建
上去,答案是和1和2的組合相加
例如3是(1+'2')和(2+'1'),而2的最佳解(組合數)為2,1的最佳解(組合數)
為1,故答案為1+2=3
再例4是(1+'3')和(2+'2'),3的最佳解為3,2的最佳解為2,故4的最佳解為3+2=5

96----------
BST分成左右兩邊,可以想像成root左邊“有幾個”和右邊"有幾個",由於左邊數量
的排列可以由之前的optimal substructure 找到,同理,右邊的也是,所以兩邊數
量相乘便是總組合數,直得注意的是optimal substructrue在0的時候要設為1
ex:
n=3時,當root為3,左邊數是2,右邊是0, 故為2(n==2時的組合數)＊1(0設為1)=2;root 為2\n
時,左邊有1,右邊也是1,故為1＊1=1; root 為1時,左邊為0,右邊為2,故為1＊2=2,
最後total為2+1+2=5

118---------
recursive到numRows==1,回彈時將next list裡的上一個list的值做運算後加到新的
list,再回傳

119---------
方法和118一樣,只是改成回傳一行而不是整個list

218---------
分開成一個個,並回傳左邊和高,右邊和0

比較時:
若是left的左邊小於right的左邊,則回傳left的左邊和高,但要考慮
高是否可以超過原本的高:max(hl,hr)

同理,right的左邊小於left的左邊時也是一樣

right和left左邊相同時則判斷哪一個高較高

最後的while是判斷還沒加完的left or right的邊

334---------
第一個跟最後一個換,第二跟倒數第二換,如此重複至中間

554---------
從第一條line開始將每一個空隙的位置用dict紀錄,依序記錄到最後一條
最後找最多空隙的值(最多條line有這個空隙),最後答案是line的數量-最多空隙的值,
要注意的是因為最後一個空隙(line的長)一定是全部的line數,所以那一個空隙不能算,
多加一個0：0的空隙以便若是全部的line都只有一個值的狀況

# 2021/07/23
## 4. Median of Two Sorted Arrays (v)
> https://leetcode.com/problems/median-of-two-sorted-arrays/

## 11. Container With Most Water
> https://leetcode.com/problems/container-with-most-water/

## 15. 3Sum (v)
> https://leetcode.com/problems/3sum/


# 2021/07/25
## 17. Letter Combinations of a Phone Number
> https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## 19. Remove Nth Node From End of List
> https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## 121. Best Time to Buy and Sell Stock
> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 2021/07/26
## 1161. Maximum Level Sum of a Binary Tree
> https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

## 973. K Closest Points to Origin
> https://leetcode.com/problems/k-closest-points-to-origin/

## 904. Fruit Into Baskets (v)
> https://leetcode.com/problems/fruit-into-baskets/

# 2021/07/27
## 226. Invert Binary Tree
> https://leetcode.com/problems/invert-binary-tree/

## 482. License Key Formatting
> https://leetcode.com/problems/license-key-formatting/

## 1304. Find N Unique Integers Sum up to Zero
> https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

# 2021/08/04

## 98. Validate Binary Search Tree
> https://leetcode.com/problems/validate-binary-search-tree/

## 45. Jump Game II
> https://leetcode.com/problems/jump-game-ii/

# 2021/08/12

## 48. Rotate Image
> https://leetcode.com/problems/rotate-image/

## 34. Find First and Last Position of Element in Sorted Array
> https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## 300. Longest Increasing Subsequence
> https://leetcode.com/problems/longest-increasing-subsequence/

## 334. Increasing Triplet Subsequence
> https://leetcode.com/problems/increasing-triplet-subsequence/

# 2021/08/19
## 207. Course Schedule (V)
> https://leetcode.com/problems/course-schedule/

## 46. Permutations
> https://leetcode.com/problems/permutations/

## 108. Convert Sorted Array to Binary Search Tree
> https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

## 88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

## 617. Merge Two Binary Trees
> https://leetcode.com/problems/merge-two-binary-trees/

# 2021/08/20
## 283. Move Zeroes
> https://leetcode.com/problems/move-zeroes/

## 338. Counting Bits
> https://leetcode.com/problems/counting-bits/

## 234. Palindrome Linked List
> https://leetcode.com/problems/palindrome-linked-list/

## 169. Majority Element
> https://leetcode.com/problems/majority-element/

# 2021/08/22
## 206. Reverse Linked List
> https://leetcode.com/problems/reverse-linked-list/

## 104. Maximum Depth of Binary Tree
> https://leetcode.com/problems/maximum-depth-of-binary-tree/
