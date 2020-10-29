# arxivs

Get arXiv AI paper.

## Install

```bash
pip install arxivs
```

## Usage

```python
import arxivs

paper_list = arxivs.get_paper(tags=["cs.CL"], days=1)

print(paper_list[0])
```

## Tag List

```bash
cs.AI: Artificial Intelligence
cs.CL: Computation and Language
cs.CV: Computer Vision and Pattern Recognition
cs.FL: Formal Languages and Automata Theory
cs.IR: Information Retrieval
cs.LG: Learning
cs.MA: Multiagent Systems
cs.NE: Neural and Evolutionary Computing
stat.ML: Machine Learning
```

## LICENSE

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
