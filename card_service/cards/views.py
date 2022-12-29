from django.shortcuts import render, redirect
from django.db.models import Q
import random
import datetime
from .forms import GenerateForm, InfoForm
from .models import Card, Info


def main(request):
    data = {}
    if request.method == 'POST':
        form = GenerateForm(request.POST)

        if form.is_valid():
            ser = request.POST.get('seria')
            col = request.POST.get('col')

            data = {
                'seria': ser,
                'col': col,
            }

            gen = f"generate/{ser}/{col}/"
            return redirect(gen)
    else:
        form = GenerateForm()

    return render(request, "main.html", context=data)


def generate(request, ser, col):
    seria = []
    nomer = []
    date_start = []
    date_end = []
    summa = []
    srok = []
    status = []

    for i in range(col):
        seria.append(ser)
        num = random.randint(100000000000, 999999999999)
        nomer.append(num)
        dst = datetime.datetime.now()
        date_start.append(str(dst)[:-10])
        delta = random.randint(30, 366)
        dlt = dst + datetime.timedelta(delta)
        date_end.append(str(dlt)[:-10])
        sum = random.randint(1000, 1000000)
        summa.append(sum)
        srk = random.randint(0, 2)
        sts = random.randint(0, 1)
        srok_dict = {0: '1 год', 1: '6 месяцев', 2: '1 месяц'}
        status_dict = {0: 'неактивно', 1: 'активно', 2: 'просрочено'}
        sr = srok_dict[srk]
        st = status_dict[sts]
        srok.append(sr)
        status.append(st)

        card = Card(seria=ser,
                    nomer=num,
                    date_start=dst,
                    date_end=dlt,
                    summa=sum,
                    srok=sr,
                    status=st)
        card.save()

    cards = {
        'seria': seria,
        'nomer': nomer,
        'date_start': date_start,
        'date_end': date_end,
        'summa': summa,
        'srok': srok,
        'status': status,
    }

    return render(request, "generate.html", context=cards)


def rnd(request):
    count = Card.objects.all().count()
    first = Card.objects.order_by('id').first()
    last = Card.objects.order_by('id').last()

    ch_list = []
    vl_list = []
    ci_list = []

    for i in range(count * 3):
        change = random.randint(0, 1)
        value = random.randint(10, 1000)
        card_id = random.randint(first.id, last.id)
        change_dir = {0: 'поступление', 1: 'списание'}
        change = change_dir[change]

        ch_list.append(change)
        vl_list.append(value)
        ci_list.append(card_id)

        info = Info(change=change,
                    value=value,
                    card_id=card_id)
        info.save()

        card_data = {
            'ch_list': ch_list,
            'vl_list': vl_list,
            'ci_list': ci_list
        }

    return render(request, 'rnd.html', context=card_data)


def list(request):
    card_list = Card.objects.all()
    seria = []
    nomer = []
    date_start = []
    date_end = []
    status = []
    for item in card_list:
        seria.append(item.seria)
        nomer.append(item.nomer)
        date_start.append(item.date_start)
        date_end.append(item.date_end)
        status.append(item.status)
    cards = {
        'seria': seria,
        'nomer': nomer,
        'date_start': date_start,
        'date_end': date_end,
        'status': status,
    }
    return render(request, 'list.html', context=cards)


def info(request, context=None):
    data = {}
    if request.method == 'POST':
        form = InfoForm(request.POST)

        if form.is_valid():
            ser = request.POST.get('seria')
            nmr = request.POST.get('nomer')

            if Card.objects.filter(seria__contains=ser) and Card.objects.filter(nomer__contains=nmr):
                card = Card.objects.filter(
                    seria__contains=ser).filter(nomer__contains=nmr)
                data = func(card)
            else:
                data = {'text': 'Карта с такой серией и номером отсутствует!'}

    else:
        form = InfoForm()
    return render(request, 'info.html', context=data)


def balance(request, id_card):
    infos = Info.objects.filter(card_id=id_card)
    list = []
    for item in infos:
        list.append(item)
    if list != []:
        data = {'list': list}
    else:
        data = {'error': 'Нет действий по карте'}
    return render(request, 'info.html', context=data)


def status(request, id_card):
    card = Card.objects.filter(id=id_card)
    card = card[0].status
    if card == 'неактивно':
        card = Card.objects.filter(id=id_card).update(status='активно')
    else:
        card = Card.objects.filter(id=id_card).update(status='неактивно')
    card = Card.objects.filter(id=id_card)
    data = func(card)
    return render(request, 'info.html', context=data)


def func(card):
    ser = card[0].seria
    nmr = card[0].nomer
    dts = card[0].date_start
    dte = card[0].date_end
    sum = card[0].summa
    srk = card[0].srok
    sts = card[0].status
    id = card[0].id
    data = {
        'seria': ser,
        'nomer': nmr,
        'dts': dts,
        'dte': dte,
        'sum': sum,
        'srk': srk,
        'sts': sts,
        'card_id': id,
    }
    return data


def delete(request, id_card):
    Card.objects.filter(id=id_card).delete()
    data = {'error': f"Карта с ID={id_card} удалена!"}
    return render(request, 'info.html', context=data)
