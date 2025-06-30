import os
from matcher.tfidf_vectorizer import build_tfidf_matrix
from matcher.cosine_similarity import compute_cosine_similarity

def read_text_file(filepath):
    """读取文本文件内容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def match_resume_to_jd(resume_path, jd_path):
    """
    主函数：读取简历和JD，计算匹配分数

    参数:
        resume_path: 简历文件路径
        jd_path: 岗位描述文件路径

    返回:
        匹配得分（余弦相似度）
    """
    resume_text = read_text_file(resume_path)
    jd_text = read_text_file(jd_path)

    documents = [resume_text, jd_text]
    tfidf_matrix, _ = build_tfidf_matrix(documents)
    score = compute_cosine_similarity(tfidf_matrix, 0, 1)

    return round(score, 4)

if __name__ == "__main__":

    resume_file = 'data/resumes/resume1.txt'
    jd_file = 'data/job_descriptions/jd1.txt'

    if not os.path.exists(resume_file) or not os.path.exists(jd_file):
        print("文件路径不存在，请检查。")
    else:
        score = match_resume_to_jd(resume_file, jd_file)
        print(f"匹配得分（简历 vs JD）: {score}")

