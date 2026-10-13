import random
import math

def calc_distance(x1,y1,x2,y2):
 diff_x = x1 - x2
 diff_y = y1 - y2

 return math.sqrt(diff_x**2 + diff_y**2)

#スイカの位置を決める
suika_x = random.randrange(0, 5) #スイカのx座標
suika_y = random.randrange(0, 5) #スイカのy座標

#プレイヤーの位置を決める
player_x = random.randrange(0, 5) #プレイヤーのx座標
player_y = random.randrange(0, 5) #プレイヤーのy座標

while (suika_x != player_x) or (suika_y != player_y):
  #プレイヤーとスイカの距離を表示
  distance = calc_distance(player_x,player_y,suika_x,suika_y)
  print("プレイヤーとスイカの距離は:",distance)

 #プレイヤーを操作
  c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動") 
  if c == "n":
   player_y = player_y - 1
  elif c == "s":
   player_y = player_y + 1
  elif c == "w":
   player_x = player_x -1
  elif c == "e":
   player_x = player_x + 1

print("プレイヤーとスイカの距離:",distance)
print("距離が一致しました。")