# 自动生成文件结构脚本

## 项目介绍

这是一个Python实用工具，用于自动化生成项目目录结构。该脚本可以根据README.md文件中的内容，自动创建相应的目录和文件，大大提高项目初始化的效率。

## 功能特点

- 自动解析README.md文件中的项目列表
- 智能创建项目目录结构
- 根据项目类型生成不同的代码模板
- 自动添加相应的依赖库
- 跳过已存在的文件，安全可重复运行
- 支持批量处理多个项目

## 使用方法

1. 将脚本放置在项目根目录下
2. 确保README.md文件中包含正确格式的项目列表
3. 运行脚本：

```bash
python3 generate_structure.py
```

脚本会自动解析README.md文件，并为每个项目创建相应的目录结构。

## 代码示例

```python
# 解析README.md获取示例项目列表
examples = parse_readme()

# 为每个示例创建目录结构
for example in examples:
    print(f"\n处理示例: {example['num']}. {example['name']}")
    create_example_structure(example)
```

## 目录结构生成规则

脚本会为每个项目创建以下文件：

1. `README.md` - 项目说明文档
2. `main.py`/`app.py` - 主代码文件（根据项目类型自动选择）
3. `requirements.txt` - 项目依赖文件

## 智能模板

脚本会根据项目名称中的关键词自动选择不同的代码模板：

- 爬虫项目：自动添加requests和BeautifulSoup相关代码
- API项目：自动添加Flask相关代码
- 数据分析项目：自动添加pandas和matplotlib相关依赖

## 依赖库

- Python 3.6+
- 无需额外依赖库，使用Python标准库即可运行

## 注意事项

- README.md文件中的项目列表格式必须符合规范
- 脚本不会覆盖已存在的文件，可以安全地多次运行
- 可以根据需要修改脚本中的模板内容
