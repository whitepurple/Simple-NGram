class NGram:
    def __init__(self, lines, n=1):
        self.lines = lines
        self.ngram(n) #N=3
        self.num = n
        

    def showTitles(self, keyword):
        return [self.lines[i] for i in self.gram_freq[keyword].index]

    class info:
        def __init__(self):
            self.freq = 0
            self.index = []

        def __repr__(self):
            return str(self.freq)

    def ngram(self, n=1):
        self.num = n
        result = dict()
        for i, title in enumerate(self.lines):
            tokens = title.split(' ')
            for gram in list(zip(*[tokens[i:] for i in range(n)])):
                gram_text = ' '.join(list(gram)).lower()
                if gram_text not in result:
                    result[gram_text] = self.info()
                result[gram_text].freq += 1
                result[gram_text].index.append(i)
        self.gram_freq_sorted = sorted(result.items(), key=lambda x:x[1].freq,reverse=True)
        self.gram_freq = result
        return self
        
        
