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
          icon: "🛍️",
          source: "📰 日本経済新聞｜2026年4月17日",
          title: "特集｜推し活が変える<br>消費の地図",
          url: "https://tokokanri10502-pixel.github.io/oshi-katsu/",
          desc: "物価高でも伸び続ける「推し活」経済圏の実態。3.8兆円市場・2,600万人の行動原理をデータで解説",
          date: "2026.04.17",
          tag: "study",
          tagLabel: "勉強会資料"
        },
        {
          icon: "🍳",
          source: "📰 日経MJ｜2026年4月17日",
          title: "特集｜長谷川あかり現象を解読<br>「疲れた日本人を救う」料理家の正体",
          url: "https://tokokanri10502-pixel.github.io/hasegawa-akari/",
          desc: "SNS総フォロワー135万人・著書30万部（発信半年）。なぜ今、彼女は時代のニーズと精密に一致するのか。社会背景と経営視点から徹底分析。",
          date: "2026.04.19",
          tag: "study",
          tagLabel: "勉強会資料"
        },
        {
          icon: "🍡",
          source: "📰 日経MJ｜2026年4月20日",
          title: "特集｜口どけから、もちもちへ",
          url: "https://tokokanri10502-pixel.github.io/mochimochi-tokushu.html",
          desc: "スイーツ単価が過去最高の227円を更新するなか、食感ランキングで唯一浮上したもちもち。インフレ時代の「充実感経済」「ご自愛消費」「SNS映え」「K-スイーツ」の4軸から、食卓の小さな異変を社会構造として読み解く。",
          date: "2026.04.21",
          tag: "study",
          tagLabel: "勉強会資料"
        }
      ]
    },
    {
      id: "ai-trends",
      label: "AIの潮流を深堀り",
      showSource: false,
      articles: [
        {
          icon: "🛒",
          title: "特集｜AI時代の販促構造変化<br>売り場はどうあるべきか",
          url: "https://tokokanri10502-pixel.github.io/kaimono-fukei/",
          desc: "現状、「買うと決めて」来店する割合は30％。AIの普及と食感度低下の二重変化を4つのSTAGEで読み解く",
          date: "2026.04.17",
          tag: "study",
          tagLabel: "勉強会資料"
        },
        {
          icon: "🤖",
          title: "特集｜アニメはAIを知っていた<br>1979年ガンダムが描いた見取り図",
          url: "https://tokokanri10502-pixel.github.io/anime-ai-gundam-tokushu.html",
          desc: "「AI」という言葉を一度も使わずに、AIの本質を描き切っていた1979年のガンダム。47年越しに見えてくる、知能と人間の三層構造を解読する。",
          date: "2026.04.19",
          tag: "study",
          tagLabel: "勉強会資料"
        },
        {
          icon: "⚖️",
          title: "特集｜なぜ、今Claudeなのか<br>信念で動くAI企業 Anthropic の正体",
          url: "https://tokokanri10502-pixel.github.io/anthropic-tokushu.html",
          desc: "米国政府から「Huaweiと同列のリスク企業」と指定されたAnthropic。OpenAIから派生し、利益最大化を法的に放棄した異端児が、今Claude躍進の裏側で何を選び続けているのか──思想と国防省事件の両面から読み解く。",
          date: "2026.04.25",
          tag: "study",
          tagLabel: "勉強会資料"
        }
      ]
    },
    {
      id: "japan-now",
      label: "日本の「今」を深堀り",
      showSource: false,
      articles: [
        {
          icon: "📊",
          title: "特集｜日本の貧困<br>「一億総中流」の終焉",
          url: "https://tokokanri10502-pixel.github.io/nihon-hinkon/",
          desc: "10年前との対比・アンダークラス890万人の実態・格差社会の未来予測を図表で解説",
          date: "2026.04.17",
          tag: "study",
          tagLabel: "勉強会資料"
        }
      ]
    }
  ]
};
