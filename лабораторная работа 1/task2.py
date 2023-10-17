# TODO Найдите количество книг, которое можно разместить на дискете
DISK_VOLUME = 1.44
PAGES = 100
LINES = 50
SYMBOLS = 25
BYTES = 4
book_amount = round(DISK_VOLUME // (PAGES * LINES * SYMBOLS * BYTES / 1024 / 1024))
print("Количество книг, помещающихся на дискету:", book_amount)
