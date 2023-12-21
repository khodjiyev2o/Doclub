import random
import string


def randomize_certificate_number():
    from .models import Certificate

    cids = Certificate.objects.values_list("cid", flat=True)
    while True:
        random_cid = "".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(7))
        if random_cid not in cids:
            return random_cid
