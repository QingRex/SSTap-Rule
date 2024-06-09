import os
import yaml

# 输入文件夹和输出文件夹路径
input_folder = 'rules'
output_folder = 'converted_rules'

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 读取并转换规则
for filename in os.listdir(input_folder):
    if filename.endswith('.rules'):
        input_path = os.path.join(input_folder, filename)
        with open(input_path, 'r') as infile:
            lines = infile.readlines()
            payload = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

        # 创建新的文件名
        new_filename = f"{os.path.splitext(filename)[0]}.txt"
        output_path = os.path.join(output_folder, new_filename)

        # 将转换后的规则写入新的文件，并确保IP地址用引号包围
        with open(output_path, 'w') as outfile:
            yaml.dump({'payload': payload}, outfile, default_flow_style=False, allow_unicode=True, Dumper=yaml.SafeDumper)

        print(f"Converted {input_path} to {output_path}")

print("Rule conversion completed.")
