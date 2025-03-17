**タイトル:**\
未経験から100日後にGTMのプロになる話【Day 25】\
その他のサードパーティタグの統合 〜Twitter・LinkedIn・TikTokの計測を一元管理〜

---

**概要（リード文）:**\
「Twitter広告のコンバージョンを計測したい！」\
「LinkedInでBtoB向けの広告効果を分析したい！」\
「TikTokの広告データを取得してパフォーマンスを向上させたい！」\
GTMを活用すれば、これらのサードパーティタグを簡単に管理できます。本日は、主要なサードパーティ広告タグの設定方法を解説します！

---

## **本文**

### ■ GTMでサードパーティタグを管理するメリット

✅ **各広告プラットフォームのタグをGTMで一元管理できる！**\
✅ **広告パフォーマンスを比較しながら分析できる！**\
✅ **マーケティング施策に応じて発火条件を柔軟に設定できる！**

では、具体的にTwitter、LinkedIn、TikTokの広告タグをGTMで設定していきましょう。

---

## **① Twitterコンバージョンタグの設定**

Twitter広告を利用する場合、Twitterピクセルを設定することで、

- **広告経由のコンバージョンを測定**
- **リマーケティングリストの作成**
- **広告の最適化（CV最適化キャンペーン）**

が可能になります。

### **1. Twitterピクセル（コンバージョンタグ）を取得する**

1. [Twitter Ads](https://ads.twitter.com/) にアクセス。
2. 「ツール」→「コンバージョントラッキング」を開く。
3. 「コンバージョンイベントを作成」をクリック。
4. 計測したいコンバージョンの種類を選択（例：購入、問い合わせなど）。
5. 「Twitterピクセルコード」をコピー。

### **2. GTMでTwitterピクセルタグを作成**

1. GTMの「**タグ**」メニューを開く。
2. 「**新規**」をクリックし、タグの種類を「**カスタムHTML**」に設定。
3. 以下のコードを貼り付け、取得したTwitterピクセルIDを入力。

```html
<script>
  !function(e,t,n,s,u,a){e.twq||(s=e.twq=function(){s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);
  },s.version='1.1',s.queue=[],u=t.createElement(n),u.async=!0,u.src='//static.ads-twitter.com/uwt.js',
  a=t.getElementsByTagName(n)[0],a.parentNode.insertBefore(u,a))}(window,document,'script');
  twq('init','o1a2b3c4d5e6f7g8h9i'); // ここにTwitterのピクセルIDを入力
  twq('track','PageView');
</script>
```

4. 「**このタグを発火させるトリガー**」を「**全ページビュー**」に設定。
5. タグ名を「Twitterピクセル - ページビュー」にして保存。

✅ **これで、Twitter広告のコンバージョン計測が可能になります！**

---

## **② LinkedIn Insightタグの設定**

LinkedIn広告を活用する場合、「LinkedIn Insightタグ」を設置することで、

- **BtoB向け広告のコンバージョン計測**
- **オーディエンスリマーケティング**
- **LinkedIn内のアクションとサイトの訪問者データを連携**

が可能になります。

### **1. LinkedIn Insightタグを取得する**

1. [LinkedIn Campaign Manager](https://www.linkedin.com/campaignmanager/) にログイン。
2. 左メニューの「アカウントアセット」→「Insightタグ」を開く。
3. 「タグを取得」をクリックし、スクリプトをコピー。

### **2. GTMでLinkedIn Insightタグを作成**

1. GTMの「**タグ**」メニューを開く。
2. 「**新規**」をクリックし、タグの種類を「**カスタムHTML**」に設定。
3. 以下のLinkedIn Insightコードを貼り付ける。

```html
<script type="text/javascript">
  _linkedin_partner_id = "123456"; // ここにLinkedInのパートナーIDを入力
  window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
  window._linkedin_data_partner_ids.push(_linkedin_partner_id);
</script>
<script type="text/javascript">
  (function(){
    var s = document.getElementsByTagName("script")[0];
    var b = document.createElement("script");
    b.type = "text/javascript";b.async = true;
    b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
    s.parentNode.insertBefore(b, s);
  })();
</script>
```

4. 「**このタグを発火させるトリガー**」を「**全ページビュー**」に設定。
5. タグ名を「LinkedIn Insightタグ」にして保存。

✅ **これで、LinkedIn広告のコンバージョン計測が可能になります！**

---

## **③ TikTokピクセルの設定**

TikTok広告を運用する場合、「TikTokピクセル」を設定することで、

- **TikTok広告経由のコンバージョンを計測**
- **サイト訪問者のデータを取得し、リマーケティングリストを作成**
- **広告配信の最適化（ターゲティング強化）**

が可能になります。

### **1. TikTokピクセルを取得する**

1. [TikTok Ads Manager](https://ads.tiktok.com/) にログイン。
2. 左メニューの「アセット」→「イベント」→「ウェブイベント」を選択。
3. 「ピクセルを作成」をクリック。
4. 「マニュアルセットアップ」を選択し、スクリプトを取得。

### **2. GTMでTikTokピクセルタグを作成**

1. GTMの「**タグ**」メニューを開く。
2. 「**新規**」をクリックし、タグの種類を「**カスタムHTML**」に設定。
3. 以下のTikTokピクセルコードを貼り付ける。

```html
<script>
  !function (w, d, t) {
    w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];
    ttq.methods=["track","identify","conversion","get"];
    ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}
    for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);
    ttq.load=function(){var e=d.createElement("script");
    e.type="text/javascript",e.async=!0,e.src="https://analytics.tiktok.com/i18n/pixel/sdk.js?sdkid=YOUR_PIXEL_ID",
    d.getElementsByTagName("head")[0].appendChild(e)}
    ttq.load()}(window, document, "ttq");
</script>
```

4. 保存。

✅ **これで、TikTok広告のコンバージョン計測が可能になります！**

