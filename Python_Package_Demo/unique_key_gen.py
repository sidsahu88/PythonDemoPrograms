import random

def generate_unique_key(characters, length):
    """Generate a unique key of specified length from given characters."""
    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    key_length = 12
    unique_key = generate_unique_key(chars, key_length)
    print(f'Generated Unique Key: {unique_key}')