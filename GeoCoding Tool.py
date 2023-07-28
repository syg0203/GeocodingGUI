import sys, UI
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

import os
import requests
import pandas as pd

class MainDialog(QDialog, UI.Ui_dialog):
	def __init__(self):
		QDialog.__init__(self, None)

		self.setupUi(self)

		self.start_pushButton.clicked.connect(self.startclicked)
		self.cancel_pushButton.clicked.connect(app.quit)
		self.findcsv_pushButton.clicked.connect(self.open_sheet)
		self.tocsv_pushButton.clicked.connect(self.to_sheet)

	def startclicked(self):
		readpath=self.csv_textBrowser.toPlainText()
		topath=self.tocsv_textBrowser.toPlainText()
		if (readpath =='csv 파일 불러오기') or (readpath==''):
			msgBox = QMessageBox()
			msgBox.setWindowTitle("GeoCoding") # 메세지창의 상단 제목
			msgBox.setIcon(QMessageBox.Critical) # 메세지창 내부에 표시될 아이콘
			msgBox.setText("불러올 파일을 선택하세요") # 메세지 제목
			msgBox.setStandardButtons(QMessageBox.Ok) # 메세지창의 버튼
			msgBox.setDefaultButton(QMessageBox.Ok) # 포커스가 지정된 기본 버튼
			msgBox.exec_() # 클릭한 버튼 결과 리턴
		elif (topath =='csv 파일 내보내기') or (topath==''):
			msgBox = QMessageBox()
			msgBox.setWindowTitle("GeoCoding") # 메세지창의 상단 제목
			msgBox.setIcon(QMessageBox.Critical) # 메세지창 내부에 표시될 아이콘
			msgBox.setText("내보낼 파일을 지정하세요") # 메세지 제목
			msgBox.setStandardButtons(QMessageBox.Ok) # 메세지창의 버튼
			msgBox.setDefaultButton(QMessageBox.Ok) # 포커스가 지정된 기본 버튼
			msgBox.exec_() # 클릭한 버튼 결과 리턴
		else:
			address_list=[]
			X_list = []
			Y_list = []
			region_1depth = []
			region_2depth = []
			region_3depth = []
			cnt=1
			for i in address_target[self.comboBox.currentText()]:		
				url = "https://dapi.kakao.com/v2/local/search/address.json"
				headers =  {'Authorization': 'KakaoAK keyvalue'}
				data = {'query': i}
				req = requests.get(url, headers=headers, data=data)

				req.get_method = lambda: "GET"
				response_body = req.json()

				req.close

				text = response_body['documents']

				try:
					XY = dict(text[0])
				except IndexError:
					url = "https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=1&sort=accuracy"
					headers =  {'Authorization': 'KakaoAK keyvalue'}
					data = {'query': i}
					req = requests.get(url, headers=headers, data=data)
					#time.sleep(3)
					req.get_method = lambda: "GET"
					response_body = req.json()
					#print(data)
					req.close

					text = response_body['documents']
					try:
						XY = dict(text[0])
					except IndexError:
						X_list.append('0')
						Y_list.append('0')
						region_1depth.append('0')
						region_2depth.append('0')
						region_3depth.append('0')
						address_list.append(i)

					else:
						X_list.append(XY['x'])
						Y_list.append(XY['y'])
						region_1depth.append(XY['address_name'].split(' ')[0])
						region_2depth.append(XY['address_name'].split(' ')[1])
						region_3depth.append(XY['address_name'].split(' ')[2])

						address_list.append(i)
				else:
					if XY['road_address'] == None:
						X_list.append(XY['x'])
						Y_list.append(XY['y'])
						region_1depth.append(XY['address']['region_1depth_name'])
						region_2depth.append(XY['address']['region_2depth_name'])
						region_3depth.append(XY['address']['region_3depth_name'])
						address_list.append(i)

					elif XY['address'] == None:
						X_list.append(XY['x'])
						Y_list.append(XY['y'])
						region_1depth.append(XY['road_address']['region_1depth_name'])
						region_2depth.append(XY['road_address']['region_2depth_name'])
						region_3depth.append(XY['road_address']['region_3depth_name'])
						address_list.append(i)
					else:
						X_list.append(XY['x'])
						Y_list.append(XY['y'])
						region_1depth.append(XY['address']['region_1depth_name'])
						region_2depth.append(XY['address']['region_2depth_name'])
						region_3depth.append(XY['address']['region_3depth_name'])
						address_list.append(i)


				cnt=cnt+1
				realcnt=cnt*100/len(address_target)
				self.progress.setValue(realcnt)
			address_target['입력주소'] = address_list
			address_target['X좌표'] = X_list
			address_target['Y좌표'] = Y_list
			address_target['입력주소_시'] = region_1depth
			address_target['입력주소_군'] = region_2depth
			address_target['입력주소_구'] = region_3depth

			address_target.to_csv(topath, encoding = 'euc-kr',index=False)

			msgBox = QMessageBox()
			msgBox.setWindowTitle("GeoCoding") # 메세지창의 상단 제목
			msgBox.setIcon(QMessageBox.Information) # 메세지창 내부에 표시될 아이콘
			msgBox.setText("변환 완료") # 메세지 제목
			msgBox.setStandardButtons(QMessageBox.Ok) # 메세지창의 버튼
			msgBox.setDefaultButton(QMessageBox.Ok) # 포커스가 지정된 기본 버튼
			msgBox.exec_() # 클릭한 버튼 결과 리턴

	def open_sheet(self):
		try:
			self.check_change = False
			path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
			self.csv_textBrowser.setText(path[0])
			path1=self.csv_textBrowser.toPlainText()
			global address_target
			address_target = pd.read_csv(path1,engine='python')
			adcol=address_target.columns
			for i in range(len(adcol)):
				self.comboBox.addItem(adcol[i])
		except:
			pass

	def to_sheet(self):
		try:
			self.check_change = False
			path = QFileDialog.getSaveFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
			self.tocsv_textBrowser.setText(path[0])
		except:
			pass

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()
