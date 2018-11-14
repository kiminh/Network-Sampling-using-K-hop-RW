import argparse
from argparse import RawTextHelpFormatter

type_ = 'aca'

def convert(dataset, model_file, graphtype):
	try:
		file = open(model_file)
	except Exception as e:
		raise e

	outname = dataset + '/embeddings/' + dataset +'_metapath2vec_embedding_' + type_ + '_' + graphtype + '.txt'
	print("Saving to: " + outname)
	outfile = open(outname , 'w')
	# Skip 2nd line (embedding for '<s>')
	count = 0
	lines = file.readlines()
	for line in lines:
		count += 1
		outfile.write(line)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate Embeddings for ACA, APA and APC graphs using metapath2vec.',
									 formatter_class=RawTextHelpFormatter)
	parser.add_argument('-d','--dataset', dest='dataset', required=True,
			    help='Dataset. Choose among following: \ndblp \nacm')
	parser.add_argument('-f','--model_file', dest='model_file', required=True,
			    help='The embedding binary file generated by node2vec.')
	parser.add_argument('-g','--graphtype', dest='graphtype', default="clique",
			    help='Type of edgelist. Choose among following: \nclique \nstar')

	args = parser.parse_args()
	convert(args.dataset, args.model_file, args.graphtype)
