import pandas as pd

# get first look
def getfirstlook(df, nrows=5, uniqueids=None):
    out = {}
    out['head'] = df.head(nrows)
    out['dtypes'] = df.dtypes
    out['nrows'] = df.shape[0]
    out['ncols'] = df.shape[1]
    out['index'] = df.index
    if (uniqueids is not None):
        out['uniqueids'] = df[uniqueids].nunique()
    return out

def displaydict(dicttodisplay):
    print(*(': '.join(map(str, x)) for x in dicttodisplay.items()), sep='\n\n')
    
