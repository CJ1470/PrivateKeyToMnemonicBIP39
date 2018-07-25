import hashlib

#Accepting Input Key in hex format
PrivateKey = raw_input("Enter Hex Private Key: ")

#Converting hex key integer and then to binary string, removing prefix '0b'
PrivateKeyBin = bin(int(PrivateKey, 16))[2:]

#Calculating bit length of key
PrivateKeyLen = len(PrivateKeyBin)

#If key is valid length then calculate Mnemonic
if PrivateKeyLen == 256:

	#Calculating checksum bits, taking sha256 hash of key and considering only first 8 bit parts 
	ChkSum = hashlib.sha256(PrivateKeyBin).hexdigest()[:2]
	#Converting hash to bin and discaring prefix '0b'
	ChkSumBin = bin(int(ChkSum,16))[2:]

	#Padding Checksum with 0 to make it length 8
	if len(ChkSumBin) != 8:
		for x in range(1,(9-len(ChkSumBin))):
			ChkSumBin = '0' + ChkSumBin
			
	#Conmbining key with checksum
	PrivateKeyBinWithChkSum = PrivateKeyBin+ChkSumBin

	#load english wordlist to words var as list
	text_file = open("english.txt", "r")
	words = text_file.read().split('\n')
	text_file.close()

	#Initialising empty list for mnemonic
	MnemonicCodeWordList = []
	x=0
	#Considering only 11 bit iteratively of 264bit so as to get mnemonic index of each 24 words
	while x<264:
		#Considering 11 bit from x to x+11, for word it is 0-10 bits
		mnemoTemp = PrivateKeyBinWithChkSum[x:(x+11)]
		#Converting index from binary to int
		WordIndex = int(mnemoTemp,2)
		#Geting word by indes and adding it to required mnemonic word list
		MnemonicCodeWordList.append(words[WordIndex])
		#Incrementing x by 11 to get next word
		x=x+11

	MnemonicCodeWords = " "
	#Print mnemonic by first converting array to space seperated word string 
	print "Mnemonic words for private key is:\n",MnemonicCodeWords.join(MnemonicCodeWordList)

else:
	print "Incorrect Input"
	print "Sample: E9873D79C6D87DC04B6A5778633389F4453213303DA61F20BD67FC233AA33262"

#E9873D79C6D87DC04B6A5778633389F4453213303DA61F20BD67FC233AA33262