"""
Genera los PDFs de entrega para la Clase 01 · Módulo 4.

Produce en la carpeta actual:
    slides-clase-01-modulo-04.pdf     — Slides visuales (sin scripts)
    ejercicios-practicos.pdf           — Ejercicios en PDF
    tablas-comparativas.pdf            — Tablas de referencia en PDF

Uso:
    python3 generate_pdf.py

Requiere: reportlab >= 4.0, markdown >= 3.0
    pip install reportlab markdown
"""

import re
import sys
from pathlib import Path

# ── ReportLab ─────────────────────────────────────────────────────────────────
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, inch, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak
)
from reportlab.platypus.flowables import HRFlowable

# ── Design tokens ─────────────────────────────────────────────────────────────
C_PRIMARY  = colors.HexColor("#0B5FFF")
C_BG       = colors.HexColor("#FAFAF7")
C_DARK     = colors.HexColor("#0A1628")
C_MUTED    = colors.HexColor("#555249")
C_WHITE    = colors.white
C_BORDER   = colors.HexColor("#D4D1C9")
C_ROW_ALT  = colors.HexColor("#F0F0EB")
C_ROW_HDR  = colors.HexColor("#0B5FFF")
C_SOFT_BG  = colors.HexColor("#EFF4FF")

# ── Fuente ────────────────────────────────────────────────────────────────────
def _register_inter():
    candidates = [
        "/Library/Fonts/Inter-Regular.ttf",
        "/System/Library/Fonts/Supplemental/Inter-Regular.ttf",
        str(Path.home() / "Library/Fonts/Inter-Regular.ttf"),
    ]
    bold_c = [p.replace("Regular", "Bold") for p in candidates]
    reg  = next((p for p in candidates if Path(p).exists()), None)
    bold = next((p for p in bold_c   if Path(p).exists()), None)
    if reg:
        pdfmetrics.registerFont(TTFont("Inter",      reg))
        pdfmetrics.registerFont(TTFont("Inter-Bold", bold or reg))
        return "Inter", "Inter-Bold"
    return "Helvetica", "Helvetica-Bold"

FONT_REG, FONT_BOLD = _register_inter()

# ─── Estilos compartidos ─────────────────────────────────────────────────────
def _styles():
    s = {
        "h1": ParagraphStyle("h1",
            fontName=FONT_BOLD, fontSize=20, textColor=C_DARK,
            spaceAfter=10, spaceBefore=18, leading=26),
        "h2": ParagraphStyle("h2",
            fontName=FONT_BOLD, fontSize=15, textColor=C_PRIMARY,
            spaceAfter=6, spaceBefore=14, leading=20),
        "h3": ParagraphStyle("h3",
            fontName=FONT_BOLD, fontSize=12, textColor=C_DARK,
            spaceAfter=4, spaceBefore=10, leading=16),
        "body": ParagraphStyle("body",
            fontName=FONT_REG, fontSize=11, textColor=C_DARK,
            spaceAfter=4, leading=16),
        "bullet": ParagraphStyle("bullet",
            fontName=FONT_REG, fontSize=11, textColor=C_DARK,
            leftIndent=14, firstLineIndent=-10,
            spaceAfter=3, leading=15),
        "muted": ParagraphStyle("muted",
            fontName=FONT_REG, fontSize=10, textColor=C_MUTED,
            spaceAfter=3, leading=14),
        "code": ParagraphStyle("code",
            fontName="Courier", fontSize=10, textColor=C_DARK,
            backColor=C_ROW_ALT, leftIndent=12, rightIndent=12,
            spaceAfter=3, leading=14),
        "note": ParagraphStyle("note",
            fontName=FONT_REG, fontSize=10, textColor=C_PRIMARY,
            leftIndent=12, spaceAfter=4, leading=14,
            backColor=C_SOFT_BG),
    }
    return s


def _rich(text: str) -> str:
    """Convierte **bold** a tags ReportLab."""
    text = re.sub(r"\*\*(.+?)\*\*",
                  r'<font name="' + FONT_BOLD + r'" color="#0B5FFF"><b>\1</b></font>', text)
    return text


