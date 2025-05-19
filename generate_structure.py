#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# 示例项目列表
EXAMPLES = [
    "01. SEO简易爬虫",
    "02. 自动化办公",
    "03. 批量图片处理",
    "04. 数据分析与可视化",
    "05. 自动发送邮件或短信通知",
    "06. 定时任务与脚本调度",
    "07. 股票/基金/比特币数据监控",
    "08. 网站/接口性能监测与报警",
    "09. 微信/钉钉机器人消息推送",
    "10. API接口开发",
    "11. 数据库批量管理",
    "12. 自动填表、自动化表单录入",
    "13. 简易桌面应用开发",
    "14. PDF文本提取与合并分割",
    "15. 音频识别转文字",
    "16. OCR图片识别",
    "17. 视频剪辑自动化",
    "18. 批量重命名和整理文件夹",
    "19. 快速制作简易小游戏",
    "20. 命令行工具开发",
    "21. Word/Excel报表生成自动化",
    "22. 本地记账与财务管理脚本",
    "23. AI写作助手",
    "24. 聊天机器人开发",
    "25. 爬虫+数据分析电商选品辅助工具",
    "26. 智能家居脚本控制",
    "27. 批量网络测速与结果分析",
    "28. 自动化注册/登录/数据采集测试脚本",
    "29. 监控本地目录变化",
    "30. 自制词库/背单词工具/学习辅助程序"
]

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLES_DIR = os.path.join(ROOT_DIR, "examples")

def create_example_structure(example_num, example_name):
    """创建示例项目的目录结构"""
    # 提取编号
    num = example_num.split(".")[0].strip()
    
    # 创建示例目录
    example_dir = os.path.join(EXAMPLES_DIR, num)
    if not os.path.exists(example_dir):
        os.makedirs(example_dir)
        print(f"创建目录: {example_dir}")
    else:
        print(f"目录已存在: {example_dir}")
    
    # 创建 README.md 文件
    readme_path = os.path.join(example_dir, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {example_name}\n\n")
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
    code_path = os.path.join(example_dir, "main.py")
    if not os.path.exists(code_path):
        with open(code_path, "w", encoding="utf-8") as f:
            f.write("#!/usr/bin/env python3\n")
            f.write("# -*- coding: utf-8 -*-\n\n")
            f.write(f"'''\n{example_name}\n'''\n\n")
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
        print(f"创建文件: {req_path}")
    else:
        print(f"文件已存在: {req_path}")

def main():
    """主函数"""
    # 确保 examples 目录存在
    if not os.path.exists(EXAMPLES_DIR):
        os.makedirs(EXAMPLES_DIR)
        print(f"创建主目录: {EXAMPLES_DIR}")
    
    # 为每个示例创建目录结构
    for example in EXAMPLES:
        parts = example.split(".", 1)
        if len(parts) == 2:
            example_num = parts[0].strip()
            example_name = parts[1].strip()
            create_example_structure(example_num, example_name)
    
    print("\n目录结构生成完成！")

if __name__ == "__main__":
    main()