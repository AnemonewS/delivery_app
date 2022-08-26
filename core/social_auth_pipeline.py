from customer.models import CustomerProfile, DriverProfile


def save_profile(backend, user, response, *args, **kwargs):
    request = backend.strategy.request_data()

    if backend.name == 'facebook':
        avatar = 'https://graph.facebook.com/%s/picture?type=large' % response['id']

        if request['user_type'] == 'driver':
            DriverProfile.objects.get_or_create(user_id=user.id, avatar=avatar)

        elif request['user_type'] == 'customer':
            CustomerProfile.objects.get_or_create(user_id=user.id, avatar=avatar)
