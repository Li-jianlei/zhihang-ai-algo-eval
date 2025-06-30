
from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf_matrix(documents):
    """
    构建 TF-IDF 向量矩阵
    参数:
        documents: List[str]，包含简历文本和JD文本的列表
    返回:
        tfidf_matrix: 稀疏矩阵
        vectorizer: TfidfVectorizer 对象
    """
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    return tfidf_matrix, vectorizer

