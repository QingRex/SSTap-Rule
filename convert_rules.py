import os
import yaml
from yaml.representer import SafeRepresenter

# 输入文件夹和输出文件夹路径
input_folder = 'rules'
output_folder = 'converted_rules'

# 确保输出文件夹存在，如果不存在则创建
os.makedirs(output_folder, exist_ok=True)

# 自定义的字符串类型，确保YAML序列化时使用单引号
class SingleQuotedScalarString(str):
    pass

def single_quoted_scalarstring_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")

yaml.add_representer(SingleQuotedScalarString, single_quoted_scalarstring_representer)

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
            # 同时为每个IP地址添加单引号
            payload = [SingleQuotedScalarString(line.strip()) for line in lines if line.strip() and not line.startswith('#')]

        # 创建新的文件名，替换扩展名为 .txt
        new_filename = f"{os.path.splitext(filename)[0]}.txt"
        output_path = os.path.join(output_folder, new_filename)

        # 将转换后的规则写入新的文件，并确保IP地址用引号包围
        with open(output_path, 'w') as outfile:
            yaml.dump({'payload': payload}, outfile, default_flow_style=False, allow_unicode=True)

        # 输出转换文件的信息到控制台
        print(f"Converted {input_path} to {output_path}")

# 输出转换完成的信息到控制台
print("Rule conversion completed.")
