import os
import yaml

input_folder = 'rules'
output_folder = 'converted_rules'

os.makedirs(output_folder, exist_ok=True)

# 自定义的Dumper类
class SingleQuotedDumper(yaml.SafeDumper):
    def represent_scalar(self, tag, value, style=None):
        if tag == 'tag:yaml.org,2002:str' and not value.startswith("'") and not value.endswith("'"):
            return super().represent_scalar(tag, value, style="'")
        return super().represent_scalar(tag, value, style)

for filename in os.listdir(input_folder):
    if filename.endswith('.rules'):
        input_path = os.path.join(input_folder, filename)
        
        with open(input_path, 'r') as infile:
            lines = infile.readlines()
            payload = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

        new_filename = f"{os.path.splitext(filename)[0]}.txt"
        output_path = os.path.join(output_folder, new_filename)

        with open(output_path, 'w') as outfile:
            # 使用自定义的SingleQuotedDumper类将字典 {'payload': payload} 写入文件
            yaml.dump({'payload': payload}, outfile, default_flow_style=False, allow_unicode=True, Dumper=SingleQuotedDumper)

        print(f"Converted {input_path} to {output_path}")

print("Rule conversion completed.")

