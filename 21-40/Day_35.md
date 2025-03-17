**タイトル:**  
未経験から100日後にGTMのプロになる話【Day 35】  
他ツールとのデータ連携 〜GTMをハブにしてデータを活かせ！〜

---

**概要（リード文）:**  
「GTMで取得したデータを、もっと活用したい！」  
「Google Analytics 4だけじゃなく、BigQueryやCRMにも連携できないの？」  
そんな疑問を解決するのが **「GTMと他ツールのデータ連携」** です。本日は、GTMをデータのハブとして活用し、マーケティングの精度を高める方法を解説します！

…今日からあなたは **「データの交通整理員」** です。データが適切なツールに届くよう、GTMのパワーを最大限に活用しましょう！

---

## **本文**

### ■ なぜGTMと他ツールを連携するのか？

GTMは「タグを管理するツール」ですが、**「データを蓄積・分析するツール」** と連携することで、さらに価値を発揮します。

例えば、
✅ **「GTMで取得したデータをGoogle BigQueryに送って、高度な分析を行いたい！」**  
✅ **「CRM（顧客管理システム）と連携して、広告配信を最適化したい！」**  
✅ **「Googleスプレッドシートにリアルタイムでデータを記録したい！」**  

これらを実現することで、データを **「取るだけ」ではなく、「使えるデータ」に変える** ことができます。

では、GTMを使った他ツールとのデータ連携方法を見ていきましょう！

---

### **① Google BigQueryと連携する（高度なデータ分析）**

#### **1. Google Analytics 4のデータをBigQueryに送る**

Google BigQuery（BQ）を使うと、GA4のデータをSQLで自由に分析できます。

**BigQuery連携の手順**
1. Google Analytics 4の管理画面を開く。
2. 「**管理**」→「**BigQueryリンク**」を選択。
3. 「**リンクを追加**」をクリックし、BigQueryのプロジェクトを選択。
4. 「**データをエクスポート**」を有効化。
5. 保存。

✅ **これで、GA4のデータがBigQueryにエクスポートされ、SQLを使った詳細分析が可能になります！**

---

### **② CRMと連携する（広告配信の最適化）**

CRM（SalesforceやHubSpotなど）と連携することで、GTMで取得したデータを広告最適化に活用できます。

#### **1. データレイヤーを使って顧客情報を取得**

```javascript
<script>
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    'event': 'crm_sync',
    'user_id': '12345',
    'customer_type': 'VIP'
  });
</script>
```

#### **2. GTMでデータをCRMに送信する**

1. GTMの「**タグ**」メニューを開く。
2. 「**新規**」をクリックし、タグの種類を「**カスタムHTML**」に設定。
3. 以下のコードを貼り付け、CRMのエンドポイントにデータを送信。

```html
<script>
  fetch('https://your-crm-api.com/sync', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      user_id: '{{DLV - User ID}}',
      customer_type: '{{DLV - Customer Type}}'
    })
  });
</script>
```

4. 「**トリガー**」を「**CRMデータ送信（カスタムイベント）**」に設定。
5. 保存。

✅ **これで、GTM経由で顧客データをCRMに送信できるようになります！**

---

### **③ Googleスプレッドシートにデータを記録する（リアルタイムログ）**

GTMのデータをGoogleスプレッドシートに記録することで、リアルタイムのデータログを可視化できます。

#### **1. Google Apps Script（GAS）を作成する**

1. Googleスプレッドシートを開く。
2. 「拡張機能」→「Apps Script」を開く。
3. 以下のコードを貼り付け、スクリプトを保存。

```javascript
function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Logs');
  var data = JSON.parse(e.postData.contents);
  sheet.appendRow([new Date(), data.event_name, data.page_url]);
  return ContentService.createTextOutput("Success");
}
```

4. 「デプロイ」→「新しいデプロイ」をクリックし、ウェブアプリとして公開。
5. 発行されたURLをコピー。

#### **2. GTMでスプレッドシートにデータを送信**

1. GTMの「**タグ**」メニューを開く。
2. 「**新規**」をクリックし、タグの種類を「**カスタムHTML**」に設定。
3. 以下のコードを貼り付け、先ほどのGASのURLを使用。

```html
<script>
  fetch('https://script.google.com/macros/s/xxxxxxx/exec', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      event_name: '{{Event Name}}',
      page_url: '{{Page URL}}'
    })
  });
</script>
```

4. 「**トリガー**」を「**すべてのページビュー**」に設定。
5. 保存。

✅ **これで、GTMのデータをスプレッドシートに記録できるようになります！**

---

### **■ まとめ 〜GTMをデータハブにして活用しよう！〜**

✅ **「Google BigQuery」にデータを送信し、高度な分析を可能に！**  
✅ **「CRM」と連携し、広告配信を最適化！**  
✅ **「Googleスプレッドシート」にデータを記録し、リアルタイムで可視化！**  
✅ **「プレビューモード」でテストし、問題なければ公開する！**  

これを活用すれば、
- **「広告・GA4・CRMを連携したマーケティング最適化」**
- **「スプレッドシートでリアルタイムデータ管理」**
- **「高度なSQL分析でユーザー行動を可視化」**

といったことが可能になります！

---

### **■ 明日の予告 〜最新機能とアップデート情報〜**

次回は、**「GTMの最新機能とアップデート」** を学びます！

