print("=====お買い物リストツールです=====")

items = []

while True:
 print("1.リストに追加、2.リストから削除（「終了」と入力すると終了します）")
 exe_number = input("実行したい数字を選んでください \n")
 if exe_number == "終了" :
   break
 if exe_number == "1" :
  while True :
   item = input("購入する物を入力してください(endを入力すると終了します) \n")
 
   if item == "end" :
    break

   items.append(item)

   print("=====完成した買い物リスト=====")
   count = 1
   for item in items :
     print(count,"番目",item)
     count += 1
 
  print("=====お買い物行ってらっしゃい=====")

 elif exe_number == "2" :
  while True :
   item = input("削除する物を入力してください(endを入力すると終了します) \n")
   if item == "end" :
    break
   if item in items :
    items.remove(item)
   
   print("=====完成した買い物リスト=====")
   count =  1
   for i in items :
     print(count,"番目",i)
     count += 1
