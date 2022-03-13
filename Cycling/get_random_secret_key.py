from django.core.management.utils import get_random_secret_key

import os, base64

def main():
    secret_key = get_random_secret_key()
    secret_key_text = 'SECRET_KEY = \'{0}\'\n'.format(secret_key)

    random_bytes = os.urandom(32)
    encryption_key = base64.urlsafe_b64encode(random_bytes)
    field_encryption_key_text = 'FIELD_ENCRYPTION_KEY = {0}'.format(encryption_key)

    with open('local_settings_tmp.py', 'w') as f:
        f.writelines([secret_key_text, field_encryption_key_text])

if __name__ == '__main__':
    main()
