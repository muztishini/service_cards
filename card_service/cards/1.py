import random
# from .models import Info
from card_service.cards.models import Info

for i in range(30):
    change = random.randint(0, 1)
    value = random.randint(10, 1000)
    card_id = random.randint(29, 38)
    change_dir = {0: 'поступление', 1: 'списание'}
    change = change_dir[change]

    info = Info(change=change,
                value=value,
                card_id=card_id)
    info.save()

    print("{3}. change = {0}, value = {1}, card_id = {2}".format(change, value, card_id, i))