def _tbl_style(n_rows: int) -> TableStyle:
    cmds = [
        ("BACKGROUND",  (0, 0), (-1, 0),   C_ROW_HDR),
        ("TEXTCOLOR",   (0, 0), (-1, 0),   C_WHITE),
        ("FONTNAME",    (0, 0), (-1, 0),   FONT_BOLD),
        ("FONTSIZE",    (0, 0), (-1, 0),   10),
        ("ALIGN",       (0, 0), (-1, 0),   "CENTER"),
        ("FONTNAME",    (0, 1), (-1, -1),  FONT_REG),
        ("FONTSIZE",    (0, 1), (-1, -1),  10),
        ("ALIGN",       (0, 1), (0, -1),   "LEFT"),
        ("ALIGN",       (1, 1), (-1, -1),  "RIGHT"),
        ("TOPPADDING",  (0, 0), (-1, -1),  4),
        ("BOTTOMPADDING",(0,0), (-1, -1),  4),
        ("LEFTPADDING", (0, 0), (-1, -1),  6),
        ("RIGHTPADDING",(0, 0), (-1, -1),  6),
        ("GRID",        (0, 0), (-1, -1),  0.4, C_BORDER),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C_WHITE, C_ROW_ALT]),
    ]
    return TableStyle(cmds)


# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 1: PDF de SLIDES (16:9, sin scripts)
# ═══════════════════════════════════════════════════════════════════════════════

SLIDE_W, SLIDE_H = 10 * inch, 5.625 * inch
SM = 0.52 * inch


def _slide_split_lines(text, font, size, max_w):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    words = text.split()
    lines, line = [], []
    for w in words:
        test = " ".join(line + [w])
        if stringWidth(test, font, size) <= max_w:
            line.append(w)
        else:
            if line:
                lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    return lines or [text]


def _slide_rect(c, x, y, w, h, fill):
    c.setFillColor(fill)
    c.setStrokeColor(fill)
    c.rect(x, y, w, h, fill=1, stroke=0)


def _slide_text(c, x, y, text, size, color, bold=False, align="left"):
    c.setFont(FONT_BOLD if bold else FONT_REG, size)
    c.setFillColor(color)
    if align == "center":
        c.drawCentredString(x, y, text)
    elif align == "right":
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)


def _slide_wrapped(c, x, y, width, text, size, color, bold=False, lh=None):
    font = FONT_BOLD if bold else FONT_REG
    lh = lh or size * 1.35
    for line in _slide_split_lines(text, font, size, width):
        _slide_text(c, x, y, line, size, color, bold=bold)
        y -= lh
    return y


def _slide_rich_wrapped(c, x, y, width, text, size, base_color, lh=None):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    lh = lh or size * 1.38
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    tokens = []
    for p in parts:
        if p.startswith("**") and p.endswith("**"):
            for w in p[2:-2].split():
                tokens.append((w, True))
        elif p:
            for w in p.split():
                tokens.append((w, False))
    if not tokens:
        return y
    lines, line, lw = [], [], 0.0
    for word, bold in tokens:
        font = FONT_BOLD if bold else FONT_REG
        sw = stringWidth(" ", font, size)
        ww = stringWidth(word, font, size)
        needed = (sw + ww) if line else ww
        if line and lw + needed > width:
            lines.append(line)
            line, lw = [(word, bold)], ww
        else:
            line.append((word, bold))
            lw += needed
    if line:
        lines.append(line)
    for line in lines:
        cx = x
        for k, (word, bold) in enumerate(line):
            font  = FONT_BOLD if bold else FONT_REG
            color = C_PRIMARY if bold else base_color
            c.setFont(font, size)
            c.setFillColor(color)
            if k > 0:
                prev_bold = line[k-1][1]
                cx += stringWidth(" ", FONT_BOLD if prev_bold else FONT_REG, size)
            c.drawString(cx, y, word)
            cx += stringWidth(word, font, size)
        y -= lh
    return y


def _strip_bold(text):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", text)


def _parse_table_lines(lines):
    headers, rows = [], []
    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            continue
        if re.match(r"^\|[-:\s|]+\|$", s):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not headers:
            headers = cells
        else:
            rows.append(cells)
    return headers, rows


