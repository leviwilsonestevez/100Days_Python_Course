import os

home: str = os.getenv("HOMEPATH")

print(os.environ.get('API_KEY_ALPHA_VANTAGE'))
print("-", "-", "-", sep=" ", end="!\n")
for key in os.environ:
    print(key, os.environ[key], sep=" ")
