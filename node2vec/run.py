import argparse

from gensim.models import Word2Vec
from argparse import RawTextHelpFormatter
from gensim.models import KeyedVectors

def convert(dataset, model_file, graphtype):
	try:
		W = KeyedVectors.load(model_file)
	except Exception as e:
		raise e

	W.wv.save_word2vec_format(dataset + '/embeddings/' + dataset + '_node2vec_'+ graphtype + '.txt')


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate Embeddings for ACA, APA and APC graphs using node2vec.',
									 formatter_class=RawTextHelpFormatter)
	parser.add_argument('-d','--dataset', dest='dataset', required=True,
			    help='Dataset. Choose among following: \ndblp \naminer \ndbis')
	parser.add_argument('-f','--model_file', dest='model_file', required=True,
			    help='The embedding binary file generated by node2vec.')
	parser.add_argument('-g','--graphtype', dest='graphtype', required=True,
			    help='The graphtype. Choose among following: \nclique \nstar')

	args = parser.parse_args()
	convert(args.dataset, args.model_file, args.graphtype)
