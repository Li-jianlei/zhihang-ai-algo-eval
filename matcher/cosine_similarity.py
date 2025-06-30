
from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(tfidf_matrix, idx1, idx2):
    """
    计算两个文档在 TF-IDF 向量下的余弦相似度

    参数:
        tfidf_matrix: 稀疏矩阵
        idx1, idx2: 要比较的两个文档在 tfidf_matrix 中的索引位置

    返回:
        相似度分数（0-1之间）
    """
    return cosine_similarity(tfidf_matrix[idx1], tfidf_matrix[idx2])[0][0]