def _draw_slide_table(c, x, y, width, min_y, headers, rows):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    n_cols = len(headers)
    col_w  = width / n_cols
    row_h  = 0.295 * inch
    hdr_h  = 0.315 * inch

    for ci, hdr in enumerate(headers):
        rx = x + ci * col_w
        ry = y - hdr_h
        _slide_rect(c, rx, ry, col_w, hdr_h, C_PRIMARY)
        if ci > 0:
            _slide_rect(c, rx, ry, 0.012, hdr_h, C_WHITE)
        c.setFont(FONT_BOLD, 10)
        c.setFillColor(C_WHITE)
        c.drawCentredString(rx + col_w / 2, ry + (hdr_h - 10) / 2, _strip_bold(hdr))
    y -= hdr_h

    for ri, row in enumerate(rows):
        if y - row_h < min_y:
            break
        bg = C_WHITE if ri % 2 == 0 else C_ROW_ALT
        for ci in range(n_cols):
            rx = x + ci * col_w
            ry = y - row_h
            _slide_rect(c, rx, ry, col_w, row_h, bg)
            val = row[ci] if ci < len(row) else ""
            is_b  = "**" in val
            label = _strip_bold(val)
            color = C_PRIMARY if is_b else C_DARK
            c.setFont(FONT_BOLD if is_b else FONT_REG, 10)
            c.setFillColor(color)
            pad = 0.1 * inch
            if ci == 0:
                c.drawString(rx + pad, ry + (row_h - 10) / 2, label)
            else:
                c.drawRightString(rx + col_w - pad, ry + (row_h - 10) / 2, label)
        y -= row_h

    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.4)
    tbl_h = hdr_h + row_h * min(len(rows), int((SLIDE_H * 0.76) / row_h))
    c.rect(x, y, width, tbl_h, fill=0, stroke=1)
    return y


def _trim(lines):
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return lines


def _parse_slides(md_path: Path) -> dict:
    lines = md_path.read_text(encoding="utf-8").split("\n")
    result = {"title": "", "subtitle": "", "meta": [], "slides": []}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# ") and "BLOQUE" not in line:
            result["title"] = line[2:].strip()
        elif line.startswith("## ") and "SLIDE" not in line and not line.startswith("### "):
            result["subtitle"] = line[3:].strip()
        elif re.match(r"^\*\*Duración\*\*|^\*\*Actualización|^\*\*Contenido", line):
            result["meta"].append(re.sub(r"\*\*", "", line).strip())
        elif re.match(r"^## SLIDE|^# BLOQUE", line):
            break
        i += 1

    current, in_visual, visual_lines = None, False, []

    def flush():
        nonlocal current, visual_lines
        if current is not None:
            current["content"] = _trim(visual_lines[:])
            result["slides"].append(current)
        current, visual_lines = None, []

    while i < len(lines):
        line = lines[i]
        if re.match(r"^# BLOQUE", line):
            flush()
            title = re.sub(r"\s*\{icon:[^}]+\}", "", line[2:]).strip()
            result["slides"].append({"type": "block", "title": title})
            in_visual = False
        elif re.match(r"^## SLIDE \d+:", line):
            flush()
            slide_title = re.sub(r"^## SLIDE \d+:\s*", "", line).strip()
            current = {"type": "content", "title": slide_title}
            in_visual = False
        elif line.startswith("### Contenido Visual"):
            in_visual = True
        elif line.startswith("### Script"):
            in_visual = False
        elif line.strip() == "---":
            pass
        elif in_visual and current is not None:
            visual_lines.append(line)
        i += 1

    flush()
    return result


def _draw_cover(c, title, subtitle, meta):
    _slide_rect(c, 0, 0, SLIDE_W, SLIDE_H, C_DARK)
    _slide_rect(c, SM, SLIDE_H * 0.28, 0.07 * inch, SLIDE_H * 0.44, C_PRIMARY)
    _slide_rect(c, 0, 0, SLIDE_W, 0.18 * inch, C_PRIMARY)

    y = SLIDE_H * 0.66
    for line in _slide_split_lines(title, FONT_BOLD, 26, SLIDE_W - SM * 2 - 0.3 * inch):
        _slide_text(c, SM + 0.25 * inch, y, line, 26, C_WHITE, bold=True)
        y -= 26 * 1.3

    y -= 0.1 * inch
    _slide_text(c, SM + 0.25 * inch, y, subtitle, 16, C_PRIMARY)
    y -= 16 * 1.5
    for line in meta:
        _slide_text(c, SM + 0.25 * inch, y, line, 11, C_MUTED)
        y -= 11 * 1.5


def _draw_block(c, title):
    _slide_rect(c, 0, 0, SLIDE_W, SLIDE_H, C_PRIMARY)
    _slide_rect(c, SLIDE_W * 0.35, SLIDE_H * 0.32, SLIDE_W * 0.30, 0.04 * inch, C_WHITE)
    lines = _slide_split_lines(title, FONT_BOLD, 22, SLIDE_W - SM * 2)
    total_h = len(lines) * 22 * 1.4
    y = (SLIDE_H + total_h) / 2 - 22 * 0.3
    for line in lines:
        _slide_text(c, SLIDE_W / 2, y, line, 22, C_WHITE, bold=True, align="center")
        y -= 22 * 1.4


