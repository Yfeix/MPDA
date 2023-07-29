import pandas as pd

def result_processing(filename):

    # filename = '训练结果（原始） - 副本.csv'
    df = pd.read_csv(filename)
    # print(df)

    # 按cwe-name列进行分组
    grouped = df.groupby("CWE-name")


    # 创建一个空的数据帧，用于保存修改后的CSV文件
    new_df = pd.DataFrame(columns=df.columns)

    for name, group in grouped:
        # 在每个分组的最后一行添加一个空行
        new_row = ["" for _ in range(len(df.columns))]
        new_df = pd.concat([new_df, group, pd.DataFrame([new_row], columns=df.columns)], ignore_index=True)
        # group.loc[group.index[-1]+1] = ["" for _ in range(len(df.columns))]

    new_df = new_df.rename(columns={"Placeholder": ""})
    new_df = new_df.rename(columns={"Placeholder.1": ""})
    new_df = new_df.rename(columns={"Placeholder.2": ""})
    new_df.to_csv(filename, index=False)