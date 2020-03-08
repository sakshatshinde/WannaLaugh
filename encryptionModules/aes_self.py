# NOTE
# This has not been used in this project. We tried to implement AES ourselves. But using a premade solution
# seemed fit for the task due to time limitations

import random
class Aes:
# key 
# data 


# constructor
	def __init__(self, fnm):
		self._fnm = fnm
		self.__sbox =    ["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76","ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0","b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15","04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75","09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84","53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf","d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8","51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2","cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73","60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db","e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79","e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08","ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a","70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e","e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df","8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]
		self.__sboxInv = ["52", "09", "6a", "d5", "30", "36", "a5", "38", "bf", "40", "a3", "9e", "81", "f3", "d7", "fb","7c", "e3", "39", "82", "9b", "2f", "ff", "87", "34", "8e", "43", "44", "c4", "de", "e9", "cb","54", "7b", "94", "32", "a6", "c2", "23", "3d", "ee", "4c", "95", "0b", "42", "fa", "c3", "4e","08", "2e", "a1", "66", "28", "d9", "24", "b2", "76", "5b", "a2", "49", "6d", "8b", "d1", "25","72", "f8", "f6", "64", "86", "68", "98", "16", "d4", "a4", "5c", "cc", "5d", "65", "b6", "92","6c", "70", "48", "50", "fd", "ed", "b9", "da", "5e", "15", "46", "57", "a7", "8d", "9d", "84","90", "d8", "ab", "00", "8c", "bc", "d3", "0a", "f7", "e4", "58", "05", "b8", "b3", "45", "06","d0", "2c", "1e", "8f", "ca", "3f", "0f", "02", "c1", "af", "bd", "03", "01", "13", "8a", "6b","3a", "91", "11", "41", "4f", "67", "dc", "ea", "97", "f2", "cf", "ce", "f0", "b4", "e6", "73","96", "ac", "74", "22", "e7", "ad", "35", "85", "e2", "f9", "37", "e8", "1c", "75", "df", "6e","47", "f1", "1a", "71", "1d", "29", "c5", "89", "6f", "b7", "62", "0e", "aa", "18", "be", "1b","fc", "56", "3e", "4b", "c6", "d2", "79", "20", "9a", "db", "c0", "fe", "78", "cd", "5a", "f4","1f", "dd", "a8", "33", "88", "07", "c7", "31", "b1", "12", "10", "59", "27", "80", "ec", "5f","60", "51", "7f", "a9", "19", "b5", "4a", "0d", "2d", "e5", "7a", "9f", "93", "c9", "9c", "ef","a0", "e0", "3b", "4d", "ae", "2a", "f5", "b0", "c8", "eb", "bb", "3c", "83", "53", "99", "61","17", "2b", "04", "7e", "ba", "77", "d6", "26", "e1", "69", "14", "63", "55", "21", "0c", "7d"]


	def __fileLength(self,file):
		with open(file, "rb") as f:
			f.seek(0,2)
			flen = f.tell()
		return flen

# read data
	def getFile(self):
		self._fileLen = self.__fileLength(self._fnm)
		#read hex 
		with open(self._fnm, "rb") as file_rb:
			temp = file_rb.read(1).hex()
			self.file_lines = []
			# get data as fast as possible 
			for i in range(self._fileLen//32):
				temp1 = []
				for j in range(8):
					temp2=[]
					for k in range(4):
						temp2.append(temp)
						temp = file_rb.read(1).hex()
					temp1.append(temp2)
				self.file_lines.append(temp1)
			# print(self.file_lines)

			# calc required offset and store it into protected var
			self._offset = 32-self._fileLen%32
			snglOfset = 0
			temp1=[]
			tempPointer=self._fileLen
			# get remaining data + offset
			i=0
			while temp:
				temp2=[]
				j=0
				while temp:
					# if condn is for offset
					if tempPointer==file_rb.tell() and snglOfset < self._offset:
						tempPointer=file_rb.seek(snglOfset,0)
						snglOfset+=1

					temp2.append(temp)
					temp = file_rb.read(1).hex()
					j+=1
					# store 4 elements
					if j==4:
						break

				# store 8 elements
				temp1.append(temp2)
				i+=1
				if i==8:
					break

			self.file_lines.append(temp1)

		# real length
		self._fileLen = self._fileLen+self._offset
		print(self.file_lines)
	def sbox(self, fileLines):
		for i in range(8):
			for j in range(4):
				# print(fileLines[i][j])
				index = self.__sbox.index(fileLines[i][j])

				fileLines[i][j] = self.__sboxInv[index]
		# print(fileLines)

		return fileLines

	def shiftRows(self, fileLines):
		temp = []
		for i in range(8):
			temp1 = []
			for j in range(4):
				temp1.append(fileLines[i][(j+i)%4])
			temp.append(temp1)
		# print(temp)
		return temp

	def mixCols(self, fileLines):
		temp=[]
		for i in range(8):
			temp1=[]
			for j in range(4):
				t = fileLines[i][j]
				t = t[::-1]
				temp1.append(t)
			temp.append(temp1)

		# print(temp)
		return temp

	def addRoundKey(self, fileLines, key):

		temp=[]
		for i in range (8):
			temp1=[]
			for j in range(4):
				temp2 = int(fileLines[i][j],16) | int(key[i][j],16)
				temp1.append(str(hex(temp2)[2:]))
			temp.append(temp1)
			# print(temp)
		
		return temp




key = [[['89', '50', '4e', '47'], ['0d', '0a', '1a', '0a'], ['00', '00', '00', '0d'], ['49', '48', '44', '52'], ['00', '00', '05', 'a0'], ['00', '00', '03', '84'], ['08', '06', '00', '00'], ['00', '57', '4d', '96']], [['d2', '00', '00', '18'], ['56', '69', '43', '43'], ['50', '49', '43', '43'], ['20', '50', '72', '6f'], ['66', '69', '6c', '65'], ['00', '00', '58', '85'], ['95', '59', '07', '54'], ['54', '4b', '93', 'ee']], [['3b', '79', '86', '3c'], ['43', 'ce', '39', '83'], ['e4', '9c', '73', 'ce'], ['19', '44', '60', '48'], ['43', '12', '86', '28'], ['a0', '08', '22', '92'], ['14', '41', '05', '04'], ['45', '45', '24', 'aa']], [['a8', '28', 'a0', '22'], ['08', '62', '40', '51'], ['82', '0f', '44', '44'], ['04', '91', 'a0', 'a2'], ['80', '0a', '2a', '41'], ['f6', '12', 'f4', 'bd'], ['7d', 'ff', '9e', 'dd'], ['b3', '7d', '4e', 'df']], [['fb', '4d', '75', '75'], ['75', '55', '75', '75'], ['a8', '3b', '00', '70'], ['ed', 'f7', '8d', '8c'], ['0c', '43', '30', '02'], ['10', '1e', '11', '43'], ['75', '30', '35', 'e0'], ['77', '73', 'f7', 'e0']], [['c7', '4e', '00', '02'], ['60', '01', 'cc', '40'], ['11', '88', 'fa', '92'], ['a3', '23', 'f5', 'ed'], ['ec', 'ac', '00', '5c'], ['7e', 'bf', 'ff', '7b'], ['59', '1a', '04', 'd0'], ['c6', 'fb', 'b9', 'cc']], [['86', 'ac', 'ff', '6c'], ['ff', '5f', '0b', '93'], ['7f', '40', '34', '19'], ['00', 'c8', '0e', 'c6'], ['7e', 'fe', 'd1', 'e4'], ['70', '18', '5f', '07'], ['00', '95', '46', '8e'], ['a4', 'c6', '00', '80']], [['51', '83', 'e9', '42'], ['f1', '31', '91', '1b'], ['d8', '0b', 'c6', 'cc'], ['54', '58', '41', '18'], ['47', '6e', 'e0', 'a0'], ['2d', '9c', 'be', '81'], ['fd', 'b6', '70', 'f1'], ['26', '8f', '93', '83']], [['21', '8c', '2f', '02'], ['80', 'a3', 'f5', 'f5'], ['a5', '06', '01', '40'], ['df', '0c', 'd3', 'f9'], ['e3', 'c8', '41', 'b0'], ['1c', 'fa', '21', 'b8'], ['8d', '18', 'e1', '4f'], ['89', '80', '59', '67']], [['61', 'ac', '43', '0e'], ['f6', 'f5', '07', '80'], ['4b', '1a', 'e6', '91'], ['0e', '0f', 'df', 'bd'], ['81', 'dd', '60', '2c'], ['ee', 'f7', '0f', '39'], ['41', 'ff', '4d', 'a6'], ['df', '1f', '99', 'be']], [['be', '41', '7f', 'f0'], ['96', '2d', '9b', '05'], ['67', '44', '89', '8e'], ['0c', 'f3', 'dd', 'f3'], ['ff', '74', 'c7', 'ff'], ['5d', 'c2', 'c3', '62'], ['7f', '8f', '21', '0a'], ['57', 'da', '60', 'aa']], [['99', 'c3', '86', 'cd'], ['b0', 'df', '86', '42'], ['77', '5b', '6e', '60'], ['5a', '18', 'cf', '46'], ['f8', 'd9', 'd8', 'c2'], ['98', '08', 'e3', '1f'], ['14', 'ff', '4d', '7e'], ['18', '23', '08', 'c1']], [['b1', '66', 'ce', '5b'], ['fc', '08', '6e', '72'], ['b4', '21', 'ec', '33'], ['c0', '0a', '63', '39'], ['7f', '5f', '23', '4b'], ['18', '73', 'c3', 'd8'], ['24', '22', 'cc', 'c6'], ['6a', '9b', 'ee', '17']], [['48', '31', '31', '87'], ['31', '1c', '21', '88'], ['04', '4a', '8c', 'b9'], ['d3', '76', 'df', 'cc'], ['80', '68', '63', 'c7'], ['6d', '99', 'a7', 'a8'], ['bb', '1d', '6c', '7f'], ['e3', '40', 'aa', 'a1']]]

hd = Aes("/Users/hd/Documents/codes/python/encryption/1.png")
hd.getFile()

for i in range(len(hd.file_lines)):
	for j in range(14):
		temp_lines = hd.file_lines[i]
		temp_lines = hd.sbox(temp_lines)
		temp_lines = hd.shiftRows(temp_lines)
		temp_lines = hd.mixCols(temp_lines)
		temp_lines = hd.addRoundKey(temp_lines, key[j])
		# break
		hd.file_lines[j] = temp_lines
	# break








