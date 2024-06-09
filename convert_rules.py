import os

# 输入文件夹和输出文件夹路径
input_folder = 'rules'
output_folder = 'converted_rules'

# 确保输出文件夹存在，如果不存在则创建
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 只处理以 .rules 结尾的文件
    if filename.endswith('.rules'):
        # 构建输入文件的完整路径
        input_path = os.path.join(input_folder, filename)
        
        # 读取输入文件内容
        with open(input_path, 'r') as infile:
            lines = infile.readlines()
            # 过滤掉注释行（以 '#' 开头）和空行，并去除每行的首尾空白字符
            payload = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    # 根据是否为IPv6地址选择前缀
                    if ':' in line:
                        payload.append(f"IP-CIDR6,{line},no-resolve")
                    else:
                        payload.append(f"IP-CIDR,{line},no-resolve")

        # 创建新的文件名，替换扩展名为 .txt
        new_filename = f"{os.path.splitext(filename)[0]}.txt"
        output_path = os.path.join(output_folder, new_filename)

        # 手动写入YAML格式的文件
        with open(output_path, 'w') as outfile:
            outfile.write('payload:\n')
            for item in payload:
                outfile.write(f"  - '{item}'\n")

        # 输出转换文件的信息到控制台
        print(f"Converted {input_path} to {output_path}")

# 输出转换完成的信息到控制台
print("Rule conversion completed.")
