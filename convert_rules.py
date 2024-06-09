import os
import yaml

# 输入文件夹和输出文件夹路径
input_folder = 'rules'
output_folder = 'converted_rules'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.rules'):
        input_path = os.path.join(input_folder, filename)
        
        with open(input_path, 'r') as infile:
            lines = infile.readlines()
            # 过滤掉注释行（以 '#' 开头）和空行，并去除每行的首尾空白字符
            # 同时为每个IP地址添加单引号
            payload = [f"'{line.strip()}'" for line in lines if line.strip() and not line.startswith('#')]

        new_filename = f"{os.path.splitext(filename)[0]}.txt"
        output_path = os.path.join(output_folder, new_filename)

        with open(output_path, 'w') as outfile:
            yaml.dump({'payload': payload}, outfile, default_flow_style=False, allow_unicode=True)

        print(f"Converted {input_path} to {output_path}")
        
print("Rule conversion completed.")
