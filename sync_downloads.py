# -*- coding: utf-8 -*-
"""Синхронизация downloads лендинга ОУД4 из ОУД/обработка."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "обработка"
DST = ROOT / "downloads"

COPIES = [
    ("01-Вопросы-к-команде-и-заказчику.docx", "01-Вопросы-к-команде-и-заказчику.docx"),
    ("02-Что-нужно-сделать-по-проекту-OUD.docx", "02-Что-нужно-сделать-по-проекту-OUD.docx"),
    ("03-Опросный-лист-ОУД4-v4.7-заполненный.docx", "03-Опросный-лист-ОУД4-v4.7-заполненный.docx"),
    ("04-Опросный-лист-РАДКОП-v1.3-заполненный.docx", "04-Опросный-лист-РАДКОП-v1.3-заполненный.docx"),
    ("05-План-действий-OUD.xlsx", "05-План-действий-OUD.xlsx"),
    ("пакет-ОУД4.zip", "пакет-свидетельств-ОУД4.zip"),
]


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    for src_name, dst_name in COPIES:
        src = SRC / src_name
        if src.exists():
            shutil.copy2(src, DST / dst_name)
            print("OK", dst_name)
        else:
            print("SKIP", src_name)
    for f in SRC.glob("*15408*.docx"):
        shutil.copy2(f, DST / "00-Роадмап-ОУД4-ГОСТ-15408.docx")
        print("OK", "00-Роадмап-ОУД4-ГОСТ-15408.docx")
        break
    print("Done:", DST)


if __name__ == "__main__":
    main()
