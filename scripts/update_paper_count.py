#!/usr/bin/env python3
"""
自动统计论文数量并更新 README 中的徽章计数
"""

import re
from pathlib import Path


def count_papers(readme_path: Path) -> int:
    """统计 README 文件中的论文数量（通过 rowspan="2" 模式）"""
    content = readme_path.read_text(encoding='utf-8')
    
    # 先移除 HTML 注释内容，避免统计被注释掉的论文
    content_without_comments = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # 每篇论文在表格中使用 rowspan="2" 来合并日期单元格
    pattern = r'rowspan="2"'
    matches = re.findall(pattern, content_without_comments)
    return len(matches)


def update_badge_count(readme_path: Path, paper_count: int) -> bool:
    """更新 README 文件中的论文数量徽章"""
    content = readme_path.read_text(encoding='utf-8')
    
    # 匹配 Papers-N-blue 格式的徽章
    pattern = r'(Papers-)\d+(-blue\.svg)'
    replacement = rf'\g<1>{paper_count}\g<2>'
    
    new_content, count = re.subn(pattern, replacement, content)
    
    if count > 0:
        readme_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def main():
    # 获取项目根目录
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    readme_files = [
        project_root / 'README.md',
        project_root / 'README_cn.md',
    ]
    
    print("📊 正在统计论文数量...")
    print("-" * 40)
    
    for readme_path in readme_files:
        if not readme_path.exists():
            print(f"⚠️  未找到文件: {readme_path.name}")
            continue
            
        paper_count = count_papers(readme_path)
        print(f"📄 {readme_path.name}: {paper_count} 篇论文")
        
        if update_badge_count(readme_path, paper_count):
            print(f"   ✅ 已更新徽章计数为 {paper_count}")
        else:
            print(f"   ⚠️  未找到徽章或无需更新")
    
    print("-" * 40)
    print("✨ 完成!")


if __name__ == '__main__':
    main()
