def horspool(metin, kelime):
    m = len(kelime)
    n = len(metin)
    if m > n:
        return 0
    geç = {}
    for k in range(m):
        geç[kelime[k]] = m - k - 1
    sayi = 0
    i = m - 1
    while i < n:
        j = m - 1
        while metin[i] == kelime[j]:
            if j == 0:
                sayi += 1
                break
            i -= 1
            j -= 1
        i += geç.get(metin[i], m)
    return sayi

# Kelimeleri aradığımız metin buraya yazılacak
metin = "ALICE'S ADVENTURES IN WONDERLAND....."

# Aranacak kelimeler
kelimeler = ["upon", "sigh", "Dormouse", "jury-box", "swim"]

# Horspool algoritması kullanarak kelimelerin sayısını bulma
for kelime in kelimeler:
    sayi = horspool(metin.lower(), kelime.lower())
    print(f"{kelime} kelimesi {sayi} kez geçmektedir.")
