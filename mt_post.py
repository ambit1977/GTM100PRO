import requests
import re
import urllib.parse

# ユーザーエージェントなどヘッダの設定
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " \
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}

LOGIN_URL = "https://blogsmt.itmedia.co.jp/mt.cgi"
NEW_ENTRY_URL = "https://blogsmt.itmedia.co.jp/mt.cgi?__mode=view&_type=entry&blog_id=216"
POST_URL = "https://blogsmt.itmedia.co.jp/mt.cgi"

def login_mt(session):
    login_payload = {
        "username": "ambit",
        "password": "miwa0407",
        "remember": "1"
    }
    # POST でログイン
    response = session.post(LOGIN_URL, data=login_payload, headers=HEADERS, allow_redirects=False)
    if response.status_code not in (200, 302):
        raise Exception("ログイン失敗: ステータスコード {}".format(response.status_code))
    return response

def fetch_new_entry_form(session):
    response = session.get(NEW_ENTRY_URL, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("新規投稿フォーム取得失敗: ステータスコード {}".format(response.status_code))
    return response.text

def parse_magic_token(html):
    # magic_token の抽出 (例: <input type="hidden" name="magic_token" value="XXXXXXXX" id="m_t" />)
    match = re.search(r'<input[^>]*name="magic_token"[^>]*value="([^"]+)"', html, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        raise Exception("magic_token が見つかりませんでした")

def post_draft_article(session, magic_token):
    # cURLサンプルに基づくペイロードを作成（URLエンコード済み文字列として作成）
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
        "title": "テストタイトル",
        "convert_breaks": "richtext",
        "text": "<p>テスト本文</p>",
        "text_more": "",
        "convert_breaks_for_mobile": "_richtext",
        "excerpt": "テスト概要",
        "keywords": "テストキーワードワード",
        "tags": "テストタグ",
        "_ignore_tags": "テストタグ",
        "customfield_beacon": "1",
        "status": "1",
        "authored_on_date": "2025-12-31",
        "authored_on_year": "2025",
        "authored_on_month": "03",
        "authored_on_day": "14",
        "authored_on_time": "23:59:59",
        "authored_on_hour": "18",
        "authored_on_minute": "16",
        "authored_on_second": "39",
        "unpublished_on_date": "",
        "unpublished_on_year": "",
        "unpublished_on_month": "",
        "unpublished_on_day": "",
        "unpublished_on_time": "",
        "unpublished_on_hour": "",
        "unpublished_on_minute": "",
        "unpublished_on_second": "",
        "basename": "TESTFILENAME",
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
    # custom_prefs は同一キーで複数送る必要があるため、URLエンコード用にリスト対応
    # requests は同一キーをリストで送信可能です
    payload = []
    for key, value in payload_dict.items():
        if isinstance(value, list):
            for item in value:
                payload.append( (key, item) )
        else:
            payload.append( (key, value) )
    
    # 送信時のヘッダーに Referer を追加
    headers = HEADERS.copy()
    headers.update({
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": NEW_ENTRY_URL
    })
    
    response = session.post(POST_URL, data=payload, headers=headers)
    return response

def main():
    # セッションオブジェクトを作成（cookieの保持・自動管理）
    session = requests.Session()
    session.headers.update(HEADERS)
    
    # ① ログイン
    login_mt(session)
    
    # ② 新規投稿フォームを取得して最新の hidden パラメータを抽出
    html = fetch_new_entry_form(session)
    magic_token = parse_magic_token(html)
    print("取得した magic_token:", magic_token)
    
    # ③ 下書き記事として投稿
    response = post_draft_article(session, magic_token)
    print("投稿レスポンスコード:", response.status_code)
    print("投稿レスポンス本文:\n", response.text)

if __name__ == '__main__':
    main()
