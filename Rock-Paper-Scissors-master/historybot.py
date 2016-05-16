# coding=UTF-8
if input == '': # initiera värdena för första rundan
	rockCount = paperCount = scissorsCount = 0
elif input == 'R':
	rockCount += 1
elif input == 'P':
	paperCount += 1
elif input == 'S':
	scissorsCount += 1

# Völj den som slår den som motspelaren använt mest

if rockCount > paperCount and rockCount > scissorsCount: #sten används mest
	output = 'P' # papper slår sten
elif paperCount > scissorsCount: #papper används mest
	output = 'S' # sax slår papper
else: #sax används mest
	output = 'R' # sten slår sax