def _draw_content_slide(c, title, content, num):
    _slide_rect(c, 0, 0, SLIDE_W, SLIDE_H, C_BG)
    _slide_rect(c, SM, SLIDE_H - 1.0 * inch, 0.07 * inch, 0.62 * inch, C_PRIMARY)
    _slide_rect(c, SM, SLIDE_H - 1.08 * inch, SLIDE_W - SM * 2, 0.025 * inch, C_BORDER)
    _slide_text(c, SLIDE_W - SM, 0.22 * inch, str(num), 9, C_MUTED, align="right")

    _slide_wrapped(c, SM + 0.22 * inch, SLIDE_H - 0.62 * inch,
                   SLIDE_W - SM * 2 - 0.3 * inch, _strip_bold(title), 20, C_DARK,
                   bold=True, lh=24)

    CT = SLIDE_H - 1.2 * inch
    CB = 0.38 * inch
    CL = SM
    CW = SLIDE_W - SM * 2

    table_idx = next((i for i, l in enumerate(content) if l.strip().startswith("|")), None)

    if table_idx is not None:
        pre   = _trim(content[:table_idx])
        tbl_l = []
        post  = []
        in_t  = True
        for line in content[table_idx:]:
            if in_t and line.strip().startswith("|"):
                tbl_l.append(line)
            else:
                in_t = False
                post.append(line)
        post = _trim(post)

        y = CT
        for line in pre:
            if line.strip() == "":
                y -= 6
                continue
            is_b = line.strip().startswith("-")
            txt  = line.strip().lstrip("- ").strip() if is_b else line.strip()
            y = _slide_rich_wrapped(c, CL, y, CW, ("• " if is_b else "") + txt, 13, C_DARK, lh=17)
            y -= 4

        y -= 6
        headers, rows = _parse_table_lines(tbl_l)
        if headers:
            y = _draw_slide_table(c, CL, y, CW, CB, headers, rows)

        y -= 8
        for line in _trim(post):
            if line.strip() == "" or y < CB:
                break
            is_b = line.strip().startswith("-")
            txt  = line.strip().lstrip("- ").strip() if is_b else line.strip()
            y = _slide_rich_wrapped(c, CL, y, CW, ("• " if is_b else "") + txt, 11, C_MUTED, lh=15)
            y -= 3
    else:
        y = CT
        for line in content:
            if y < CB:
                break
            if line.strip() == "":
                y -= 8
                continue
            is_b = line.strip().startswith("-")
            txt  = line.strip().lstrip("- ").strip() if is_b else line.strip()
            y = _slide_rich_wrapped(c, CL, y, CW, ("• " if is_b else "") + txt, 15, C_DARK, lh=20)
            y -= 6


def generate_slides_pdf(md_path: Path, out_path: Path):
    data = _parse_slides(md_path)
    c = Canvas(str(out_path), pagesize=(SLIDE_W, SLIDE_H))
    c.setTitle(data["title"])
    c.setAuthor("LCP Israel Castro")

    _draw_cover(c, data["title"], data["subtitle"], data["meta"])
    c.showPage()

    slide_num = 1
    for s in data["slides"]:
        if s["type"] == "block":
            _draw_block(c, s["title"])
        else:
            slide_num += 1
            _draw_content_slide(c, s["title"], s.get("content", []), slide_num)
        c.showPage()

    c.save()
    print(f"✓ {out_path.name}  ({1 + len(data['slides'])} páginas)")


# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 2: PDF de documentos Markdown (ejercicios, tablas)
# ═══════════════════════════════════════════════════════════════════════════════

def _header_footer(canvas, doc, title):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(C_PRIMARY)
    canvas.rect(doc.leftMargin, doc.height + doc.topMargin + 4 * mm,
                doc.width, 4, fill=1, stroke=0)
    # Footer
    canvas.setFont(FONT_REG, 8)
    canvas.setFillColor(C_MUTED)
    canvas.drawString(doc.leftMargin,
                      doc.bottomMargin - 12,
                      "Diplomado en Herramientas Prácticas ante la Autoridad Fiscal · Módulo 4 · Clase 1")
    canvas.drawRightString(doc.leftMargin + doc.width,
                           doc.bottomMargin - 12,
                           f"Pág. {canvas.getPageNumber()}")
    canvas.restoreState()


