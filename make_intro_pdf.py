# -*- coding: utf-8 -*-
"""
deep-lab-site の社内紹介資料 A4 1枚 PDF を生成する。
- サイトコンセプト・狙い
- 代表記事サムネイル（カテゴリごとに 1 件）
- サイト URL への QR コード
"""
from pathlib import Path
from io import BytesIO

import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

BASE = Path(r"C:\Users\seisaku00\Desktop\Development\deep-lab-site")
OUT = BASE / "deep-lab-site_intro.pdf"
SITE_URL = "https://tokokanri10502-pixel.github.io/"

# Japanese fonts — Windows 標準の Yu Gothic TTC を使う
# TTC のサブフォント index: 0 = Yu Gothic, 1 = Yu Gothic UI 系
pdfmetrics.registerFont(TTFont("YuGothB", r"C:\Windows\Fonts\YuGothB.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("YuGothM", r"C:\Windows\Fonts\YuGothM.ttc", subfontIndex=0))

JP_BOLD = "YuGothB"
JP_REG = "YuGothM"

# Colors (matching the site palette)
NAVY = (0x0f / 255, 0x0f / 255, 0x1a / 255)
NAVY2 = (0x1a / 255, 0x1a / 255, 0x2e / 255)
RED = (0xe5 / 255, 0x39 / 255, 0x35 / 255)
GREY_TEXT = (0.20, 0.20, 0.22)
GREY_SUB = (0.45, 0.45, 0.50)
LIGHT_LINE = (0.85, 0.85, 0.88)
CHIP_BG = (0xff / 255, 0xeb / 255, 0xee / 255)


PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt


def make_qr_image(url: str) -> ImageReader:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return ImageReader(buf)


def draw_header(c: canvas.Canvas):
    # Header band
    band_h = 32 * mm
    c.setFillColorRGB(*NAVY2)
    c.rect(0, PAGE_H - band_h, PAGE_W, band_h, stroke=0, fill=1)

    # red accent bar
    c.setFillColorRGB(*RED)
    c.rect(0, PAGE_H - band_h, 6 * mm, band_h, stroke=0, fill=1)

    # Eyebrow chip "TOKO WORKS"
    chip_x, chip_y = 16 * mm, PAGE_H - 14 * mm
    c.setFillColorRGB(*RED)
    c.roundRect(chip_x, chip_y, 28 * mm, 5.5 * mm, 1 * mm, stroke=0, fill=1)
    c.setFillColorRGB(1, 1, 1)
    c.setFont(JP_BOLD, 8)
    c.drawCentredString(chip_x + 14 * mm, chip_y + 1.6 * mm, "TOKO WORKS")

    # Title
    c.setFillColorRGB(1, 1, 1)
    c.setFont(JP_BOLD, 22)
    title_y = PAGE_H - 23 * mm
    c.drawString(16 * mm, title_y, "社会派 ")
    title_w = c.stringWidth("社会派 ", JP_BOLD, 22)
    c.setFillColorRGB(*RED)
    c.drawString(16 * mm + title_w, title_y, "DEEP Lab")

    # Subtitle
    c.setFillColorRGB(0.85, 0.85, 0.88)
    c.setFont(JP_REG, 9.5)
    c.drawString(16 * mm, PAGE_H - 29 * mm, "社会の深層を、データと言葉で読み解く ─ 社内向け 知的アーカイブ")


def draw_concept(c: canvas.Canvas, top_y: float) -> float:
    """returns next y (top of next section)"""
    # Section title
    c.setFillColorRGB(*RED)
    c.rect(16 * mm, top_y - 6 * mm, 1.2 * mm, 5 * mm, stroke=0, fill=1)
    c.setFillColorRGB(*GREY_TEXT)
    c.setFont(JP_BOLD, 11)
    c.drawString(19 * mm, top_y - 4.7 * mm, "コンセプト・狙い")

    body_y = top_y - 14 * mm
    c.setFillColorRGB(*GREY_TEXT)
    c.setFont(JP_REG, 9.6)
    lines = [
        "日経・日経MJ・AI・社会動向のニュースを、社内の判断や雑談に効く粒度まで",
        "噛み砕いて解説するアーカイブサイトです。「なぜ今この話題なのか」「現場の",
        "打ち手にどう繋がるか」を、データと社会背景の両面から短時間で掴めます。",
    ]
    leading = 5.2 * mm
    for i, ln in enumerate(lines):
        c.drawString(16 * mm, body_y - i * leading, ln)

    # 3 pillars
    pillars = [
        ("日経・MJ", "話題のニュースを\n深堀り・解説"),
        ("AIの潮流", "Claude / xAI など\n最新トレンドを解読"),
        ("日本の今", "貧困・消費・社会構造\nを図表で可視化"),
    ]
    px = 16 * mm
    py = body_y - len(lines) * leading - 6 * mm
    box_w = (PAGE_W - 32 * mm - 6 * mm) / 3
    box_h = 18 * mm
    for i, (head, sub) in enumerate(pillars):
        x = px + i * (box_w + 3 * mm)
        c.setFillColorRGB(*CHIP_BG)
        c.roundRect(x, py - box_h, box_w, box_h, 2 * mm, stroke=0, fill=1)
        c.setFillColorRGB(*RED)
        c.setFont(JP_BOLD, 10)
        c.drawString(x + 4 * mm, py - 6 * mm, head)
        c.setFillColorRGB(*GREY_TEXT)
        c.setFont(JP_REG, 8.6)
        for j, l in enumerate(sub.split("\n")):
            c.drawString(x + 4 * mm, py - 11 * mm - j * 4.2 * mm, l)

    return py - box_h - 8 * mm


def draw_articles(c: canvas.Canvas, top_y: float) -> float:
    # Section title
    c.setFillColorRGB(*RED)
    c.rect(16 * mm, top_y - 6 * mm, 1.2 * mm, 5 * mm, stroke=0, fill=1)
    c.setFillColorRGB(*GREY_TEXT)
    c.setFont(JP_BOLD, 11)
    c.drawString(19 * mm, top_y - 4.7 * mm, "代表記事")

    cards = [
        {
            "img": BASE / "images" / "pb.jpg",
            "cat": "日経・MJの記事を深堀り",
            "title": "安さの先へ ─ イズミ、イオンのPB戦略",
            "date": "2026.04.27",
        },
        {
            "img": BASE / "images" / "claude.jpg",
            "cat": "AIの潮流を深堀り",
            "title": "なぜ、今 Claude なのか ─ Anthropic の正体",
            "date": "2026.04.25",
        },
        {
            "img": BASE / "images" / "nihonhinkon.jpg",
            "cat": "日本の「今」を深堀り",
            "title": "日本の貧困 ─「一億総中流」の終焉",
            "date": "2026.04.17",
        },
    ]

    grid_top = top_y - 10 * mm
    inner_w = PAGE_W - 32 * mm
    gap = 4 * mm
    card_w = (inner_w - gap * 2) / 3
    img_h = 32 * mm
    text_h = 26 * mm
    card_h = img_h + text_h

    for i, card in enumerate(cards):
        x = 16 * mm + i * (card_w + gap)
        y = grid_top - card_h

        # card frame
        c.setStrokeColorRGB(*LIGHT_LINE)
        c.setLineWidth(0.6)
        c.roundRect(x, y, card_w, card_h, 2 * mm, stroke=1, fill=0)

        # image
        try:
            c.drawImage(
                str(card["img"]), x + 0.4 * mm, y + text_h,
                width=card_w - 0.8 * mm, height=img_h - 0.4 * mm,
                preserveAspectRatio=True, anchor="c", mask="auto",
            )
        except Exception:
            c.setFillColorRGB(0.9, 0.9, 0.92)
            c.rect(x + 0.4 * mm, y + text_h, card_w - 0.8 * mm, img_h - 0.4 * mm, stroke=0, fill=1)

        # category label
        c.setFillColorRGB(*RED)
        c.setFont(JP_BOLD, 7.6)
        c.drawString(x + 3 * mm, y + text_h - 5 * mm, card["cat"])

        # title (wrap by char count)
        c.setFillColorRGB(*GREY_TEXT)
        c.setFont(JP_BOLD, 9.2)
        title = card["title"]
        max_chars = 18
        line1 = title[:max_chars]
        line2 = title[max_chars:max_chars * 2]
        c.drawString(x + 3 * mm, y + text_h - 10 * mm, line1)
        if line2:
            c.drawString(x + 3 * mm, y + text_h - 14.5 * mm, line2)

        # date
        c.setFillColorRGB(*GREY_SUB)
        c.setFont(JP_REG, 7.6)
        c.drawString(x + 3 * mm, y + 3 * mm, card["date"])

    return grid_top - card_h - 8 * mm


def draw_compliance(c: canvas.Canvas, top_y: float) -> float:
    # Section title
    c.setFillColorRGB(*RED)
    c.rect(16 * mm, top_y - 6 * mm, 1.2 * mm, 5 * mm, stroke=0, fill=1)
    c.setFillColorRGB(*GREY_TEXT)
    c.setFont(JP_BOLD, 11)
    c.drawString(19 * mm, top_y - 4.7 * mm, "制作上のお約束 ─ 著作権・社会的ルールの順守")

    # Panel
    inner_w = PAGE_W - 32 * mm
    panel_top = top_y - 10 * mm
    panel_h = 28 * mm
    c.setFillColorRGB(0.98, 0.98, 0.99)
    c.setStrokeColorRGB(*LIGHT_LINE)
    c.setLineWidth(0.6)
    c.roundRect(16 * mm, panel_top - panel_h, inner_w, panel_h, 2 * mm, stroke=1, fill=1)

    items = [
        "元記事の文章は直接引用・転載しません。表現はすべてオリジナルで再構成します。",
        "数字・データ・固有名詞は事実として参照し、各記事末尾の sources に出典を明記します。",
        "公開情報をもとに独自に編集・再構成する体裁を徹底し、第三者の権利を尊重します。",
        "社内共有を目的とした非営利の知的アーカイブとして運用しています。",
    ]
    c.setFillColorRGB(*GREY_TEXT)
    c.setFont(JP_REG, 8.8)
    line_y = panel_top - 6 * mm
    for ln in items:
        # red bullet dot
        c.setFillColorRGB(*RED)
        c.circle(20 * mm, line_y + 1.2 * mm, 0.7 * mm, stroke=0, fill=1)
        c.setFillColorRGB(*GREY_TEXT)
        c.drawString(23 * mm, line_y, ln)
        line_y -= 5.2 * mm

    return panel_top - panel_h - 6 * mm


def draw_footer_qr(c: canvas.Canvas, top_y: float):
    # divider
    c.setStrokeColorRGB(*LIGHT_LINE)
    c.setLineWidth(0.6)
    c.line(16 * mm, top_y, PAGE_W - 16 * mm, top_y)

    # left text block
    left_x = 16 * mm
    block_top = top_y - 7 * mm
    c.setFillColorRGB(*GREY_TEXT)
    c.setFont(JP_BOLD, 11)
    c.drawString(left_x, block_top, "サイトはこちら ─ スマホで読み込めます")

    c.setFillColorRGB(*GREY_SUB)
    c.setFont(JP_REG, 9)
    msg_lines = [
        "・スマホ・PC どちらからでもアクセスできます",
        "・記事は随時追加。社内勉強会・朝礼ネタ・営業の話題作りにご活用ください",
        "・感想・取り上げてほしいテーマがあれば気軽にお知らせください",
    ]
    for i, ln in enumerate(msg_lines):
        c.drawString(left_x, block_top - 6 * mm - i * 4.6 * mm, ln)

    # URL
    c.setFillColorRGB(*RED)
    c.setFont(JP_BOLD, 9.5)
    c.drawString(left_x, block_top - 26 * mm, SITE_URL)

    # QR (right)
    qr_size = 32 * mm
    qr_x = PAGE_W - 16 * mm - qr_size
    qr_y = top_y - qr_size - 6 * mm
    c.drawImage(make_qr_image(SITE_URL), qr_x, qr_y,
                width=qr_size, height=qr_size, mask="auto")
    # QR caption
    c.setFillColorRGB(*GREY_SUB)
    c.setFont(JP_REG, 7.4)
    c.drawCentredString(qr_x + qr_size / 2, qr_y - 3 * mm, "QRコードでアクセス")


def draw_page_footer(c: canvas.Canvas):
    c.setFillColorRGB(*GREY_SUB)
    c.setFont(JP_REG, 7)
    c.drawString(16 * mm, 8 * mm, "© 2026 TOKO WORKS ─ 社会派 DEEP Lab  /  社内共有用資料")
    c.drawRightString(PAGE_W - 16 * mm, 8 * mm, "Issued: 2026.04.30")


def build():
    c = canvas.Canvas(str(OUT), pagesize=A4)
    c.setTitle("社会派 DEEP Lab 紹介")
    c.setAuthor("TOKO WORKS")

    draw_header(c)
    next_y = draw_concept(c, top_y=PAGE_H - 38 * mm)
    next_y = draw_articles(c, top_y=next_y)
    next_y = draw_compliance(c, top_y=next_y)
    draw_footer_qr(c, top_y=next_y)
    draw_page_footer(c)

    c.showPage()
    c.save()
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    build()
