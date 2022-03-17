from solid.tell_dont_ask.models.user import User


def update_wallet_view(request, amount=100000):
    try:
        user = User.objects.get(pk=1)
    except User.DoesNotExists:
        raise Exception("User Does Not Exists")
    user.increase_wallet(amount=amount)
