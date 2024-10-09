import pandas as pd


def clean_excel_file(input_file, output_file):
    # 读取Excel文件
    df = pd.read_excel(input_file, engine='openpyxl')

    # 移除全空的行和列
    df_cleaned = df.dropna(how='all').dropna(axis=1, how='all')

    # 将清洗后的数据写入新的Excel文件
    df_cleaned.to_excel(output_file, index=False)

    print(f"Data cleaned and saved to {output_file}")


if __name__ == "__main__":
    input_file = 'sample.xlsx'  # 输入的Excel文件路径
    output_file = 'cleaned_sample.xlsx'  # 输出的清洗后文件路径
    clean_excel_file(input_file, output_file)
