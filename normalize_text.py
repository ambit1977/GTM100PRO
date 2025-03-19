import os
import re

def process_file(file_path, pattern, replacement):
    """ファイルを読み込み、patternに一致する部分をreplacementに置換して上書き保存する。
    置換回数とともにコンソールに結果を表示する。"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 置換処理（置換後の文字列と置換回数を取得）
    new_content, count = re.subn(pattern, replacement, content)
    
    if count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path} - {count} 置換しました。")
    else:
        print(f"No changes: {file_path} - 置換は行われませんでした。")
    
    return count

# 対象フォルダのリスト
folders = ["1-20", "21-40", "41-60", "61-80", "81-100"]

# Unicode補助平面の文字（MySQLのutf8が扱えない4バイト文字）の除去用パターン
pattern = r'[\U00010000-\U0010ffff]'

# 該当文字を空文字に置換
replacement = ''

total_replacements = 0
total_files = 0

for folder in folders:
    if not os.path.isdir(folder):
        print(f"Folder not found: {folder}")
        continue

    for filename in os.listdir(folder):
        if filename.endswith(".md"):
            total_files += 1
            file_path = os.path.join(folder, filename)
            count = process_file(file_path, pattern, replacement)
            total_replacements += count

print("\n処理完了")
print(f"総ファイル数: {total_files}")
print(f"総置換数: {total_replacements}")
