#!/usr/bin/env python
#回溯法求N皇后

#1.定义3个正整数，分别表示纵行row，左斜行l和右斜行r被占据的情况。
#2.通过位运算判断目前所有可放置的位置，如果还有可放置的位置，就向选择放置。
#3.向下一层尝试，将已选择的位置通过位运算

NQ=8#皇后数以及棋盘的宽度，尽量设置在10以内
s=""

def showNQ(data):
	#拼接解法字符串,用于保存解法集
	global s
	for i in data:
		for j in range(0,NQ):
			if (i>>j)&1==1:
				s=s+"X"
			else:
				s=s+"O"
		s=s+"\n"
	s=s+"\n"

tot = 0
goal=(1<<NQ)-1

def dfs(a,l,r,row):
	#回溯法求解
	if row != goal:
		safe = goal & (~(row|l|r))#可放置的位置
		while(safe > 0):
			nt = safe & (~safe + 1)#利用位运算求出右边第一个可放置位置
			safe = safe^nt#改变可放置位置
			a.append(nt)
			dfs(a,(l|nt)<<1,(r|nt)>>1,row|nt)
			a.pop()
	else:
		global tot
		tot+=1
		showNQ(a)

if __name__ == '__main__':
	dfs([],0,0,0)
	f = open("8Queen.txt", 'w')
	f.write(s)
	f.close()
	print("共"+str(tot)+"种解法,所有解法保存在8Queen.txt中")
