'''

@author: Righini Marco
'''

import argparse as ap
import libs.preprocessing as prep
import os
import cProfile
import random


def main():
    random.seed()
    
    parser = ap.ArgumentParser(description='Tool creating datasets for LDA topic modeling')
    subparsers = parser.add_subparsers(title='subcommands')
    
    parser_createDataset = subparsers.add_parser('createKFold', help='create K training-validation couples using k-fold. First of all retains a part of corpus for testset')
    parser_createDataset.add_argument('corpus', help='path to the corpus file')
    parser_createDataset.add_argument('vocabulary', help='path to the vocabulary file')
    parser_createDataset.add_argument('--test_frac', type=float, default=0.0, help='fraction of corpus documents to retain as test set (default: 0)')
    parser_createDataset.add_argument('--k', type=int, default=1, help='number of folds (default: 1, no validation set)')
    parser_createDataset.add_argument('--output', help='output files directory (default: same directory of input)')
    parser_createDataset.add_argument('--debug', action="store_true", help='debug flag (default: false)')
    parser_createDataset.set_defaults(func=prep.createKFold)
    
    args = parser.parse_args()
    
    args.func(args)
    
if __name__ == '__main__':
    main()
