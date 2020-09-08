def carga_keywords():
    keywords=[]
    with open('C:\GIT\Desafios\Ej 1\keywords.txt') as f:
        f1=list(f)
        for kw in f1:
            kw=kw.replace('\n','')
            keywords.append(kw)
        return keywords

carga_keywords()