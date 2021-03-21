from pathlib import Path
import re
from copy import copy
from pprint import pprint
import sys

class NGram:
    def __init__(self, filenames, n=1,name=None):
        self.name = name
        lines = []
        for filename in filenames:
            p = Path(filename)
            with p.open(mode='rt', encoding='UTF-8') as f:
                line = f.readline().strip()
                while line.strip():
                    lines.append(line)
                    line = f.readline().strip()

        self.lines = lines
        print(f'{len(lines)} lines loaded from')
        pprint(filenames)
        self.ngram(n)
        self.num = n

    def ngram(self, n=1):
        self.num = n
        result = dict()
        for i, title in enumerate(self.lines):
            prep = re.sub('[^\w ]',' ',title)
            prep = re.sub('[ ]+',' ',prep)
            prep = prep.strip()
            tokens = prep.split(' ')
            for gram in zip(*[tokens[i:] for i in range(n)]):
                gram_text = ' '.join(gram).lower()
                try:
                    result[gram_text].freq += 1
                    result[gram_text].index.append(i)
                except:
                    result[gram_text] = self.Info([i])

        self.gram_freq = result
        return self
    
    @property
    def gram_freq_sorted(self):
        return sorted(self.gram_freq.items(), key=lambda x:x[1].freq,reverse=True)

    def show_titles(self, keyword):
        key= keyword.lower()
        if key in self.gram_freq:
            self.gram_freq[key].index_distict()
            return [self.lines[i] for i in self.gram_freq[key].index]
        else:
            return []

    class Info:
        def __init__(self, index=[]):
            self.freq = len(index)
            self.index = index

        def index_distict(self):
            self.index = list(set(self.index))
            self.freq = len(self.index)

        def __repr__(self):
            self.index_distict()
            return str(self.freq)

    @classmethod
    def stat(cls, ngramlist, tuplelist=False, total_to_last=False, top=10, stopword=True,console=True):
        '''
        doc string test
        '''
        if top == -1:
            top = sys.maxsize
        try:
            num = set()
            for n in ngramlist:
                if type(n) != cls:
                    raise
                num.add(n.num)
        except:
            print('this method need list of NGram object')
            return 

        if len(num) != 1:
            print('NGram objects must have same n-gram num')
            return

        stopwords = Path('stopwords.txt').open().read().split('\n')

        total = dict()

        maxlen = 0

        for n in ngramlist:
            for gram, info in n.gram_freq.items():
                if maxlen < len(gram):
                    maxlen = len(gram)

                try:
                    total[gram].freq += info.freq
                except:
                    total[gram] = copy(info)

        total_sorted = sorted(total.items(), key=lambda x:x[1].freq, reverse=True)

        header = ( f'{"gram":30s}' if console else 'gram', 'total', *[n.name for n in ngramlist])
    
        print(*header, sep='\t')

        view = [header]
        
        for gram, info in total_sorted:
            if stopword:
                flag=False
                if gram.split(' ')[0] in stopwords or gram.split(' ')[-1] in stopwords:
                    flag=True

                if flag:
                    continue

            line = (f'{gram:30s}' if console else gram, info, *[ngram.gram_freq[gram] if gram in ngram.gram_freq else 0 for ngram in ngramlist])
            print(*line, sep='\t')
            view.append(line)
            if len(view) > top:
                break

        if tuplelist:
            return view


        
        
