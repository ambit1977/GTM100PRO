**タイトル:**  
未経験から100日後にGTMのプロになる話【Day 20】  
変数を使った柔軟なタグ設定 〜計測の自由度を最大化する〜

---

**概要（リード文）:**  
「タグの発火条件をもっと細かく制御したい！」  
「同じタグを複数の用途で使い回したい！」  
GTMの「変数」を活用すれば、タグの設定をより柔軟に管理できます。本日は、**変数を使った高度なタグ設定のテクニック**を解説します！

---

## **本文**

### ■ GTMの「変数」とは？

GTMの変数は、タグ・トリガー・設定値を動的に制御するための要素です。

例えば、
✅ **「特定のページで異なるGA4の測定IDを使いたい」**  
✅ **「クリックされたボタンのテキストを取得し、イベントデータに含めたい」**  
✅ **「Cookieの値に応じてタグの発火を切り替えたい」**  

こういったケースでは、GTMの「組み込み変数」や「ユーザー定義変数」を活用することで、計測の自由度を大幅に高められます。

では、実際に設定方法を学んでいきましょう！

---

### **① GTMの組み込み変数を活用する**

GTMにはデフォルトで用意されている「組み込み変数」があります。

#### **1. 組み込み変数を有効化する**

1. GTMの「**変数**」メニューを開く。
2. 「**組み込み変数を設定**」をクリック。
3. 必要な変数（例：`Click Text`、`Click URL`、`Page URL` など）にチェックを入れる。
4. 保存。

✅ **これで、ページのURLやクリックしたボタンのテキストなどを簡単に取得できます！**

#### **2. GA4のイベントタグで変数を活用する**

例えば、「クリックイベントでボタンのテキストを取得し、GA4に送信する」場合は、

1. GTMの「**タグ**」メニューを開く。
2. 「**新規**」をクリックし、タグの種類を「**Google アナリティクス: GA4 イベント**」に設定。
3. 「**イベント名**」を `button_click` にする。
4. 「イベントパラメータを追加」ボタンをクリックし、
   - **パラメータ名:** `button_text`（値: `{{Click Text}}`）
   - **パラメータ名:** `button_url`（値: `{{Click URL}}`）
5. 保存。

✅ **これで、クリックされたボタンのテキストとURLがGA4に送信されます！**

---

### **② ユーザー定義変数を活用する（JavaScript変数）**

GTMの「ユーザー定義変数」を使うと、サイト内の情報をより柔軟に取得できます。

例えば、「ユーザーのログイン状態」を取得するには、JavaScript変数を作成します。

#### **1. JavaScript変数を作成する**

1. GTMの「**変数**」メニューを開く。
2. 「**新規**」をクリックし、変数の種類を「**JavaScript変数**」に設定。
3. 「変数名」に `window.userStatus` を入力。
4. 変数名を「JS - ユーザーステータス」として保存。

✅ **これで、`window.userStatus` に格納された値をGTM内で取得できるようになります！**

#### **2. ユーザーのログイン状態に応じたタグの発火制御**

「ログインしているユーザーだけにタグを発火させたい」場合、

1. GTMの「**トリガー**」メニューを開く。
2. 「**新規**」をクリックし、トリガーの種類を「**ページビュー**」に設定。
3. 「このトリガーの発火を…」のオプションを「**一部のページビュー**」に変更。
4. 条件として「**JS - ユーザーステータス** が `logged_in` と等しい」を設定。
5. 保存。

✅ **これで、ログインユーザーだけにタグを発火させる設定ができます！**

---

### **③ Cookie変数を活用する（ファーストパーティCookieの利用）**

Cookie変数を使うと、ユーザーの過去の行動を考慮してタグを発火できます。

#### **1. Cookie変数を作成する**

1. GTMの「**変数**」メニューを開く。
2. 「**新規**」をクリックし、変数の種類を「**ファーストパーティ Cookie**」に設定。
3. 「Cookie 名」に `user_segment` を入力。
4. 変数名を「Cookie - ユーザーセグメント」として保存。

#### **2. ユーザーのセグメントに応じてタグを発火させる**

例えば、「VIPユーザーのみに広告タグを発火させる」場合、

1. GTMの「**トリガー**」メニューを開く。
2. 「**新規**」をクリックし、トリガーの種類を「**ページビュー**」に設定。
3. 「このトリガーの発火を…」のオプションを「**一部のページビュー**」に変更。
4. 条件として「**Cookie - ユーザーセグメント** が `vip` と等しい」を設定。
5. 保存。

✅ **これで、「VIPユーザーだけに広告タグを発火」できるようになります！**

---

### **■ まとめ 〜変数を使ってタグ設定を自在に操ろう！〜**

今回の学びを整理すると…

✅ **組み込み変数を有効化すると、GTMが提供する便利なデータを取得できる！**  
✅ **JavaScript変数を活用すれば、ログイン状態などの動的なデータを取得できる！**  
✅ **Cookie変数を使えば、ユーザーの過去の行動に基づいてタグの発火を制御できる！**  
✅ **GTMの「プレビューモード」でテストし、問題なければ公開する！**  

これを活用すれば、
- **「特定のボタンのクリック時に詳細なデータを取得」**
- **「ユーザーの属性（ログイン状態・セグメント）に応じてタグを発火」**
- **「Cookieを利用してリマーケティング広告の対象を制御」**

といった計測が可能になります！

---

### **■ 明日の予告 〜Google広告コンバージョンタグの設定〜**

次回は、**「Google広告のコンバージョンタグ」** を設定し、

- **「広告経由のコンバージョンを計測」**
- **「GTMを使って動的にコンバージョン値を設定」**

といった方法を解説します。

明日も引き続き、GTMの実践スキルを磨いていきましょう！

