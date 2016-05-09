# LatentDirichletAllocationPreprocessing

This tool was developed to preprocess data for LDA (Latent Dirichlet Allocation) topic modeling.
The output is to be used in conjunction with the LDA C++ project available in my list of projects.

# Usage

```
python LDA.py createKFold -h
```

```
usage: LDA.py createKFold [-h] [--test_frac TEST_FRAC] [--k K]
                          [--output OUTPUT] [--debug]
                          corpus vocabulary

positional arguments:
  corpus                path to the corpus file
  vocabulary            path to the vocabulary file

optional arguments:
  -h, --help            show this help message and exit
  --test_frac TEST_FRAC fraction of corpus documents to retain as test set
                        (default: 0)
  --k K                 number of folds (default: 1, no validation set)
  --output OUTPUT       output files directory (default: same directory of
                        input)
  --debug               debug flag (default: false)
```

# Input corpus and vocabulary

The corpus and vocabulary files must be in the form of the datasets present at the url [http://archive.ics.uci.edu/ml/datasets/Bag+of+Words](http://archive.ics.uci.edu/ml/datasets/Bag+of+Words).

#License

Copyright 2016 Marco Righini

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
