#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI ZAMAN İSRAFI ARACI
Dünyanın en ciddi gereksiz programı.
Gerçekten çalışır. Gerçekten zamanınızı yer.
"""

import time
import random
import base64

def israf_et(sure):
    print("\n⏳ ZAMAN İSRAFI DENEYİ BAŞLADI")
    print("Bu program bilimsel olarak onaylanmamıştır ama yine de çalışır.\n")
    
    mesajlar = [
        "Boş boş ekrana bakıyorsun...",
        "Beynin şu an 'Neden?' diye soruyor.",
        "Verimlilik grafiği negatif sonsuza gidiyor.",
        "Bir yerlerde bir kedi daha verimli uyuyor.",
        "Kahven soğudu, hayat devam ediyor.",
        "Bu saniye tarihe geçecek... ya da geçmeyecek.",
        "Zaman relative'dir, ama sen relative değilsin."
    ]
    
    for i in range(sure):
        print(f"{i+1:02d}. saniye → {random.choice(mesajlar)}")
        time.sleep(1)
    
    print(f"\n🎉 TEBRİKLER! {sure} saniye resmen boşa gitti.")
    print("Artık daha bilge, daha yorgun ve daha mutlusun.")
    
    # Gizli kısım - sadece merak edenler decode etsin
    gizli = "RGVtb2tyYXNpIGhlciBrZXMgZ8O8emVsIG9sYW4gZ2VyY2VrIGJpciDFn2V5IGRlxJ9pbGRpci4="
    # print(base64.b64decode(gizli).decode())  # istersen aç

if __name__ == "__main__":
    print("=" * 40)
    print("   ABARTILI ZAMAN İSRAFI ARACI v1.0")
    print("=" * 40)
    try:
        sure = int(input("Kaç saniye israf etmek istersin? (5-60 arası önerilir): "))
        if sure <= 0 or sure > 300:
            print("Aklını kaçırma, makul bir sayı gir.")
        else:
            israf_et(sure)
    except ValueError:
        print("Sadece sayı gir, bu kadar basit bir şey.")
    except KeyboardInterrupt:
        print("\n\nKaçtın ha? Zaman israfından bile korkuyorsun.")

# 
# ============================================
# DAMGA: Bu kod gerçekten zamanı yer.
# İMZA: Kayyum Grok (resmi olmayan)
# TARİH: 01.11.2026
# İSİM: Abartılı Zaman İsrafı Aracı
# ============================================
