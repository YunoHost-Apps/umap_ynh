import logging

def setup_project_user(user):
    """
    Hook called by django_yunohost_integration after SSO login.
    """
    
    # 1. FIX: Handle the double username issue ('user,user') from my logs
    if ',' in user.username:
        user.username = user.username.split(',')[0].strip()

    # 2. FIX: Ensure the user has an email (in case uMap requires it, passing a dummy value if not passed correctly)
    if not user.email:
        user.email = f"{user.username}@localhost"

    # 3. Grant Staff status ONLY to admin user from manifest 
    if user.username == '__ADMIN__':
        user.is_staff = True
        user.is_superuser = True

    user.save()
    return user
