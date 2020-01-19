

218---------
分開成一個個,並回傳左邊和高,右邊和0

比較時:
若是left的左邊小於right的左邊,則回傳left的左邊和高,但要考慮
高是否可以超過原本的高:max(hl,hr)

同理,right的左邊小於left的左邊時也是一樣

right和left左邊相同時則判斷哪一個高較高

最後的while是判斷還沒加完的left or right的邊
