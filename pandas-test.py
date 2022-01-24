import pandas as pd

df_1 = pd.read_csv('car_event_history_details_noComponent.csv')
df_2 = pd.read_csv('car_event_history_details_noComponentAfter.csv')

# print(df_1)
# print(df_2)
# 完全一致
# print(df_1 == df_2)

# 差分のあった df2 のレコードのみ表示
print(df_2[(df_1 == df_2).all(axis=1) == False])
#        key  val
# 3  string4   -1

print()

# 差分のあったフィールドのみ表示
print(df_1.compare(df_2))
#    val
#   self other
# 3  4.0  -1.0
