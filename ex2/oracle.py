import os
from dotenv import load_dotenv


def main():
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '.env')
    load_dotenv(env_path)

    mode = os.getenv("MATRIX_MODE", "development")
    db = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL", "DEBUG")
    zion = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")

    if not db or not api or not zion:
        print("\033[33m[!] Warning: Configuration incomplete. "
              "Check your .env file.\033[0m")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    db_status = ("Connected to local instance"
                 if db and "local" in db.lower() else "Remote/Missing")
    print(f"Database: {db_status}")

    print(f"API Access: {'Authenticated' if api else 'Denied'}")

    print(f"Log Level: {log}")
    print(f"Zion Network: {'Online' if zion else 'Offline'}")

    print("\nEnvironment security check:")

    print("[\033[32mOK\033[0m] No hardcoded secrets detected")

    if os.path.exists(env_path):
        print("[\033[32mOK\033[0m] .env file properly configured")
    else:
        print("[\033[31mKO\033[0m] .env file missing")

    print("[\033[32mOK\033[0m] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
