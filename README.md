# 职航AI：大模型赋能的智能面试教练系统
本项目为“职教AI·数字人面试模拟教练”的算法性能测试，构建一个集简历解析、岗位匹配、情绪识别、智能问答与面试评分于一体的智能评估系统，用于服务高职学生的就业训练与职业发展。

## 项目结构

zhihang-ai-algo-eval/

├── data/ # 测试用样本数据（简历、岗位JD、问答样本等）

├── resume_parser/ # 简历解析模块（spaCy NER 实体提取）

├── jd_parser/ # 岗位信息解析模块（关键词匹配）

├── matcher/ # 岗位匹配度计算模块（TF-IDF + Cosine）

├── emotion_eval/ # 情绪识别模块（FER+模型评估）

├── qna_eval/ # 问答生成与评估模块（DeepPavlov + BLEU）

├── requirements.txt # Python依赖环境配置

└── README.md # 项目说明文件

## 功能模块说明
### 1. 简历解析（resume_parser/）
使用 spaCy NER 模型自动提取简历中的：姓名、学历、技能、工作经历等关键信息，支持 PDF、DOCX、TXT 格式，模拟 HR 结构化简历筛选流程。

### 2. 岗位信息提取（jd_parser/）
从岗位描述中提取技能关键词，生成岗位标签结构化表示，可用于与简历进行技能匹配与重合度分析。

### 3. 简历与岗位匹配（matcher/）
使用 TF-IDF 将简历和岗位文本向量化，使用余弦相似度计算匹配度得分，输出匹配排名与评估分数。

### 4. 情绪识别模块（emotion_eval/）
使用 FER+ 模型识别人脸情绪（支持图像或 CSV 数据），输出分类标签、稳定性评估，可作为面试视频情绪分析依据。

### 5. 问答生成与评估（qna_eval/）
使用 DeepPavlov 模型加载 SQuAD 问答，提供 BLEU 指标评估回答质量，可扩展为模拟结构化面试对答过程。

## 模型与代码来源致谢
AjNavneet/Resume-Parser-Spacy-NER

keshavbansal015/Job-Description-Parser

SeekAI-786/Resume-Analyzer

microsoft/FERPlus

deeppavlov/DeepPavlov

## 使用说明
本项目作为“数字人面试模拟教练”系统的功能验证与算法性能测试模块，用于展示关键技术路径与核心模型的集成逻辑。部分模块基于开源模型改编构建，用于教学展示与大赛演示，不用于商用部署。示例数据（简历、岗位、图像等）仅为测试使用，系统代码以验证算法可行性为主，非完整应用版本。
