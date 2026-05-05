/* =========================================================
   TOKO WORKS 社会派 DEEP Lab ｜ 記事データ
   ---------------------------------------------------------
   記事を追加するとき：
     該当カテゴリの articles 配列に {} を1つ追加するだけ。
     index.html・その他ファイルは一切触らない。

   カテゴリ構成：
     - nikkei-mj  … 日経・MJの記事を深堀り（showSource: true）
     - ai-trends  … AIの潮流を深堀り
     - japan-now  … 日本の「今」を深堀り

   フィールド説明：
     icon      … カード左上の絵文字
     source    … 「📰 媒体名｜年月日」形式（showSource:true のカテゴリのみ使用）
     title     … カードタイトル（<br> で改行可）
     url       … リンク先（https://tokokanri10502-pixel.github.io/... 形式）
     desc      … カード本文の説明
     date      … 記事の公開日（"YYYY.MM.DD" 形式）
     tag       … バッジ種別（"study"|"app"|"life"）
     tagLabel  … バッジ表示文言（通常は "勉強会資料"）
   ========================================================= */

window.ARTICLES = {
  categories: [
    {
      id: "nikkei-mj",
      label: "日経・MJの記事を深堀り",
      showSource: true,
      articles: [
        {
          icon: "🛢️",
          image: "images/naphtha.png",
          source: "📰 日経｜2026年4月30日",
          title: "特集｜「ナフサ不足」が変える<br>小売の風景──ホルムズから食卓まで",
          url: "https://tokokanri10502-pixel.github.io/naphtha-tokushu.html",
          desc: "国産ナフサ価格は4-6月期に2倍弱へ。値上げラッシュ第二波と「巣ごもりGW」が示す、これから半年の消費の輪郭をデータで読む。",
          date: "2026.05.05",
          tag: "study",
          tagLabel: "※画像はイメージです"
        },
        {
          icon: "🛍️",
          image: "images/oshikatsu.jpg",
          source: "📰 日本経済新聞｜2026年4月17日",
          title: "特集｜推し活が変える<br>消費の地図",
          url: "https://tokokanri10502-pixel.github.io/oshi-katsu-tokushu.html",
          desc: "物価高でも伸び続ける「推し活」経済圏の実態。3.8兆円市場・2,600万人の行動原理をデータで解説",
          date: "2026.04.17",
          tag: "study",
          tagLabel: "※画像はイメージです"
        },
        {
          icon: "🍳",
          image: "images/hasegawaakari.jpg",
          source: "📰 日経MJ｜2026年4月17日",
          title: "特集｜長谷川あかり現象を解読<br>「疲れた日本人を救う」料理家の正体",
          url: "https://tokokanri10502-pixel.github.io/hasegawa-tokushu.html",
          desc: "SNS総フォロワー135万人・著書30万部（発信半年）。なぜ今、彼女は時代のニーズと精密に一致するのか。社会背景と経営視点から徹底分析。",
          date: "2026.04.19",
          tag: "study",
          tagLabel: "※画像はイメージです"
        },
        {
          icon: "🍡",
          image: "images/mochimochi.jpg",
          source: "📰 日経MJ｜2026年4月20日",
          title: "特集｜口どけから、もちもちへ<br>食感ランキングに異変あり",
          url: "https://tokokanri10502-pixel.github.io/mochimochi-tokushu.html",
          desc: "スイーツ単価が過去最高の227円を更新するなか、食感ランキングで唯一浮上したもちもち。インフレ時代の「充実感経済」「ご自愛消費」「SNS映え」「K-スイーツ」の4軸から、食卓の小さな異変を社会構造として読み解く。",
          date: "2026.04.21",
          tag: "study",
          tagLabel: "※画像はイメージです"
        },
        {
          icon: "🛒",
          image: "images/pb.jpg",
          source: "📰 日経MJ｜2026年4月27日",
          title: "特集｜安さの先へ──<br>イズミ、イオンのPB戦略",
          url: "https://tokokanri10502-pixel.github.io/pb-tokushu.html",
          desc: "イズミ会長が日経MJで改めて語った「第二の創業」。一方、4月初旬発表のイオンも過去最高益を見込み、PBを軸に据える。進め方の色合いは違うが、向かう方向はそろって「PB拡大」。家計の食費が変わらないまま、消費者の買い物には何が起きるのか。ゆめイチ8.6倍拡大のイズミと、価値観スコアのイオン──地域インフラとしてのスーパーが届けるべき「豊かさ」を問う。",
          date: "2026.04.27",
          tag: "study",
          tagLabel: "※画像はイメージです"
        }
      ]
    },
    {
      id: "ai-trends",
      label: "AIの潮流を深堀り",
      showSource: false,
      articles: [
        {
          icon: "🤖",
          image: "images/gundam.jpg",
          title: "特集｜ガンダムの駆動はAIだった⁉<br>1979年のアニメが描いた先見性",
          url: "https://tokokanri10502-pixel.github.io/anime-ai-gundam-tokushu.html",
          desc: "「AI」という言葉を一度も使わずに、現代AI論の核を先取りしていた1979年のガンダム。「学習する機械」「頭脳と身体の分離」「人間の知覚」── 47年越しに見えてくる3つの先見性を解読する。",
          date: "2026.04.19",
          tag: "study",
          tagLabel: "※画像はイメージです"
        },
        {
          icon: "⚖️",
          image: "images/claude.jpg",
          title: "特集｜なぜ、今Claudeなのか<br>信念で動くAI企業 Anthropic の正体",
          url: "https://tokokanri10502-pixel.github.io/anthropic-tokushu.html",
          desc: "米国政府から「Huaweiと同列のリスク企業」と指定されたAnthropic。OpenAIから派生し、利益最大化を法的に放棄した異端児が、今Claude躍進の裏側で何を選び続けているのか──思想と国防省事件の両面から読み解く。",
          date: "2026.04.25",
          tag: "study",
          tagLabel: "※画像はイメージです"
        },
        {
          icon: "⚡",
          image: "images/xaigrok.jpg",
          title: "特集｜イーロン・マスクの第4極戦略<br>xAIとGrokが描く、もう一つのAI地図",
          url: "https://tokokanri10502-pixel.github.io/xai-grok-tokushu.html",
          desc: "ChatGPT・Gemini・Claudeに続く第4のAI企業 xAI。月10億ドル赤字、4か月でデータセンター建設、創業者11名中9名離脱、SpaceX統合 ── 異常値ばかりが並ぶ「マスクのAI」を、思想・物理力・組織から読み解く。",
          date: "2026.04.25",
          tag: "study",
          tagLabel: "※画像はイメージです"
        }
      ]
    },
    {
      id: "japan-now",
      label: "日本の「今」を深堀り",
      showSource: false,
      articles: [
        {
          icon: "💄",
          image: "images/kankoku.png",
          title: "特集｜イオン広島府中の改装から見る<br>コスメ消費の現状",
          url: "https://tokokanri10502-pixel.github.io/kankoku-cosme-tokushu.html",
          desc: "2026年4月28日、中国・四国エリアの旗艦店として刷新されたイオンスタイル広島府中。グラムビューティーク全面刷新を起点に、ロビン・フッド甚目寺店4/24開業、ドラッグストアの二極化、地場スーパーの衣料苦戦──いま日本のコスメ消費に何が起きているかをファクトベースで読む。マーケ担当者向けに「動機で切る／プチプラを格上げる／体験で接続する」の3つの視点を提示。",
          date: "2026.05.01",
          tag: "study",
          tagLabel: "※画像はイメージです"
        },
        {
          icon: "📊",
          image: "images/nihonhinkon.jpg",
          title: "特集｜日本の貧困<br>「一億総中流」の終焉",
          url: "https://tokokanri10502-pixel.github.io/nihon-hinkon/",
          desc: "10年前との対比・アンダークラス890万人の実態・格差社会の未来予測を図表で解説",
          date: "2026.04.17",
          tag: "study",
          tagLabel: "※画像はイメージです"
        }
      ]
    }
  ]
};
