import nbformat

from nbconvert.preprocessors import ExecutePreprocessor

OK = {
  "name": "Homework 2",
  "endpoint": "cal/phy151/fa17/homework1",
  "src": ['HW1.ipynb'],
  "tests": { },
  "protocols": [
      "file_contents",
      "grading",
      "backup"
  ]
}

import copy
import json

def run(OK):
    OK = copy.deepcopy(OK)
    for i in range(len(OK['src'])):
        ipynb = OK['src'][i]
        eipynb = 'executed-' + ipynb
        runone(ipynb, eipynb)
        OK['src'][i] = eipynb
    return OK

def runone(ipynb, eipynb):

    with open(ipynb) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    print("running all cells from notebook", ipynb)

    #ep.preprocess(nb, {'metadata': {'path': './'}})

    with open(eipynb, 'wt') as f:
        nbformat.write(nb, f)
    return eipynb

def push(OK):
    with open('ok.py', 'wt') as f:
        json.dump(OK, f)

    from client.api.notebook import Notebook

    ok = Notebook('ok.py')
    ok.auth(inline=True)
    ok.submit()

OK = run(OK)
push(OK)
