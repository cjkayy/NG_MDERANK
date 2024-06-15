import operator
import yake
import pandas as pd

df = pd.read_csv("D:\\eight_description.csv", header=None, index_col=0)


dataresult = []
indexresult = []

indexresult = df.index

for i in df.values:
    text = str(i[0]) + ""
    datatest = []
    kw_extractor = yake.KeywordExtractor()
    language = "en"
    max_ngram_size = 1 #最大关键词语长度
    deduplication_threshold = 0.9 #设置在关键词中是否可以重复单词
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    keywords.sort(key=operator.itemgetter(1), reverse=True)
    for i in keywords:
        datatest.append(i[0])
    dataresult.append(datatest)

dd = pd.DataFrame(dataresult, index=indexresult)
dd.to_csv("D:\\eight_description_result_yake_2.csv", header=False)
