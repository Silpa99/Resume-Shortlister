import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def parsepdf(file_path,job_desc):
    resume = docx2txt.process(file_path)
    job_description = job_desc
    text = [resume,job_description]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal
    if matchPercentage >60:
        return False
    else:
        return True