def show_items(items) :
  #現在の買い物リストを表示させます
  if not items :
    print("現在買い物リストは空です")
    return
  
  print("=====現在の買い物リスト=====")
  for index, item in  enumerate(items, start = 1) :
      print(f"{index}.{item}")

def add_item(items) :
  #買い物リストに新しい商品を追加する
  while True :
   ad_item = input("=====追加したい商品を入力してください(「終了」を入力すると終了します) \n")
   if ad_item == "終了" :
     break
   if ad_item.strip() == "" :
     print("空白は入力できません")
     continue
   items.append(ad_item)
   print(f"{ad_item}を追加しました")
   show_items(items)
  return items

def remove_item(items) :
  #買い物リストから指定されて商品を削除します
  while True : 
   if not items :
    print("削除する商品がありません")
    break
   
   show_items(items)
   re_item = input("=====削除したい商品または番号を入力してください(「終了」を入力すると終了します) \n")
   if re_item == "終了" :
     break
   
   if re_item.isdigit() :
     number = int(re_item)
     if 1 <= number <= len(items) :
       del_item = items.pop(number - 1)
       print(f"{del_item}を削除しました")
     else :
       print(f"{len(items)}の範囲内の番号を入力してください")
    
   else :
    if re_item in items :
     items.remove(re_item)
     print(f"{re_item}を削除しました")
    else :
     print(f"{re_item}はリストから見つかりません")   
  
   return items

def main() :
 print("=====買い物リストアプリです=====")

 shopping_list = []

 while True :
   print("\n----------------------------------")
   print("1: リストの表示")
   print("2: 商品の追加")
   print("3: 商品の削除")
   print("4: 終了")

   choice = input("メニュー番号を入力してください\n")

   if choice == "1" :
     show_items(shopping_list)
   elif choice == "2" :
     shopping_list = add_item(shopping_list)
   elif choice == "3" :
     shopping_list = remove_item(shopping_list)
   elif choice == "4" :
     print("=====アプリを終了します。行ってらっしゃい")
     break
   else :
     print("※1~4の数字から選んでください")  

#このファイルが直接実行された時だけ main() を呼び出すお決まりの書き方（スクリプトのエントリポイント）です。将来、別ファイル
#からこの関数群を import して再利用する際に誤動作するのを防ぎます。
if __name__ == "__main__" :
  main()
















