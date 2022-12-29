import random
import datetime

seria = []
nomer = []
date_start = []
date_end = []
summa = []
srok = []
status = []

for i in range(10):
    seria.append(2202)
    nomer.append(random.randint(100000000000, 999999999999))
    dst = datetime.datetime.now()
    date_start.append(str(dst))
    delta = random.randint(30, 366)
    dlt = dst + datetime.timedelta(delta)
    date_end.append(str(dlt))
    summa.append(random.randint(1000, 1000000))
    srk = random.randint(0, 2)
    sts = random.randint(0, 1)
    srok_dict = {0: '1 год', 1: '6 месяцев', 2: '1 месяц'}
    status_dict = {0: 'неактивно', 1: 'активно', 2: 'просрочено'}
    srok.append(srok_dict[srk])
    status.append(status_dict[sts])

cards = {
    'seria': seria,
    'nomer': nomer,
    'date_start': date_start,
    'date_end': date_end,
    'summa': summa,
    'srok': srok,
    'status': status,
}

print("-------------------------------------")
print(cards)
print("-------------------------------------")


