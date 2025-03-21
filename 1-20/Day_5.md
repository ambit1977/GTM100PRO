**タイトル:**  
未経験から100日後にGTMのプロになる話【Day 5】  
最初のタグを作成！GA4ページビュー計測を始めよう

---

**概要（リード文）:**  
GTMの管理画面に慣れ、「タグ・トリガー・変数」の関係も理解したら、いよいよ実践です。今回は、Google Analytics 4（GA4）のページビュー計測タグをGTMで作成し、データが正しく取得できるように設定します。マーケターにとって「データが取れている」という安心感は何より大事。さあ、最初のタグを作りましょう！

---

## **本文**

### ■ GA4のタグを作る前に 〜計測タグはマーケターの命綱〜

マーケターにとって、アクセスデータは「空気」のようなものです。普段は意識しなくても、突然なくなると大問題になる。

たとえば、広告を回しているのに「流入数がゼロ」となったらどうでしょう？

- **A案:** 「アクセス数が減ったのかな？」と分析する。
- **B案:** 「そもそもタグが動いていないんじゃないか？」と疑う。

マーケターの経験が浅いうちはA案を考えがちですが、実際はB案（タグの計測漏れ）が原因なことが少なくありません。つまり、「正しくタグが動作しているかどうか」は、マーケティング施策の成否を分ける非常に重要な要素なのです。

ということで、今回はGTMを使ってGA4のページビュー計測タグを設定し、「データがきちんと取得できている」という安心感を得るところから始めましょう。

---

### **① GA4の測定IDを取得しよう**

まずは、Google Analytics 4（GA4）の管理画面から「測定ID」を取得します。

#### **1. GA4の管理画面にログイン**
Google Analytics（[https://analytics.google.com/](https://analytics.google.com/)）にアクセスし、GA4プロパティにログインします。

#### **2. 測定IDを確認する**
1. **「管理」**（画面左下の歯車アイコン）をクリック。
2. 「データストリーム」→ 設定済みのウェブストリームを選択。
3. 「G-XXXXXXX」という形式の「測定ID」をコピーする。

この測定IDが、GTMでGA4のタグを作成する際に必要になります。

---

### **② GTMでGA4ページビュータグを作成しよう**

#### **1. GTMにログインして新しいタグを作成**

1. [Google Tag Manager](https://tagmanager.google.com/) にアクセスし、コンテナを開く。
2. 左メニューの「**タグ**」をクリック。
3. 「**新規**」ボタンを押して、新しいタグを作成。

#### **2. タグの種類を「GA4 設定」にする**

1. 「**タグの設定**」をクリック。
2. 「**Google アナリティクス: GA4 設定**」を選択。
3. 「**測定ID**」に、先ほどGA4の管理画面から取得した測定ID（G-XXXXXXX）を入力。

#### **3. 送信先データを管理する（データストリームの設定）**

- デフォルトの状態で「データストリーム」に情報が送られるので、そのままでOK。
- **「この設定タグをすべてのGA4イベントタグに使用する」にチェックを入れる**（今後追加するイベント計測でも同じ設定を使える）。

---

### **③ トリガーを設定しよう（ページビュー時に発火）**

1. 「**トリガー**」をクリックし、「新規」を選択。
2. 「**ページビュー**」を選択（これにより、ページが読み込まれるたびにタグが発火）。
3. **「すべてのページ」** を選択して保存。

これで、「すべてのページでページビューを計測するGA4タグ」が完成しました！

---

### **④ プレビューモードで動作確認をする**

GTMでは、タグを本番環境に適用する前に「プレビューモード」でテストができます。

#### **1. プレビューを開始する**

1. GTMの管理画面で「プレビュー」ボタンをクリック。
2. 計測したいサイトのURLを入力し、「開始」をクリック。
3. 別ウィンドウで自分のサイトが開き、GTMのデバッグツールが表示される。

#### **2. タグの発火を確認する**

- GTMのデバッグツールで「**Tags Fired（発火したタグ）**」を確認。
- 「GA4設定」タグが正しく発火しているかをチェック。
- Google Analytics 4のリアルタイムレポートでもデータが送信されているか確認する。

---

### **⑤ 公開（タグを本番環境に適用）**

問題なく動作していることを確認したら、GTMのタグを本番環境に反映させましょう。

#### **1. コンテナの公開手順**

1. GTM管理画面で「送信」ボタンをクリック。
2. 「バージョン名」を入力（例：「GA4ページビュータグ追加」）。
3. 「公開」ボタンを押して適用。

これで、GA4のページビュータグが本番環境で稼働し始めました！

---

### **■ まとめ 〜最初のタグが完成！マーケターの第一歩〜**

今回の内容を振り返ると、

1. **GA4の測定IDを取得する**（Google Analyticsの管理画面から）
2. **GTMでGA4ページビュータグを作成する**（測定IDを設定）
3. **トリガーを「ページビュー」に設定する**（すべてのページで発火）
4. **プレビューモードで動作確認をする**（データが送信されているかチェック）
5. **問題なければ公開する**（本番環境に適用）

これで、マーケティングデータの収集がスタートしました！

GTMを使えば、エンジニアに依頼せずともタグの管理ができ、スムーズに計測を進められます。これは、マーケターにとって非常に大きなメリットです。

---

### **■ 明日の予告 〜プレビューモードとデバッグの活用〜**

GTMを使う上で最も重要な「プレビューモード」と「デバッグ機能」。
「タグが動かない！」と慌てないために、デバッグの基本を次回しっかり学びましょう！

