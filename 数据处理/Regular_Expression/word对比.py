import re


def getText(wordname)
    '''
    提取文字
    :param wordname: 
    :return: 
    '''
    d=Document(wordname)
    texts=[]
    for para in d.paragraphs:
        texts.append(para.text)
    retu texts

def is_Chinese(word):
    '''
    识别中文
    :param word:
    :return:
    '''
    for ch in word:
        if '\u4e00' <=ch<='\u9fff':
            return True
        return False

def msplit(s,seperators=',|\.|\?|\，|\。|?|!|、'):
    '''
    根据标点符号分句
    :param s:
    :param seperators:
    :return:
    '''
    return re.split(seperators,s)


def resdDoc(docfile):
    '''
    读取文档
    :param docfile:
    :return:
    '''
    print(f'=======正在读取{docfile}========')
    paras=getText(docfile)
    seg=[]
    for p in paras:
        temp=[]
        for s in msplit(p):
            if len(s) >2:
                temp.append((s.replace(' ',"")))
            if len(temp)>0:
                seg.append(temp)
    return seg

def comparasion (doc1,doc2,p,s):
    if doc1==doc2:
        print('两个我word完全一致')
    else:
        if doc1[p][s]!=doc2[p][s]:
            print(f'第{p+1}段，第{s+1}句不相同:{doc1[p][s]}----->{doc2[p][s]}')

