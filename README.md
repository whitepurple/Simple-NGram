# Simple-NGram
Analysis of 2020 Accepted Papers(ACL, EMNLP) using N-Gram

## Usage
```python
NGram(paper_2020_list).ngram(2).gram_freq_sorted[:10]
```
```[('machine translation', 83),
 ('neural machine', 59),
 ('language models', 59),
 ('natural language', 50),
 ('question answering', 46),
 ('for neural', 32),
 ('learning to', 32),
 ('model for', 31),
 ('learning for', 30),
 ('text classification', 24)]
 ```
```python
NGram(paper_2020_list,2).showTitles('generation with')[:3]
```
```
['Diverse and Informative Dialogue Generation with Context-Specific Commonsense Knowledge Awareness',
 'Diversifying Dialogue Generation with Non-Conversational Text',
 'Evidence-Aware Inferential Text Generation with Vector Quantised Variational AutoEncoder']
```
 
## License
MIT License
