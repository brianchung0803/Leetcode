
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


218---------
分開成一個個,並回傳左邊和高,右邊和0

比較時:
若是left的左邊小於right的左邊,則回傳left的左邊和高,但要考慮
高是否可以超過原本的高:max(hl,hr)

同理,right的左邊小於left的左邊時也是一樣

right和left左邊相同時則判斷哪一個高較高

最後的while是判斷還沒加完的left or right的邊

554---------
從第一條line開始將每一個空隙的位置用dict紀錄,依序記錄到最後一條
最後找最多空隙的值(最多條line有這個空隙),最後答案是line的數量-最多空隙的值,
要注意的是因為最後一個空隙(line的長)一定是全部的line數,所以那一個空隙不能算,
多加一個0：0的空隙以便若是全部的line都只有一個值的狀況
