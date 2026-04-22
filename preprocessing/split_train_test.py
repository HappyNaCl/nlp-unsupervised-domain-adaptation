import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

df = pd.read_csv('./datasets/lazada_final.csv')

pos = df[df['label'] == 'positive']
neg = df[df['label'] == 'negative']

# downsample positive to match negative count
pos_down = resample(pos, replace=False, n_samples=len(neg), random_state=42)

df_balanced = pd.concat([pos_down, neg]).sample(frac=1, random_state=42).reset_index(drop=True)

train_df, test_df = train_test_split(
    df_balanced, 
    test_size=0.2,        # 80% train, 20% test
    random_state=42,
    stratify=df_balanced['label']  # keeps pos/neg balance in both splits
)

print(f"Train: {len(train_df)} | Test: {len(test_df)}")
print(train_df['label'].value_counts())
print(test_df['label'].value_counts())

train_df.to_csv('./datasets/lazada_train.csv', index=False)
test_df.to_csv('./datasets/lazada_test.csv', index=False)