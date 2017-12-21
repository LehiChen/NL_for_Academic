import jieba,os,nltk
import jieba.analyse
from matplotlib import pyplot as plt

def ishan(text):
    return all('\u4e00' <= char <= '\u9fff' for char in text)

def join_list(list_):
	long_sentence = ""
	for item in list_:
		long_sentence += (item + "\n")
	return long_sentence

def FreqDict_to_Dict(txt_freq):
	FreqDict = {}
	for i in txt_freq:
		FreqDict[i] = txt_freq[i]
	return FreqDict

def get_freq_from_file(path):
	with open(path,'r',encoding = 'UTF-8') as f:
		demo = f.readlines()
		demo = join_list(demo)
		txt_spited = jieba.lcut(demo,cut_all=False)
		tags = jieba.analyse.extract_tags(demo,topK = 10)
		txt_freq = nltk.FreqDist(txt_spited)
		freq_dict = FreqDict_to_Dict(txt_freq)
		freq_dict_final = {}
		for tag in tags:
			freq_dict_final[tag] = freq_dict[tag]
		return freq_dict_final

def count_in_main(main,temp):
	for tag in temp.keys():
		if tag in main.keys():
			main[tag] += temp[tag]
		else:
			main[tag] = temp[tag]
	return main
def sort_dict(dic):
	new_dic = {}
	dic_list = sorted(dic.items(),key=lambda item:item[1],reverse=True)
	for key,value in dic_list:
		new_dic[key] = value
	return new_dic

if __name__ == '__main__':
	main_freq_dict = {}
	file_list = os.listdir('lyrics')
	for txt in file_list:
		print(txt)
		freq_dict = get_freq_from_file('lyrics//%s'%txt)
		main_freq_dict = count_in_main(main_freq_dict,freq_dict)
	main_freq_dict = sort_dict(main_freq_dict)
	with open('result.csv','w') as f:
		string = ""
		for tag in main_freq_dict.keys():
			string += "%s,%d\n"%(tag,main_freq_dict[tag])
		f.write(string) 
	pass