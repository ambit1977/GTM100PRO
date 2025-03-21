**タイトル:**  
未経験から100日後にGTMのプロになる話【Day 28】  
ECサイト向け計測設定（Google広告＆GA4）〜売れる店のタグ設定とは？〜

---

**概要（リード文）:**  
「ECサイトで売上を伸ばしたい！」  
「購入データを広告最適化に活用したい！」  
そんなときに欠かせないのが **GTMを活用した正確な計測設定** です。本日は、Google広告とGA4を活用したEC向け計測設定を解説します！

…って、こんな真面目な導入でいいんですか？ いやいや、今日はECサイト向け計測設定です。つまり、**「お客さんが財布を開く瞬間を逃さず記録する技」** を身につける日です！

マーケターの皆さん、タグの力で売上を底上げする準備はいいですか？ では、いってみましょう！

---

## **本文**

### ■ ECサイトで計測すべき重要データとは？

ECサイトでは、ただページビューを測るだけでは不十分です。売上に直結するデータを正しく計測し、それをマーケティングに活かすことが重要です。

例えば、
✅ **「どの商品が一番売れているのか？」**  
✅ **「カートに入れたけど購入しなかったユーザーはどれくらいいる？」**  
✅ **「広告経由の売上はどれくらい？」**  

これらを正しく計測することで、**「売れる戦略」** を見つけ出すことができます。

では、Google広告とGA4を使って、ECサイトの計測設定をしていきましょう！

---

### **① Google広告のコンバージョン計測（購入完了）**

まずは、Google広告経由での「購入」を計測するためのタグを設定します。

#### **1. Google広告のコンバージョンタグを取得する**

1. [Google広告](https://ads.google.com/) にログイン。
2. 「ツールと設定」→「コンバージョン」を選択。
3. 「新しいコンバージョンアクションを作成」をクリック。
4. 「ウェブサイト」を選択し、「購入」をコンバージョンイベントとして設定。
5. 「Googleタグマネージャーを使用する」を選択し、以下の情報を取得。
   - **コンバージョンID（AW-XXXXXXXXXX）**
   - **コンバージョンラベル（XXXXXXXXXXXXX）**

✅ **これで、GTMに設定する準備ができました！**

---

#### **2. GTMでGoogle広告の購入コンバージョンタグを作成**

1. GTMの「**タグ**」メニューを開く。
2. 「**新規**」をクリックし、タグの種類を「**Google 広告のコンバージョン トラッキング**」に設定。
3. 「**コンバージョン ID**」に `AW-XXXXXXXXXX` を入力。
4. 「**コンバージョン ラベル**」に `XXXXXXXXXXXXX` を入力。
5. 「送信するコンバージョン値」を `{{DLV - Total Value}}` にする（データレイヤーから取得）。
6. 保存。

✅ **これで、Google広告のコンバージョン計測の準備ができました！**

…ところで、このタグ、しっかり動作してくれないと困るんですが、**「購入完了ページがどこなのか」** ちゃんと把握できてますか？

次に、トリガーを設定して「購入完了時に発火するように」しましょう！

---

### **② トリガーを設定する（購入完了ページのみで発火）**

1. GTMの「**トリガー**」メニューを開く。
2. 「**新規**」をクリックし、トリガーの種類を「**ページビュー**」に設定。
3. 「このトリガーの発火を…」のオプションを「**一部のページビュー**」に変更。
4. **条件:** `Page URL 次を含む thank-you.html`
5. 保存。

✅ **これで、購入完了ページが表示されたときにタグが発火します！**

さて、購入データを広告だけでなく、**GA4でも取得したくないですか？** そうですよね、じゃあ次はGA4の設定に移りましょう！

---

### **③ GA4のEコマースイベントを設定する（購入データの計測）**

GA4では、ECサイト向けの「Eコマースイベント」を使うことで、売上データを詳細に記録できます。

#### **1. データレイヤーの準備**

購入完了時に、以下のようなデータレイヤーをサイト側で実装する必要があります。

```javascript
<script>
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    'event': 'purchase',
    'transaction_id': 'T123456',
    'value': 9800,
    'currency': 'JPY',
    'items': [
      {
        'id': 'P001',
        'name': 'スニーカー',
        'category': 'シューズ',
        'price': 9800
      }
    ]
  });
</script>
```

✅ **これで、購入完了時にGTMがデータを取得できるようになります！**

---

#### **2. GTMでGA4の購入イベントタグを作成**

1. GTMの「**タグ**」メニューを開く。
2. 「**新規**」をクリックし、タグの種類を「**Google アナリティクス: GA4 イベント**」に設定。
3. 「**設定タグを選択**」で、既存のGA4設定タグを選択。
4. 「**イベント名**」を `purchase` にする。
5. 「イベントパラメータを追加」ボタンをクリックし、
   - `transaction_id`: `{{DLV - Transaction ID}}`
   - `value`: `{{DLV - Total Value}}`
   - `currency`: `{{DLV - Currency}}`
6. 保存。

✅ **これで、GA4の「収益レポート」に売上データが反映されるようになります！**

---

### **■ まとめ 〜ECサイトの売上を見える化しよう！〜**

✅ **Google広告のコンバージョンタグを設定し、広告経由の売上を計測！**  
✅ **トリガーを「購入完了ページ」に限定し、正確なデータを取得！**  
✅ **GA4のEコマースイベントを設定し、売上レポートを作成！**  
✅ **「プレビューモード」でテストし、問題なければ公開する！**  

次回は、**「サーバーサイドGTMの活用」** を学びます！
「計測の精度をさらに向上させる方法」、楽しみにしていてください！

