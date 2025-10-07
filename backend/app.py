# app.py
# Example app with a hardcoded secret (bad practice)
SECRET_KEY = "supersecret_test_key_ABC123DEF456"   # hardcoded secret - gitleaks will flag
DB_PASSWORD = "P@ssw0rd!notreal"                   # hardcoded DB password

def main():
    print("Secret Key length:", len(SECRET_KEY))
    # Pretend to connect to DB using DB_PASSWORD (don't actually do this)

if __name__ == "__main__":
    main()
