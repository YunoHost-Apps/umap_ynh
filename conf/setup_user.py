def setup_project_user(user):
        print(user.username)
        if ',' in user.username:
                user.username = user.username.split(',')[0].strip()

        if not user.email:
                user.email = f"{user.username}@localhost"

        user.is_staff = True
        user.save(update_fields=['is_staff'])
        return user
