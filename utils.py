import pandas as pd
import os

def load_data_from_directories(articles_dir, summaries_dir):
    data = []

    # Load articles
    for category in os.listdir(articles_dir):
        category_path = os.path.join(articles_dir, category)
        if os.path.isdir(category_path):
            for filename in os.listdir(category_path):
                if filename.endswith('.txt'):
                    file_path = os.path.join(category_path, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                            content = f.read().strip()
                        data.append({
                            'content': content,
                            'type': 'article',
                            'filename': filename,
                            'category': category
                        })
                    except Exception as e:
                        print(f"Error reading article {file_path}: {e}")

    # Load summaries
    for category in os.listdir(summaries_dir):
        category_path = os.path.join(summaries_dir, category)
        if os.path.isdir(category_path):
            for filename in os.listdir(category_path):
                if filename.endswith('.txt'):
                    file_path = os.path.join(category_path, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                            content = f.read().strip()
                        data.append({
                            'content': content,
                            'type': 'summary',
                            'filename': filename,
                            'category': category
                        })
                    except Exception as e:
                        print(f"Error reading summary {file_path}: {e}")

    return pd.DataFrame(data)