import glob
import os
import re
import subprocess

DEBUG = True  # Trueなら処理経過を出力

def normalize_header(content, filepath=""):
    """
    64日目以降の記事ヘッダーを統一する。
    
    ① すでに太字形式（**タイトル:**）でタイトルとサブタイトルが分かれている場合
       → タイトル見出し行の末尾に '\' がなければ追加する。
    
    ② 先頭行が「タイトル:」の場合は、1〜63日目形式に変換し、
       タイトル見出し行にも '\' を付与する。
       
    変換後のヘッダーは以下の形式となります。
    
    **タイトル:**\
    未経験から100日後にGTMのプロになる話【Day XX】\
    <サブタイトル>
    """
    lines = content.splitlines()
    if DEBUG:
        print(f"\n--- Processing file: {filepath} ---")
        for i, line in enumerate(lines):
            print(f"{i:02d}: {line}")
    
    # ファイル先頭の空行はそのまま残す
    first_nonempty_idx = None
    for i, line in enumerate(lines):
        if line.strip():
            first_nonempty_idx = i
            break
    if first_nonempty_idx is None:
        return content  # 空ファイルならそのまま返す

    first_line = lines[first_nonempty_idx].strip()

    # ケース①: すでに太字形式になっている場合
    if first_line.startswith("**タイトル:**"):
        # 2行目（シリーズタイトル）と3行目（サブタイトル）があるか確認
        if len(lines) >= first_nonempty_idx + 3:
            title_header = lines[first_nonempty_idx].rstrip()
            # タイトル見出し行の末尾に '\' がなければ追加
            if not title_header.endswith("\\"):
                title_header += "\\"
                if DEBUG:
                    print("タイトル見出し行にバックスラッシュを追加しました。")
            series_title = lines[first_nonempty_idx+1].rstrip()
            # 既にシリーズタイトルの末尾にも '\' が無ければ追加
            if not series_title.endswith("\\"):
                series_title += "\\"
                if DEBUG:
                    print("シリーズタイトル行にバックスラッシュを追加しました。")
            subtitle = lines[first_nonempty_idx+2].strip()
            new_header = [title_header, series_title, subtitle]
            new_lines = lines[:first_nonempty_idx] + new_header + lines[first_nonempty_idx+3:]
            new_content = "\n".join(new_lines)
            if DEBUG:
                print("変換後のファイル内容:")
                print(new_content)
            return new_content
        else:
            if DEBUG:
                print("太字形式ですが、行数が不足しているため変換不要。")
            return content

    # ケース②: 先頭行が「タイトル:」で始まる場合
    m = re.match(r"^タイトル:\s*(.+)$", first_line)
    if not m:
        if DEBUG:
            print("先頭行が『タイトル:』で始まっていません。変換スキップ:", filepath)
        return content

    header_rest = m.group(1).strip()
    # 「【Day」で区切り、シリーズタイトルとサブタイトルを抽出する
    m2 = re.search(r"(未経験から100日後にGTMのプロになる話【Day\s*\d+】)(.*)", header_rest)
    if m2:
        series_title = m2.group(1).strip()
        subtitle = m2.group(2).strip()
    else:
        # 分割できなければ、先頭行の内容をシリーズタイトル、次の非空行をサブタイトルとする
        series_title = header_rest
        subtitle = ""
        for j in range(first_nonempty_idx + 1, len(lines)):
            if lines[j].strip():
                subtitle = lines[j].strip()
                break

    # タイトル見出し行を太字形式かつ末尾に '\' を追加
    new_title_header = "**タイトル:**\\"
    # シリーズタイトルの末尾にも '\' を付与（既に無ければ追加）
    if not series_title.endswith("\\"):
        series_title += "\\"
    if DEBUG:
        print(f"Normalized header: series_title='{series_title}', subtitle='{subtitle}'")
    
    new_header = [new_title_header, series_title, subtitle]
    new_lines = lines[:first_nonempty_idx] + new_header + lines[first_nonempty_idx+1:]
    new_content = "\n".join(new_lines)
    if DEBUG:
        print("変換後のファイル内容:")
        print(new_content)
    return new_content

def update_files():
    """
    各グループの中で、日付が64以上のファイルについてヘッダーを正規化する。
    変更されたファイルの一覧を返す。
    """
    modified_files = []
    groups = [
        ("基礎編", "1-20", range(1, 21)),
        ("応用編 前半", "21-40", range(21, 41)),
        ("応用編 後半", "41-60", range(41, 61)),
        ("高度な活用編", "61-80", range(61, 81)),
        ("実践編・総仕上げ", "81-100", range(81, 101)),
    ]
    for group_name, folder, day_range in groups:
        pattern = os.path.join(folder, "Day_*.md")
        for filepath in glob.glob(pattern):
            basename = os.path.basename(filepath)
            m = re.search(r"Day_(\d+)\.md", basename)
            if not m:
                continue
            day = int(m.group(1))
            if day < 64:
                continue  # 1〜63日目は変更対象外
            if DEBUG:
                print(f"\n【対象ファイル】 {filepath} (Day {day})")
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = normalize_header(content, filepath)
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                modified_files.append(filepath)
                if DEBUG:
                    print(f"{filepath} を更新しました。")
            else:
                if DEBUG:
                    print(f"{filepath} は変換不要です。")
    return modified_files

def git_commit_and_push(modified_files):
    """
    変更されたファイルをGitにステージング、コミット、プッシュする。
    """
    if not modified_files:
        print("更新するファイルはありませんでした。")
        return
    # ステージング
    cmd_add = ["git", "add"] + modified_files
    subprocess.run(cmd_add)
    commit_message = "Normalize header for Day 64+ files: add explicit newline after title heading"
    subprocess.run(["git", "commit", "-m", commit_message])
    push_result = subprocess.run(["git", "push"], capture_output=True, text=True)
    if push_result.returncode == 0:
        print("変更をGitにコミット＆プッシュしました。")
    else:
        print("Gitプッシュに失敗しました:")
        print(push_result.stdout)
        print(push_result.stderr)

if __name__ == "__main__":
    modified_files = update_files()
    if modified_files:
        print("\n【更新されたファイル一覧】")
        for f in modified_files:
            print(f" - {f}")
    else:
        print("更新するファイルはありませんでした。")
    # 必要に応じて以下の行のコメントを解除して自動コミット＆プッシュ
    git_commit_and_push(modified_files)
