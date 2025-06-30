import pandas as pd
from emotion_eval.ferplus_model import load_fer_model, predict_emotion

def run_inference_on_csv(csv_path):
    """
    从 CSV 文件中加载图像路径，执行情绪识别预测
    
    """
    # 加载模型
    model = load_fer_model()

    # 读取数据
    df = pd.read_csv(csv_path)
    if 'image_path' not in df.columns:
        raise ValueError("CSV 文件必须包含 'image_path' 列")

    # 执行预测
    predictions = []
    for path in df['image_path']:
        emotion = predict_emotion(model, path)
        predictions.append(emotion)

    df['predicted_emotion'] = predictions
    return df

if __name__ == "__main__":
    test_csv = 'data/emotion_testset/sample_emotions.csv'
    result_df = run_inference_on_csv(test_csv)
    print(result_df.head())
