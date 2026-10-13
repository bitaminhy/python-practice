print("-------計測ツール-------")

total_price = int(input("合計金額を入力してください \n"))
number_people = int(input("人数を入力してください \n"))

per_price = (total_price // number_people)
remainder = (total_price % number_people)

print("一人あたりの金額：",per_price,"円")
print("端数の金額：",remainder,"円")




