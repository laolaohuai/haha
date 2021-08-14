#! /usr/bin/python
# coding=utf-8
# -*- coding:utf8 -*-

import re
#re模块的七大方法
#match(string[, pos[, endpos]]) | re.match(pattern, string[, flags])
#search(string[, pos[, endpos]]) | re.search(pattern, string[, flags])
#split(string[, maxsplit]) | re.split(pattern, string[, maxsplit])
#findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags])
#finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags])
#sub(repl, string[, count]) | re.sub(pattern, repl, string[, count])
#subn(repl, string[, count]) |re.sub(pattern, repl, string[, count])



#re.match函数
#re.match(pattern, string, flags=0)
#匹配成功re.match方法返回一个匹配的对象，否则返回None。
#我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
#group(num=0)匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
#groups()返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
def test1():
	print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
	print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

def test2():
	line = "Cats are smarter than dogs"
	matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
	if matchObj:
		print "matchObj.group() : ", matchObj.group()
		print "matchObj.group(1) : ", matchObj.group(1)
		print "matchObj.group(2) : ", matchObj.group(2)
	else:
		print "No match!!"

#re.search方法
#re.search(pattern, string, flags=0)
#pattern匹配的正则表达式
#string要匹配的字符串。
#flags标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
#group(num=0)匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
#groups()返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
def test3():
	print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
	print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

def test4():
	line = "Cats are smarter than dogs";
	searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
	if searchObj:
		print "searchObj.group() : ", searchObj.group()
		print "searchObj.group(1) : ", searchObj.group(1)
		print "searchObj.group(2) : ", searchObj.group(2)
	else:
		print "Nothing found!!"

#re.match与re.search的区别
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
#而re.search匹配整个字符串，直到找到一个匹配。
def test5():
	line = "Cats are smarter than dogs";
	matchObj = re.match( r'dogs', line, re.M|re.I)
	if matchObj:
		print "match --> matchObj.group() : ", matchObj.group()
	else:
		print "No match!!"
	matchObj = re.search( r'dogs', line, re.M|re.I)
	if matchObj:
		print "search --> matchObj.group() : ", matchObj.group()
	else:
		print "No match!!"

#检索和替换
#re.sub(pattern, repl, string, count=0, flags=0)
#pattern : 正则中的模式字符串。
#repl : 替换的字符串，也可为一个函数。
#string : 要被查找替换的原始字符串。
#count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
def test6():
	phone = "2004-959-559 # 这是一个国外电话号码"
	# 删除字符串中的 Python注释 
	num = re.sub(r'#.*$', "", phone)
	print "电话号码是: ", num
	# 删除非数字(-)的字符串 
	num = re.sub(r'\D', "", phone)
	print "电话号码是 : ", num


#repl 参数是一个函数
# 将匹配的数字乘以 2
def test7():
	def double(matched):
	    value = int(matched.group('value'))
	    return str(value * 2)
	s = 'A23G4HFD567'
	print(re.sub('(?P<value>\d+)', double, s))



#re.compile 函数
#re.compile(pattern[, flags])
#pattern : 一个字符串形式的正则表达式
#flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：

	#re.I 忽略大小写
	#re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
	#re.M 多行模式
	#re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
	#re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
	#re.X 为了增加可读性，忽略空格和 # 后面的注释

def test8():
	pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
	m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
	print m

	m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
	print m

	m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
	print m                                         # 返回一个 Match 对象
	#在上面，当匹配成功时返回一个 Match 对象，其中：
	#group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
	#start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
	#end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
	#span([group]) 方法返回 (start(group), end(group))。
	print m.group(0)   # 可省略 0
	print m.start(0)   # 可省略 0
	print m.end(0)     # 可省略 0
	print m.span(0)    # 可省略 0



#findall
#findall(string[, pos[, endpos]])
#string : 待匹配的字符串。
#pos : 可选参数，指定字符串的起始位置，默认为 0。
#endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。

#查找字符串中的所有数字：
def test9():
	pattern = re.compile(r'\d+')   # 查找数字
	result1 = pattern.findall('runoob 123 google 456')
	result2 = pattern.findall('run88oob123google456', 0, 10)
	print(result1)
	print(result2)

#re.finditer
#和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
#re.finditer(pattern, string, flags=0)
def test10():
	it = re.finditer(r"\d+","12a32bc43jf3") 
	for match in it: 
	    print (match.group())


#分组匹配
#身份证 1102231990xxxxxxxx
def test11():
	s = '1102231990xxxxxxxx'
	res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
	print(res.groupdict())

def test12():
	# 匹配如下内容：单词+空格+单词+任意字符
	m = re.match(r'(\w+) (\w+)(.*)', 'hello world!')
	print "m.string:", m.string
	print "m.re:", m.re
	print "m.pos:", m.pos
	print "m.endpos:", m.endpos
	print "m.lastindex:", m.lastindex
	print "m.lastgroup:", m.lastgroup
	print "m.group():", m.group()
	print "m.group(1,2):", m.group(1, 2)
	print "m.groups():", m.groups()
	print "m.groupdict():", m.groupdict()
	print "m.start(2):", m.start(2)
	print "m.end(2):", m.end(2)
	print "m.span(2):", m.span(2)
	print "m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')

#re.split(pattern, string[, maxsplit])
def test13():
	pattern = re.compile(r'\d+')
	print re.split(pattern,'one1two2three3four4')



#匹配次数
#^	匹配字符串的开头
#$	匹配字符串的末尾。
#.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
#[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
#[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
#re*	匹配0个或多个的表达式。
#re+	匹配1个或多个的表达式。
#re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
#re{ n}	精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
#re{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
#re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
#a| b	匹配a或b
#(re)	匹配括号内的表达式，也表示一个组
#(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
#(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
#(?: re)	类似 (...), 但是不表示一个组
#(?imx: re)	在括号中使用i, m, 或 x 可选标志
#(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
#(?#...)	注释.
#(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
#(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
#(?> re)	匹配的独立模式，省去回溯。
#\w	匹配字母数字及下划线
#\W	匹配非字母数字及下划线
#\s	匹配任意空白字符，等价于 [\t\n\r\f].
#\S	匹配任意非空字符
#\d	匹配任意数字，等价于 [0-9].
#\D	匹配任意非数字
#\A	匹配字符串开始
#\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
#\z	匹配字符串结束
#\G	匹配最后匹配完成的位置。
#\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
#\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
#\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
#\1...\9	匹配第n个分组的内容。
#\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。

#匹配符（规则）
#[Pp]ython	匹配 "Python" 或 "python"
#rub[ye]	匹配 "ruby" 或 "rube"
#[aeiou]	匹配中括号内的任意一个字母
#[0-9]	匹配任何数字。类似于 [0123456789]
#[a-z]	匹配任何小写字母
#[A-Z]	匹配任何大写字母
#[a-zA-Z0-9]	匹配任何字母及数字
#[^aeiou]	除了aeiou字母以外的所有字符
#[^0-9]	匹配除了数字外的字符
#.	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
#\d	匹配一个数字字符。等价于 [0-9]。
#\D	匹配一个非数字字符。等价于 [^0-9]。
#\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
#\S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
#\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
#\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。

test12()