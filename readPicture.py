# -*- coding: utf-8 -*-

import tesserocr
from re import sub, match

class ReadPicture:
	"""
		Represent extracted data about a picture

		PROPERTIES
		title (String) : Title of the chess game
		data (String) : Extracted PGN data from the picture
	"""

	def __init__(self,picturePath):
		"""
			Initialization of a ReadPicture instance
			picturePath (String) : the path of the picture
			RETURN void
		"""
		self.data=ReadPicture.pictureToText(picturePath)
		self.dataSetTitle()
		self.data=self.data.replace('\n',' ')
		self.dataReplaceSymbols()

	def pictureToText(picturePath):
		"""
			STATIC FUNCTION			
			Get untreated data from the picture
			picturePath (String) : the path of the picture
			RETURN String
		"""
		api = tesserocr.PyTessBaseAPI() # path='C:/Anaconda3/tessdata' on Windows in USMB
		api.SetImageFile(picturePath)
		return api.GetUTF8Text()

	def dataSetTitle(self):
		"""
			Extract title from data
			RETURN List(String,String) The title + the game
		"""
		dataBegin=False
		if(not dataBegin and '\n1.' in self.data):
			dataBegin='\n1.'
		if(not dataBegin and ' 1.' in self.data):
			dataBegin=' 1.'
		dataBegin=self.data.index(dataBegin)+1
		self.title=self.data[:dataBegin].strip()
		self.data=self.data[dataBegin:].strip()
		dataEnd=False
		if(not dataEnd and '0-1' in self.data):
			dataEnd='0-1'
		if(not dataEnd and '1-0' in self.data):
			dataEnd='1-0'
		if(not dataEnd and '1/2-1/2' in self.data):
			dataEnd='1/2-1/2'
		if(not dataEnd and '½-½' in self.data):
			dataEnd='½-½'
		if(not dataEnd and '*' in self.data):
			dataEnd='*'
		if(dataEnd):
			dataEnd=self.data.index(dataEnd)+len(dataEnd)
			self.title=self.title+self.data[dataEnd:]
			self.data=self.data[:dataEnd]

	def dataReplaceSymbols(self):
		"""
			Correct bad data and put chess pawns
			RETURN void
		"""
		replaceSymbols=[
			(' K',' \u2654'), # King
			('.K','.\u2654'), # King
			(' W',' \u2655'), # Queen
			('.W','.\u2655'), # Queen
			(' Q',' \u2655'), # Queen
			('.Q','.\u2655'), # Queen
			(' H',' \u2656'), # Rook
			('.H','.\u2656'), # Rook
			(' R',' \u2656'), # Rook
			('.R','.\u2656'), # Rook
			(' fi',' \u2656'), # Rook
			('.fi','.\u2656'), # Rook
			(' B',' \u2657'), # Bishop
			('.B',' \u2657'), # Bishop
			(' 2',' \u2657'), # Bishop
			(' \u2657.',' 2.'),
			(' \u26570',' 20'),
			(' \u26571',' 21'),
			(' \u26572',' 22'),
			(' \u26573',' 23'),
			(' \u26574',' 24'),
			(' \u26575',' 25'),
			(' \u26576',' 26'),
			(' \u26577',' 27'),
			(' \u26578',' 28'),
			(' \u26579',' 29'),
			('.2','.\u2657'), # Bishop
			('@','\u2658'), # Knight
			(' N',' \u2658'), # Knight
			('.N','.\u2658'), # Knight
			(' O',' \u2658'), # Knight
			('.O','.\u2658'), # Knight
			(' A',' \u2658'), # Knight
			('.A','.\u2658'), # Knight
			(' G',' \u2658'), # Knight
			('.G','.\u2658'), # Knight
			(' 0',' \u2658'), # Knight
			(' \u2658-0',' 0-0'), # Knight
			('.0','.\u2658'), # Knight
			('.\u2658-0','.0-0'), # Knight
			(' 4',' \u2658'), # Knight
			(' \u2658.',' 4.'),
			(' \u26580',' 40'),
			(' \u26581',' 41'),
			(' \u26582',' 42'),
			(' \u26583',' 43'),
			(' \u26584',' 44'),
			(' \u26585',' 45'),
			(' \u26586',' 46'),
			(' \u26587',' 47'),
			(' \u26588',' 48'),
			(' \u26589',' 49'),
			('.4','.\u2658'), # Knight
			# Divers
			('€','e'),
			(' 9',' g'),
			(' g.',' 9.'),
			('.9','.g'),
			('S','5'),
			('d ','5 '),
			('é','6'),
			('B','8'),
			(',','.'),
			('. ', '.')
		]
		for r in replaceSymbols:
			self.data=self.data.replace(r[0],r[1])
