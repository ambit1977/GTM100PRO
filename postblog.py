import os
import re
import glob
import requests
import markdown  # pip install markdown
from datetime import datetime, timedelta

# 定数設定
LOGIN_URL = "https://blogsmt.itmedia.co.jp/mt.cgi"
NEW_ENTRY_URL = "https://blogsmt.itmedia.co.jp/mt.cgi?__mode=view&_type=entry&blog_id=216"
POST_URL = "https://blogsmt.itmedia.co.jp/mt.cgi"

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}

# ログインしてセッションを返す
def login_mt(session):
    payload = {
        "username": "ambit",
        "password": "miwa0407",
        "remember": "1"
    }
    response = session.post(LOGIN_URL, data=payload, headers=HEADERS, allow_redirects=False)
    if response.status_code not in (200, 302):
        raise Exception(f"ログイン失敗: ステータスコード {response.status_code}")
    return session

# 新規投稿フォームをGETして最新の magic_token を抽出
def fetch_magic_token(session):
    response = session.get(NEW_ENTRY_URL, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"新規投稿フォーム取得失敗: ステータスコード {response.status_code}")
    html = response.text
    match = re.search(r'<input[^>]*name="magic_token"[^>]*value="([^"]+)"', html, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        raise Exception("magic_token が見つかりませんでした")

# Markdown原稿をパースする（最初の2個の区切りで分割）
def parse_article(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    parts = content.split('---', 2)
    if len(parts) < 3:
        raise Exception("ファイルのフォーマットが想定と異なります")
    # タイトル部：最初のセクションの2行目以降を1行に結合
    title_lines = parts[0].strip().splitlines()
    if len(title_lines) < 2:
        raise Exception("タイトル部が不十分です")
    title = " ".join(line.strip() for line in title_lines[1:] if line.strip())
    # 概要部：2番目のセクションの2行目を利用
    excerpt_lines = parts[1].strip().splitlines()
    if len(excerpt_lines) < 2:
        raise Exception("概要部が不十分です")
    excerpt = excerpt_lines[1].strip()
    # 本文部：3番目のセクション全体を本文とする。もし先頭に "##" があれば除去
    body = parts[2].strip()
    if body.startswith("##"):
        body = "\n".join(body.splitlines()[1:]).strip()
    return title, excerpt, body

# タイトルから "Day 〇〇" の数字を抽出
def extract_day_number(title):
    match = re.search(r'Day\s*(\d+)', title, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return "XX"

# 各記事を予約投稿する
def post_article(session, title, excerpt, body, magic_token, publish_date):
    # Markdown → HTML変換（本文をHTML化）
    body_html = markdown.markdown(body)
    # 公開日時を publish_date（datetime オブジェクト）の形式にする
    auth_date = publish_date.strftime("%Y-%m-%d")
    auth_time = publish_date.strftime("%H:%M:%S")
    payload_dict = {
        "author_id": "220",
        "blog_id": "216",
        "__mode": "save_entry",
        "_type": "entry",
        "return_args": "__mode=view&_type=entry&blog_id=216",
        "magic_token": magic_token,
        "action_name": "",
        "itemset_action_input": "",
        "dirty": "1",
        "old_status": "",
        "mobile_view": "",
        "save_revision": "1",
        "entry_prefs": "Custom",
        "custom_prefs": ["excerpt", "keywords", "tags", "category", "feedback", "assets"],
        "title": title,
        "convert_breaks": "richtext",
        "text": body_html,
        "text_more": "",
        "convert_breaks_for_mobile": "_richtext",
        "excerpt": excerpt,
        # 固定のキーワードとタグ
        "keywords": "GTM,100日後,GoogleTagManager,タグマネとは,GTMとは,デジマ,アドテク,マーテック",
        "tags": "GTM,100日後,GoogleTagManager,タグマネとは,GTMとは,デジマ,アドテク,マーテック",
        "_ignore_tags": "GTM,100日後,GoogleTagManager,タグマネとは,GTMとは,デジマ,アドテク,マーテック",
        "customfield_beacon": "1",
        # ステータス「日時指定」は通常 4
        "status": "4",
        "authored_on_date": auth_date,
        "authored_on_year": auth_date.split("-")[0],
        "authored_on_month": auth_date.split("-")[1],
        "authored_on_day": auth_date.split("-")[2],
        "authored_on_time": auth_time,
        "authored_on_hour": auth_time.split(":")[0],
        "authored_on_minute": auth_time.split(":")[1],
        "authored_on_second": auth_time.split(":")[2],
        "unpublished_on_date": "",
        "unpublished_on_year": "",
        "unpublished_on_month": "",
        "unpublished_on_day": "",
        "unpublished_on_time": "",
        "unpublished_on_hour": "",
        "unpublished_on_minute": "",
        "unpublished_on_second": "",
        # 出力ファイル名：タイトル中のDay番号から抽出
        "basename": f"GTM100DAY_DAY{extract_day_number(title)}",
        "basename_manual": "1",
        "revision-note": "",
        "add_category_id_5246": "on",
        "add_category_id_5245": "on",
        "category_ids": "5246,5245",
        "allow_comments": "1",
        "allow_pings": "1",
        "to_ping_urls": "",
        "include_asset_ids": ""
    }
    payload = []
    for key, value in payload_dict.items():
        if isinstance(value, list):
            for item in value:
                payload.append((key, item))
        else:
            payload.append((key, value))
    headers = HEADERS.copy()
    headers.update({
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": NEW_ENTRY_URL
    })
    response = session.post(POST_URL, data=payload, headers=headers)
    return response

def main():
    # 予約投稿の対象フォルダ（相対パス）
    folders = ["1-20", "21-40", "41-60", "61-80", "81-100"]
    # 各フォルダ内の *.md ファイルを再帰的に取得
    md_files = []
    for folder in folders:
        md_files.extend(glob.glob(os.path.join(folder, "*.md")))
    # ファイル名からDay番号を抽出してソート（例："Day_1.md" → 1）
    def get_day(filepath):
        filename = os.path.basename(filepath)
        m = re.search(r'Day[_\s]?(\d+)', filename, re.IGNORECASE)
        return int(m.group(1)) if m else 9999
    md_files = sorted(md_files, key=get_day)
    total = len(md_files)
    print(f"投稿対象ファイル数: {total}")
    
    # 予約開始日：2025-03-19 05:00:00
    base_date = datetime(2025, 3, 19, 5, 0, 0)
    
    session = requests.Session()
    session.headers.update(HEADERS)
    login_mt(session)
    
    # 1件ずつ投稿
    for i, filepath in enumerate(md_files):
        try:
            title, excerpt, body = parse_article(filepath)
            # 予約公開日時は base_date に i 日分足す
            publish_date = base_date + timedelta(days=i)
            # 毎回新規投稿フォームから最新の magic_token を取得
            magic_token = fetch_magic_token(session)
            print(f"[{filepath}] 投稿開始（公開予定日時: {publish_date.strftime('%Y-%m-%d %H:%M:%S')}）")
            response = post_article(session, title, excerpt, body, magic_token, publish_date)
            print(f"  {title} => レスポンスコード: {response.status_code}")
            if response.status_code != 200:
                print(f"  投稿失敗: {response.text}")
        except Exception as e:
            print(f"  ファイル {filepath} の投稿でエラー: {e}")

if __name__ == "__main__":
    main()
