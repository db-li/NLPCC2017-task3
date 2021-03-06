import get_data
import ROUGE


def cal_ROUGE(result_filepath):
	
	list_true_summary  = get_data.get_test_summary()
	f = open(result_filepath)
	list_predict_summary = []
	for i , line in enumerate(f.readlines()):
		list_predict_summary.append(line)
	#list_true_summary = [summary.encode("utf8") for summary in list_true_summary]

	print ROUGE.ROUGE1_character_based(list_predict_summary,list_true_summary)
	print ROUGE.ROUGE2_character_based(list_predict_summary,list_true_summary)
	ROUGE.ROUGE_SU4(list_predict_summary,list_true_summary,1)



if __name__ == "__main__":
	'''
	for k in range(25,31):
		print "k is %d"%(k)
		cal_ROUGE("./result/EK_tfidf_result/0504_k=%d.txt"%(k))
	'''

	#cal_ROUGE("./result/ES_textrank4zh_result/0518.txt")
	'''
	for k in range(10,20):
		print "k is %d"%(k)
		cal_ROUGE("./result/EK_textrank4zh_result/0520_k=%d.txt"%(k))
	'''

	#cal_ROUGE("./result/ES_snownlp_result/0520.txt")

	for k in range(10,20):
		print "k is %d"%(k)
		cal_ROUGE("./result/EK_snownlp_result/0521_k=%d.txt"%(k))
