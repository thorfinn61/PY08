import sys
import os
import site


def construct():
    GREEN = "\033[32m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    in_venv = sys.prefix != sys.base_prefix

    if not in_venv:
        print(f"{BOLD}MATRIX STATUS: {RESET}"
              f"{RED}You're still plugged in{RESET}")
        print(f"{BLUE}Current Python:{RESET} {sys.executable}")
        print(f"{BLUE}Virtual Environment:{RESET} None detected")

        msg_warn = f"\n{RED}{BOLD}WARNING:{RESET} You're in the global env!"
        print(msg_warn)
        print("The machines can see everything you install.")

        print(f"\n{BOLD}To enter the construct, run:{RESET}")
        print(f"{GREEN}python3 -m venv matrix_env{RESET}")
        print(f"{GREEN}source matrix_env/bin/activate{RESET}  # On Unix")
        print(r"matrix_env\Scripts\activate     # On Windows")
        print("\nThen run this program again.")

    else:
        env_name = os.path.basename(sys.prefix)
        pkg_path = site.getsitepackages()[0]

        print(f"{BOLD}MATRIX STATUS:{RESET}"
              f"{GREEN}Welcome to the construct{RESET}")
        print(f"{BLUE}Current Python:{RESET} {sys.executable}")
        print(f"{BLUE}Virtual Environment:{RESET} {BOLD}{env_name}{RESET}")
        print(f"{BLUE}Environment Path:{RESET} {sys.prefix}")

        succ = f"\n{GREEN}{BOLD}SUCCESS:{RESET} You're in an isolated env!"
        print(succ)
        print("Safe to install packages without affecting")
        print("the global system.")

        print(f"\n{BOLD}Package installation path:{RESET}")
        print(f"{pkg_path}")


if __name__ == "__main__":
    construct()
