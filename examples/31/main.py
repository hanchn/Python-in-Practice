#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLES_DIR = os.path.join(ROOT_DIR, "examples")
README_PATH = os.path.join(ROOT_DIR, "README.md")

def parse_readme():
    """从README.md文件中解析示例项目列表"""
    examples = []
    
    try:
        with open(README_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 使用正则表达式匹配示例项目
        pattern = r'\[(\d+)\.\s+(.*?)\]\(examples/(\d+)/README\.md\)'
        matches = re.findall(pattern, content)
        
        for match in matches:
            num, name, dir_num = match
            examples.append({
                'num': num,
                'name': name,
                'dir': dir_num
            })
            
        return examples
    except Exception as e:
        print(f"解析README.md时出错: {e}")
        return []

def create_example_structure(example):
    """创建示例项目的目录结构"""
    num = example['num']
    name = example['name']
    dir_num = example['dir']
    
    # 创建示例目录
    example_dir = os.path.join(EXAMPLES_DIR, dir_num)
    if not os.path.exists(example_dir):
        os.makedirs(example_dir)
        print(f"创建目录: {example_dir}")
    else:
        print(f"目录已存在: {example_dir}")
    
    # 创建 README.md 文件
    readme_path = os.path.join(example_dir, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {num}. {name}\n\n")
            f.write("## 项目介绍\n\n")
            f.write("这是一个Python实践项目，用于...\n\n")
            f.write("## 功能特点\n\n")
            f.write("- 功能1\n")
            f.write("- 功能2\n")
            f.write("- 功能3\n\n")
            f.write("## 使用方法\n\n")
            f.write("```python\n")
            f.write("# 示例代码\n")
            f.write("```\n\n")
            f.write("## 依赖库\n\n")
            f.write("- 依赖1\n")
            f.write("- 依赖2\n\n")
        print(f"创建文件: {readme_path}")
    else:
        print(f"文件已存在: {readme_path}")
    
    # 创建示例代码文件
    main_file = "main.py"
    if name.lower().find("web") >= 0 or name.lower().find("api") >= 0:
        main_file = "app.py"  # Web应用通常使用app.py
    
    code_path = os.path.join(example_dir, main_file)
    if not os.path.exists(code_path):
        with open(code_path, "w", encoding="utf-8") as f:
            f.write("#!/usr/bin/env python3\n")
            f.write("# -*- coding: utf-8 -*-\n\n")
            f.write(f"'''\n{num}. {name}\n'''\n\n")
            
            # 根据项目类型生成不同的模板代码
            if name.lower().find("爬虫") >= 0:
                f.write("import requests\n")
                f.write("from bs4 import BeautifulSoup\n\n")
                f.write("def crawl_website(url):\n")
                f.write("    response = requests.get(url)\n")
                f.write("    soup = BeautifulSoup(response.text, 'html.parser')\n")
                f.write("    # 在这里提取数据\n")
                f.write("    return soup\n\n")
                f.write("def main():\n")
                f.write("    url = 'https://example.com'\n")
                f.write("    data = crawl_website(url)\n")
                f.write("    print('爬取完成!')\n\n")
            elif name.lower().find("api") >= 0:
                f.write("from flask import Flask, request, jsonify\n\n")
                f.write("app = Flask(__name__)\n\n")
                f.write("@app.route('/api/v1/hello', methods=['GET'])\n")
                f.write("def hello():\n")
                f.write("    return jsonify({'message': 'Hello, World!'})\n\n")
                f.write("def main():\n")
                f.write("    app.run(debug=True)\n\n")
            else:
                f.write("def main():\n")
                f.write("    print('Hello, Python in Practice!')\n")
                f.write("    # 在这里实现你的代码\n\n")
            
            f.write("if __name__ == '__main__':\n")
            f.write("    main()\n")
        print(f"创建文件: {code_path}")
    else:
        print(f"文件已存在: {code_path}")
    
    # 创建 requirements.txt 文件
    req_path = os.path.join(example_dir, "requirements.txt")
    if not os.path.exists(req_path):
        with open(req_path, "w", encoding="utf-8") as f:
            f.write("# 项目依赖\n")
            
            # 根据项目类型添加不同的依赖
            if name.lower().find("爬虫") >= 0:
                f.write("requests>=2.25.1\n")
                f.write("beautifulsoup4>=4.9.3\n")
            elif name.lower().find("数据分析") >= 0:
                f.write("pandas>=1.3.0\n")
                f.write("numpy>=1.20.0\n")
                f.write("matplotlib>=3.4.0\n")
            elif name.lower().find("api") >= 0:
                f.write("flask>=2.0.0\n")
                f.write("flask-restful>=0.3.9\n")
            
        print(f"创建文件: {req_path}")
    else:
        print(f"文件已存在: {req_path}")

def main():
    """主函数"""
    # 确保 examples 目录存在
    if not os.path.exists(EXAMPLES_DIR):
        os.makedirs(EXAMPLES_DIR)
        print(f"创建主目录: {EXAMPLES_DIR}")
    
    # 解析README.md获取示例项目列表
    examples = parse_readme()
    
    if not examples:
        print("未能从README.md中解析出示例项目，请检查文件格式。")
        return
    
    print(f"从README.md中解析出{len(examples)}个示例项目。")
    
    # 为每个示例创建目录结构
    for example in examples:
        print(f"\n处理示例: {example['num']}. {example['name']}")
        create_example_structure(example)
    
    print("\n目录结构生成完成！")

if __name__ == "__main__":
    main()