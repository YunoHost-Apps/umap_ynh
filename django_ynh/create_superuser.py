#!/usr/bin/env python3

"""
    Can be called e.g.:

        poetry run create_superuser --ds="foo.settings" --username="bar" \
            --email="foo@bar.tld" --password="no-password"

    or, e.g.:

        python3 -m django_ynh.create_superuser --ds="foo.settings" --username="bar" \
            --email="foo@bar.tld" \
            --password="no-password"
"""

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description='Create or update Django super user.')
    parser.add_argument('--ds', help='The "DJANGO_SETTINGS_MODULE" string')
    parser.add_argument('--username')
    parser.add_argument('--email')
    parser.add_argument('--password')

    args = parser.parse_args()

    os.environ['DJANGO_SETTINGS_MODULE'] = args.ds

    username = args.username
    email = args.email or ''
    password = args.password

    import django

    django.setup()

    from django.contrib.auth import get_user_model

    User = get_user_model()
    user = User.objects.filter(username=username).first()
    if user:
        print(f'Update existing user "{user}" and set his password.', file=sys.stderr)
        print(repr(password))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.email = email
        user.save()
    else:
        print(f'Create new super user "{username}"', file=sys.stderr)
        User.objects.create_superuser(username=username, email=email, password=password)


if __name__ == '__main__':
    main()
