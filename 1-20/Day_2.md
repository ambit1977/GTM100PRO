**タイトル:**  
未経験から100日後にGTMのプロになる話【Day 2】  
GTMのアカウント作成とコンテナ設定 〜マーケターの自由への第一歩〜

---

**概要（リード文）:**  
GTMを使うための第一歩、それはアカウント作成とコンテナ設定です。これさえ済ませれば、マーケターがエンジニアの工数を気にせずにタグを管理できる未来が待っています。かつてタグの設置をお願いするたびに「また？」と言われていたあの日々にさようなら。本日は、GTMの基本環境を整えて、よりスムーズなタグ運用を実現する準備をしましょう！

---

## 本文

### ■ GTMのアカウントを作る日は、マーケターの自由記念日

マーケターの皆さん、「このタグ、設置お願いできますか？」とエンジニアに相談したら、「次のリリースで対応します」と言われ、数週間待たされる――そんな経験、ありませんか？

私もかつて、広告の計測タグをお願いしたのに、ようやく設置された頃にはキャンペーンが半分終わっていた…なんてことがありました。マーケティング施策はスピードが命。しかし、ウェブサイトの運用は慎重に行わなければならず、「ちょっとタグを入れたいんですけど」と気軽に言える環境の方が珍しいのが現実です。

そんな中、「GTMを使えばマーケターがタグを自由に管理できる」と聞いたときの衝撃は忘れられません。ただし、**「自由に管理」と言っても、マーケターが直接サイトのコードをいじるわけではない**のがポイントです。

一般的な企業のウェブ運営では、サイトの修正や更新はエンジニアが担当します。GTMのコンテナタグをサイトに設置する作業も、基本的にはエンジニアが行うことが多いでしょう。マーケターとしては、**エンジニアに「GTMを使いたいので、コンテナタグを設置してください」と依頼し、あとはGTMの管理画面から設定を進める**のが現実的なフローになります。

ということで、今回はまず、GTMのアカウントを作成し、コンテナ設定を行い、エンジニアに設置を依頼するまでの流れを解説します。

---

### ■ Google Tag Managerのアカウント作成方法

まずは、GTMのアカウントを作りましょう。

#### **① Google Tag Managerの公式サイトにアクセス**
GTMを利用するには、Googleの公式サイト（[https://tagmanager.google.com/](https://tagmanager.google.com/)）にアクセスします。

#### **② アカウントを作成する**
画面の「アカウントを作成」ボタンをクリックし、以下の情報を入力します。

- **アカウント名:** 自社の会社名やプロジェクト名を入力（例：Acme Inc.）
- **国:** 日本
- **コンテナ名:** GTMを使用するサイトのURL（例：www.example.com）
- **ターゲットプラットフォーム:** ウェブ、iOS、Android、AMP から選択（通常は「ウェブ」）

#### **③ コンテナを作成する**
コンテナとは、GTMで管理するタグの「箱」のようなものです。この中にGA4のタグや広告タグを入れていきます。

ターゲットプラットフォームが「ウェブ」であることを確認し、「作成」をクリックします。

#### **④ 利用規約の確認**
Googleの利用規約が表示されるので、確認後「同意する」をクリック。

すると、「GTM-XXXXXXX」というコンテナIDが表示され、GTMの管理画面にアクセスできるようになります。

---

### ■ GTMのコンテナタグをエンジニアに依頼する

さて、GTMのアカウントとコンテナを作成したら、次に必要なのが**エンジニアへの設置依頼**です。

#### **① GTMのコードを取得する**
GTMの管理画面にアクセスすると、コンテナコード（スニペット）が表示されます。

```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->
```

#### **② エンジニアに依頼する内容をまとめる**
エンジニアへの依頼時には、以下のような内容をまとめて伝えましょう。

**件名:** 【GTM設置依頼】Google Tag Managerのコンテナタグ設置のお願い  
**本文:**
> お世話になっております。GTMを導入するため、以下のタグをウェブサイトに設置いただけますでしょうか？
>
> - **設置箇所:** `<head>`タグの直後、および`<body>`タグの直後
> - **タグ:**（上記のスニペットを記載）
>
> 追加後、動作確認のためにプレビューモードでチェックを行う予定です。
> ご対応のほど、よろしくお願いいたします。

エンジニアも仕事の優先順位があるので、**設置の目的と設置箇所を明確に伝えること**が大切です。「このタグを入れることで、マーケティング施策のタグ管理がしやすくなる」という背景を共有すると、よりスムーズに対応してもらえるかもしれません。

---

### ■ GTMの準備が整ったら次のステップへ

GTMのアカウント作成とコンテナ設定が完了し、エンジニアがコンテナタグを設置すれば、いよいよマーケターがGTMの管理画面からタグを設定できるようになります。

これで、「タグを追加したいけど、エンジニアのスケジュールが空くまで待たなきゃ…」という状況から一歩抜け出すことができます。マーケターがデータを自在に扱うための環境が整いました！

---

### ■ 明日の予告 〜GTMの管理画面ツアー〜

次回は、**GTMの管理画面を徹底解説**します。タグ・トリガー・変数がどこにあるのか、どのように操作するのか、基本的な機能を学びながら、さらに一歩進んでいきましょう。

マーケターとしての自由を手にした今、次はそれを最大限に活用するためのスキルを身につける番です。明日もぜひ読んでください！

