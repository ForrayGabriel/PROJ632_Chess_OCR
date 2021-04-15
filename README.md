# PROJ632 : Chess OCR
A datascience project about extracting text from a picture of the moves of a chess game and storing them in a PGN file

We tried to use Tesseract OCR to retreive the text from the picture.
Our first problem was that Tesseract does not know how to read chess pieces and translated them as letters. The second problem was that these letter were not always the same for the same chess piece, making it very hard to process.

So this project was mainly about trying to create a new language for Tesseract.

We did it by using [this tutorial](https://towardsdatascience.com/simple-ocr-with-tesseract-a4341e4564b6)

In this repository you can find two folders name chess font v1 and v2. The first one is a failure that we trained with only the chess pieces and can't read alphabetical characters. We tried to assign an unsued accentued letter to every piece.
The second one is a bit better, we trained it with the image visible in Exemple - Jtessbox.png, and we assigned chess pieces to their unicode character. But our training set was not big enought and we still have a lot of errors that make it hard to exploit.

"Image a tester" is the picture we want to extract text from, and "resultat.txt" the text we were able to exctract using our chess font v2.

Test_tesseract was a first attempt to apply filters to an image and read it using the tesseract python librairy for further usage if we were able to correctly read text.
