# 📄 需求文档：SEO 信息抓取爬虫（Python 实现）

## 一、项目背景

为了快速分析任意网页的基础 SEO 信息与主要内容，需开发一款轻量级的 Python 工具，自动抓取网页中的标题、描述、关键词等基础 SEO 数据，以及页面正文的部分文本内容，用于 SEO 诊断、数据采集或内容分析目的。

---

## 二、项目目标

开发一个命令行运行的 Python 脚本，功能如下：

1. 输入一个网页 URL
2. 自动获取该网页的：

   * `<title>` 页面标题
   * `<meta name="description">` 描述
   * `<meta name="keywords">` 关键词
   * 网页正文中 `<p>` 标签下的文本内容（最多预览 500 字）
3. 控制台打印上述信息
4. 可处理网页异常或字段缺失

---

## 三、功能需求

### 3.1 输入参数

| 参数名   | 类型  | 是否必需 | 说明            |
| ----- | --- | ---- | ------------- |
| `url` | str | 是    | 要抓取的网页 URL 地址 |

### 3.2 输出数据（结构化）

```json
{
  "URL": "https://www.example.com",
  "Title": "Example Domain",
  "Description": "This is an example site...",
  "Keywords": "sample, example, domain",
  "TextContent": "This domain is for use in illustrative examples in documents..."
}
```

### 3.3 控制台输出格式

格式化输出每一项字段，并添加分隔符（`--------------------------------------------------`）

---

## 四、技术方案

### 4.1 技术栈

| 技术/库            | 用途      |
| --------------- | ------- |
| Python 3        | 编程语言    |
| `requests`      | 网页请求    |
| `BeautifulSoup` | HTML 解析 |

### 4.2 请求策略

* 设置常见 User-Agent 避免 403 拒绝访问
* 超时时间设置为 10 秒
* 报错捕获使用 `try-except`

---

## 五、异常处理

| 场景                             | 处理方式                                                    |
| ------------------------------ | ------------------------------------------------------- |
| 网络连接失败                         | 返回 `{'error': '请求失败信息'}`                                |
| 页面无 title、description、keywords | 显示为 `No title found` / `No description` / `No keywords` |
| 字段解析失败                         | 跳过该字段，继续抓取其余信息                                          |

---

## 六、非功能性需求

* 脚本文件名建议为 `seo_scraper.py`
* 代码需易于扩展，可后期加入：

  * H1-H6 提取
  * 图片 alt 抓取
  * 内部链接提取
  * 批量 URL 读取功能

---

## 七、运行示例

```bash
$ python seo_scraper.py
URL:
https://www.example.com
--------------------------------------------------
Title:
Example Domain
--------------------------------------------------
Description:
No description
--------------------------------------------------
Keywords:
No keywords
--------------------------------------------------
TextContent:
This domain is for use in illustrative examples in documents...
--------------------------------------------------
```

