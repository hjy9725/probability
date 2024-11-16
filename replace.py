import os

# 获取当前目录下所有.md文件
md_files = [file for file in os.listdir() if file.endswith('.md')]

for filename in md_files:
    # 打开文件读取内容
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换 " $" 为 "$"
    new_content = content.replace(" $", "$")
    new_content = content.replace("$", " $")
    new_content = content.replace("$ $", "$$")
    
    # 将修改后的内容写回文件
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
    print(f"已成功替换文件: {filename}")
import os

def replace_dollar_signs_in_md_files(root_dir="."):
    # 遍历指定路径下的所有文件和子目录
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # 检查文件是否为 .md 文件
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                # 读取文件内容并替换 $ 为 " $"
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # 使用替换方法
                new_content = content.replace(" $", "$")
                new_content = new_content.replace("$", " $")
                new_content = new_content.replace("$ $", "$$")
                
                # 写回文件
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                
                print(f"已成功替换文件: {file_path}")

# 运行函数，处理当前目录及所有子目录下的 .md 文件
replace_dollar_signs_in_md_files(".")
