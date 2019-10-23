filename1='/home/lancelot/Sub-word-LSTM/Data/IIITH_Codemixed.txt'
file1= open(filename1, 'rt')
text1=file1.readlines()
file1.close()
res='/home/lancelot/Sub-word-LSTM/Data/preprocess1.txt'
new_file=open(res,"a+")
i=0
while(i!=len(text1)):
    new_file.writelines(["%s " % item for item in text1[i].split()[1:len(text[i])-3]])
    new_file.write('\n')
    i=i+1
new_file.close()

filename1='/home/lancelot/Sub-word-LSTM/Data/preprocess1.txt'
file1= open(filename1, 'rt')
text1=file1.readlines()
file1.close()
all=[]
from nltk.tokenize import word_tokenize
i=0
#print(text1[1].split())
while(i!=len(text1)):
    all.append(word_tokenize(text1[i]))
    i=i+1
print(all)