def md_to_flowables(md_text: str, styles: dict) -> list:
    """Convierte Markdown simplificado a flowables de ReportLab."""
    flowables = []
    lines = md_text.split("\n")
    i = 0
    in_code = False
    code_buf = []

    while i < len(lines):
        line = lines[i]

        # Bloque de código
        if line.strip().startswith("```"):
            if in_code:
                in_code = False
                code_text = "\n".join(code_buf)
                flowables.append(Paragraph(code_text.replace("\n", "<br/>"),
                                           styles["code"]))
                flowables.append(Spacer(1, 4))
                code_buf = []
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # Separador
        if line.strip() == "---":
            flowables.append(HRFlowable(width="100%", thickness=0.5,
                                         color=C_BORDER, spaceAfter=6, spaceBefore=6))
            i += 1
            continue

        # Headings
        if line.startswith("# "):
            flowables.append(Spacer(1, 6))
            flowables.append(Paragraph(_rich(line[2:].strip()), styles["h1"]))
            i += 1
            continue
        if line.startswith("## "):
            flowables.append(Paragraph(_rich(line[3:].strip()), styles["h2"]))
            i += 1
            continue
        if line.startswith("### "):
            flowables.append(Paragraph(_rich(line[4:].strip()), styles["h3"]))
            i += 1
            continue

        # Tabla Markdown
        if line.strip().startswith("|"):
            tbl_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            headers, rows = _parse_table_lines(tbl_lines)
            if headers:
                n_cols = len(headers)
                col_w  = (A4[0] - 3.4 * cm) / n_cols
                data   = [[Paragraph(_rich(_strip_bold(h)), ParagraphStyle(
                            "th", fontName=FONT_BOLD, fontSize=10,
                            textColor=C_WHITE, alignment=TA_CENTER))
                           for h in headers]]
                for row in rows:
                    data.append([
                        Paragraph(_rich(_strip_bold(row[ci] if ci < len(row) else "")),
                                  ParagraphStyle("td", fontName=FONT_REG, fontSize=10,
                                                 textColor=C_DARK,
                                                 alignment=TA_LEFT if ci == 0 else TA_RIGHT))
                        for ci in range(n_cols)
                    ])
                tbl = Table(data, colWidths=[col_w] * n_cols, repeatRows=1)
                tbl.setStyle(_tbl_style(len(data)))
                flowables.append(tbl)
                flowables.append(Spacer(1, 8))
            continue

        # Bullet
        if re.match(r"^[-*] ", line):
            txt = line[2:].strip()
            flowables.append(Paragraph("• " + _rich(txt), styles["bullet"]))
            i += 1
            continue

        # Subíndented bullet
        if re.match(r"^  [-*] ", line):
            txt = line[4:].strip()
            sub = ParagraphStyle("sub", parent=styles["bullet"],
                                 leftIndent=28, firstLineIndent=-10, fontSize=10)
            flowables.append(Paragraph("– " + _rich(txt), sub))
            i += 1
            continue

        # Blockquote / nota
        if line.startswith("> "):
            txt = line[2:].strip()
            flowables.append(Paragraph(_rich(txt), styles["note"]))
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # Línea en blanco
        if line.strip() == "":
            flowables.append(Spacer(1, 5))
            i += 1
            continue

        # Párrafo normal
        flowables.append(Paragraph(_rich(line.strip()), styles["body"]))
        i += 1

    return flowables


def generate_md_pdf(md_path: Path, out_path: Path, doc_title: str = ""):
    styles = _styles()

    def on_page(canvas, doc):
        _header_footer(canvas, doc, doc_title)

    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.8 * cm,
        title=doc_title or md_path.stem,
        author="LCP Israel Castro",
    )

    md_text = md_path.read_text(encoding="utf-8")
    flowables = md_to_flowables(md_text, styles)
    doc.build(flowables, onFirstPage=on_page, onLaterPages=on_page)
    print(f"✓ {out_path.name}")


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    here = Path(__file__).parent

    generate_slides_pdf(
        here / "slides-scripts.md",
        here / "slides-clase-01-modulo-04.pdf",
    )

    generate_md_pdf(
        here / "ejercicios-practicos.md",
        here / "ejercicios-practicos.pdf",
        "Ejercicios Prácticos · Clase 01 · Módulo 4",
    )

    generate_md_pdf(
        here / "tablas-comparativas.md",
        here / "tablas-comparativas.pdf",
        "Tablas Comparativas · Clase 01 · Módulo 4",
    )

    print("\n3 PDFs generados en", here)


if __name__ == "__main__":
    main()
