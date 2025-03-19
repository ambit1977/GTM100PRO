import os
import re
import requests
import markdown  # pip install markdown

# 定数設定
LOGIN_URL = "https://blogsmt.itmedia.co.jp/mt.cgi"
NEW_ENTRY_URL = "https://blogsmt.itmedia.co.jp/mt.cgi?__mode=view&_type=entry&blog_id=216"
POST_URL = "https://blogsmt.itmedia.co.jp/mt.cgi"

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}

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

def parse_article(file_path):
    """
    Markdownファイルの例：
    
    **タイトル:**  
    未経験から100日後にGTMのプロになる話【Day 1】  
    エンジニアにもマーケターにも有効な「GTMとは何か？」
    
    ---
    
    **概要（リード文）:**  
    「100日後にGTMのプロになる」…（概要）
    
    ---
    
    ## 本文
    
    (本文)
    """
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    # 最初の2個の区切りのみで分割し、本文は残り全体
    parts = content.split('---', 2)
    if len(parts) < 3:
        raise Exception("ファイルのフォーマットが想定と異なります")
    
    # タイトル部：最初のセクションの2行目以降を1行に結合
    title_lines = parts[0].strip().splitlines()
    if len(title_lines) < 2:
        raise Exception("タイトル部が不十分です")
    title = " ".join(line.strip() for line in title_lines[1:] if line.strip())
    
    # 概要部：2 番目のセクションの2行目を利用
    excerpt_lines = parts[1].strip().splitlines()
    if len(excerpt_lines) < 2:
        raise Exception("概要部が不十分です")
    excerpt = excerpt_lines[1].strip()
    
    # 本文部：3 番目のセクション全体を本文とする。もし先頭に "##" があれば除去
    body = parts[2].strip()
    if body.startswith("##"):
        body = "\n".join(body.splitlines()[1:]).strip()
    return title, excerpt, body

def extract_day_number(title):
    # タイトルから "Day 〇〇" の数字を抽出（大文字小文字無視）
    match = re.search(r'Day\s*(\d+)', title, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return "XX"

def post_test_article(session, title, excerpt, body, magic_token):
    # Markdown → HTML 変換（本文はHTMLへ変換）
    body_html = markdown.markdown(body)
    # 公開日時：2025-03-19 05:00:00
    auth_date = "2025-03-19"
    auth_time = "05:00:00"
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
        # 固定のキーワードとタグ（カンマ区切り）
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
        # 出力ファイル名: GTM100DAY_DAY{数字}（タイトル中のDay番号から抽出）
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
    # 相対パスで投稿するテスト原稿ファイルのパス
    file_path = "1-20/Day_1.md"
    title, excerpt, body = parse_article(file_path)
    print("抽出したタイトル:", title)
    print("抽出した概要:", excerpt)
    session = requests.Session()
    session.headers.update(HEADERS)
    login_mt(session)
    magic_token = fetch_magic_token(session)
    print("取得した magic_token:", magic_token)
    response = post_test_article(session, title, excerpt, body, magic_token)
    print("投稿レスポンスコード:", response.status_code)
    print("投稿レスポンス本文:\n", response.text)

if __name__ == "__main__":
    main()
