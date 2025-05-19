import requests
from bs4 import BeautifulSoup

def fetch_seo_info(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取 SEO 信息
        title = soup.title.string.strip() if soup.title else '无标题'
        description = soup.find('meta', attrs={'name': 'description'})
        keywords = soup.find('meta', attrs={'name': 'keywords'})

        description_content = description['content'].strip() if description and 'content' in description.attrs else '无描述'
        keywords_content = keywords['content'].strip() if keywords and 'content' in keywords.attrs else '无关键词'

        # 提取正文内容（简单处理）
        paragraphs = soup.find_all('p')
        text_content = '\n'.join(p.get_text().strip() for p in paragraphs if p.get_text().strip())

        return {
            'URL': url,
            'Title': title,
            'Description': description_content,
            'Keywords': keywords_content,
            'TextContent': text_content[:500]  # 限制预览字符数
        }
    except Exception as e:
        return {'error': str(e)}

# 示例使用
if __name__ == "__main__":
    test_url = 'https://www.example.com'
    result = fetch_seo_info(test_url)
    
    for key, value in result.items():
        print(f"{key}:\n{value}\n{'-' * 50}")
