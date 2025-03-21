**タイトル:**\
未経験から100日後にGTMのプロになる話【Day 83】\
【実践編】BtoBサイトでのタグ管理とリード計測

---

## **概要（リード文）**

「BtoBサイトでリード獲得を正確に測定したい！」
「フォーム送信のトラッキングやリードの質を分析するには？」

BtoBマーケティングでは、ECサイトやSaaSとは異なり、
**「問い合わせフォームの送信」「資料ダウンロード」「ホワイトペーパーの閲覧」** などのリード獲得が重要です。

そこで今回は、 **BtoBサイト向けのGTM活用法** を **ケーススタディ形式** で解説！

✅ **BtoBのリード計測で押さえるべきポイント**
✅ **フォーム送信のトラッキングとGoogle広告の最適化**
✅ **リードスコアリングのためのデータ活用法**

GTMを活用し、 **リード獲得の効率を最大化する方法** を学びましょう！

---

## **① BtoBのGTM設定のポイント**

BtoBサイトでは、**「リード獲得の質」** を計測することが非常に重要です。

 **BtoBマーケティングでGTMを活用するポイント**
✅ **フォーム送信の計測（問い合わせ・資料請求・デモ申込）**
✅ **ホワイトペーパー・PDFダウンロードのクリック計測**
✅ **Google広告やLinkedIn広告と連携し、リード獲得を最適化**
✅ **リードスコアリングのためのデータを取得**

 **「どのチャネルから質の高いリードが来ているのか？」を可視化することがカギ！**

---

## **② フォーム送信のトラッキングをGTMで設定する**

BtoBサイトでは **「問い合わせフォームの送信」** をコンバージョンとするケースが多いため、
**フォームの送信を正確にトラッキング** することが必須です。

 **フォーム送信を計測する方法（3つのパターン）**
✅ **ページ遷移型フォーム（送信後に「Thanksページ」に遷移）**
✅ **非同期フォーム（Ajaxを使用し、ページ遷移せずに送信）**
✅ **ボタンクリック型フォーム（確認ボタンを押したタイミングで計測）**

### ** GTMでフォーム送信を計測する方法**

#### **① Thanksページ（ページ遷移型）の場合**

1. **トリガーを作成**
   - トリガーの種類：「ページビュー」
   - 条件：「Page URL」→「含む」→ `/thanks`（ThanksページのURL）

2. **GA4のイベントタグを作成**
   - **イベント名**：`form_submit`
   - **イベントパラメータ**：`form_type: inquiry`（問い合わせ）
   - **トリガー**：「Thanksページビュー」

✅ **これでGA4にフォーム送信のデータが送信される！**

 **URL遷移があるフォームなら、この方法が最も簡単！**

---

#### **② 非同期フォーム（Ajax）の場合**

1. **カスタムイベントを発火させる（エンジニア対応）**
   - Ajax処理が完了したら、以下のコードを実装

```javascript
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  'event': 'form_submission',
  'form_type': 'inquiry'
});
```

2. **GTMでカスタムイベントトリガーを作成**
   - トリガーの種類：「カスタムイベント」
   - イベント名：「form_submission」

3. **GA4のイベントタグを作成**
   - イベント名：「form_submit」
   - パラメータ：「form_type: inquiry」
   - トリガー：「form_submission」

✅ **これでページ遷移がないフォームでも正確に計測できる！**

 **Ajaxを使ったフォームなら、この方法が最適！**

---

## **③ Google広告・LinkedIn広告のリード計測を最適化**

BtoBサイトでは、**Google広告やLinkedIn広告からのリードを正確に計測** し、
**「どの広告チャネルが最も良質なリードを獲得しているのか？」** を分析することが重要です。

### ** Google広告のコンバージョン設定（GTM版）**

1. **Google Adsの管理画面で「コンバージョン」を作成**
   - アクション：「リード（Lead）」
   - 計測方法：「ウェブサイト」
   - 設定完了後、**「コンバージョンID」と「コンバージョンラベル」** を取得

2. **GTMで「Google Adsコンバージョンタグ」を作成**
   - **コンバージョンID**：取得したIDを入力
   - **コンバージョンラベル**：取得したラベルを入力
   - **トリガー**：「フォーム送信」トリガーを設定

✅ **これで、Google広告経由の問い合わせが計測可能に！**

 **LinkedIn広告も同様に、コンバージョンタグをGTMで管理可能！**

---

## **④ リードスコアリングのためのデータ活用**

BtoBでは「リードの数」だけでなく、
**「どのリードが有望か？」（リードスコアリング）** を行うことが重要です。

 **リードスコアリングに活用できるデータ**
✅ **フォーム送信後のページ閲覧履歴（サイト滞在時間、閲覧ページ数）**
✅ **特定の資料ダウンロード（リードの関心を判別）**
✅ **企業属性データ（業種、企業規模、役職 など）**
✅ **広告流入元ごとのコンバージョン率の違い**

 **GTM×GA4でリードスコアリングを行う方法**

1. **フォーム送信後の行動データを取得（イベント計測）**
2. **Google BigQueryにデータを送信し、リードスコアリングを分析**
3. **スコアの高いリードにパーソナライズド広告を配信**

 **リードの質をデータで可視化し、営業・マーケティングの効率を向上！**

---

## **まとめ: BtoBリード獲得を最大化するGTM活用術！**

 **今回のポイント:**
✅ **BtoBのリード獲得には「フォーム送信」の計測が必須！**
✅ **Google広告・LinkedIn広告のコンバージョンタグをGTMで管理！**
✅ **リードスコアリングのために、ユーザーの行動データを活用！**
✅ **GTM×GA4を活用し、BtoBマーケティングを最適化！**

---

## **次回予告: メディアサイトでのGTM活用とエンゲージメント分析**