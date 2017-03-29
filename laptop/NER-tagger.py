from nltk.tag import StanfordNERTagger
import json

st = StanfordNERTagger('./ner-laptop-model.ser.gz', './stanford-ner.jar') 
dataModel = ["BRAND", "RAM", "HARDDISK", "DISLAY", "COLOR", "OS", "OTHER"]

infile = open('laptop-items.txt', 'r')

count=0
for line in infile.readlines():
	tg = st.tag(line.split())
	count+=1
	with open('result.json', 'a') as outfile:
		for tag in dataModel:
			elements = ' '.join([ele[0] for ele in tg if ele[1]==tag])
			jsonObject=json.dumps({tag:elements})
		json.dump({'Line':jsonObject}, outfile)
		
infile.close()
outfile.close()