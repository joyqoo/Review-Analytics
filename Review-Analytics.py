datas = []
count =0
with open ('reviews.txt', 'r') as f:
	for line in f:
		datas.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(datas))
print('檔案讀取完畢 共有' ,len(datas),"筆資料")

sum_len = 0
new = [data for data in datas if len(data) < 100]
good = [data for data in datas if 'good' in data]
bad = [data for data in datas if 'bad' in data]
for data in datas:
	sum_len = sum_len + len(data)
print('有' ,len(new),"筆留言的長度小於100")
print('有' ,len(good),"筆留言是正向回覆")
print('有' ,len(bad),"筆留言是負向回覆 ")
print('留言的平均長度為' ,sum_len/len(datas))

