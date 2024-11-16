import os
import re

# 获取当前路径下的所有 .md 文件
md_files = [file for file in os.listdir() if file.endswith('.md')]

# 替换函数
def replace_dollar_signs(text):
    # 将 "$" 替换为 " $" 并考虑前后有无空格的情况
    text = re.sub(r'(\s?)\$(\s?)', r'\1 $\2', text)
    return text

# 遍历所有 .md 文件并进行替换
for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换操作
    new_content = replace_dollar_signs(content)
    
    # 将修改后的内容写回文件
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

print("所有 .md 文件中的 $ 符号已成功替换为 ' $ ' 格式。")
