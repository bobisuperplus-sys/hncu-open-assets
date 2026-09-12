#!/usr/bin/env python3
"""
Python 校园知识库轻量检索示例 (Campus FAQ Search Demo)
无需复杂向量库依赖，标准 Python 即可检索校园规章与高频生活指南
"""
import os
import json


def load_faq_dataset():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "../../datasets/faq/campus_faq.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("items", [])


def search_faq(keyword: str, max_results: int = 3):
    items = load_faq_dataset()
    results = []
    keyword_lower = keyword.lower()
    for item in items:
        q = item.get("question", "")
        a = item.get("answer", "")
        if keyword_lower in q.lower() or keyword_lower in a.lower():
            results.append(item)
            if len(results) >= max_results:
                break
    return results


def main():
    print("=" * 60)
    print(" 🏛️ 湖南城市学院开放数据集 - 校园知识检索示例")
    print("=" * 60)

    test_queries = ["饭卡掉了", "四人寝", "旷课", "转专业", "作息时间"]

    for query in test_queries:
        print(f"\n🔍 检索关键词: 【{query}】")
        matches = search_faq(query)
        if matches:
            for idx, m in enumerate(matches, 1):
                print(f"  [{idx}] Q: {m['question']}")
                print(f"      A: {m['answer']}")
        else:
            print("  暂未匹配到相关条目")


if __name__ == "__main__":
    main()
