# -*- coding: utf-8 -*-
import zipfile, re
DOC = r"d:\文件\工作 作业\深度学习\期末\考试报告-.docx"
with zipfile.ZipFile(DOC) as z:
    xml = z.read("word/document.xml").decode("utf-8")
rows = re.findall(r"<w:tr\b.*?</w:tr>", xml, re.DOTALL)
for ri, r in enumerate(rows):
    cells = re.findall(r"<w:tc\b.*?</w:tc>", r, re.DOTALL)
    print(f"\n=== Row {ri} ===")
    for ci, c in enumerate(cells):
        texts = re.findall(r"<w:t[^>]*>([^<]*)</w:t>", c)
        text = "".join(texts)
        print(f"  C{ci}: {text}")
        print("  ---")
