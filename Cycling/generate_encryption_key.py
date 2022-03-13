import os
import base64

def generate():
    random_bytes = os.urandom(32)
    new_key = base64.urlsafe_b64encode(random_bytes)
    print(new_key)

if __name__ == "__main__":
    generate()
