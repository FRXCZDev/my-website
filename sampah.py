import os
import threading

# Kode ANSI untuk warna yang lebih cerah
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
RESET = "\033[0m"

def open_telegram_link():
    link = "https://t.me/+q_Aa7xYY8C8yMGM1"
    os.system(f"am start -a android.intent.action.VIEW -d {link}")
    print(f"{BRIGHT_GREEN}MENCARI FILE SAMPAH......") 
    print(f"{BRIGHT_GREEN}SEARCH FILE JUNK FILE .....") 
     

def find_junk_files(directory, extensions):
    junk_files = []
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                junk_files.append((file_path, file_size))
                total_size += file_size
    return junk_files, total_size

def delete_file(file_path, file_size):
    try:
        os.remove(file_path)
        print(f"{BRIGHT_GREEN}Deleted: {file_path} - Size: {file_size / 1024:.2f} KB{RESET}")
    except Exception as e:
        print(f"{BRIGHT_RED}Failed to delete: {file_path} - {e}{RESET}")

def delete_files(file_paths):
    threads = []
    for file_path, file_size in file_paths:
        thread = threading.Thread(target=delete_file, args=(file_path, file_size))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    storage_path = "/storage/emulated/0"
    junk_extensions = ('.log', '.tmp', '.cache', '.bak', '.crdownload', '.swp', '.dat', '.gif')
    junk_files, total_size = find_junk_files(storage_path, junk_extensions)
    
    if junk_files:
        print(f"{BRIGHT_YELLOW}\n--- Found Junk Files ---{RESET}")
        for junk_file, file_size in junk_files:
            print(f"{BRIGHT_RED}{junk_file} - Size: {file_size / 1024:.2f} KB{RESET}")
        print(f"\n{BRIGHT_GREEN}ENGLISH LANGUAGE : Total size of junk files: {total_size / (1024 * 1024):.2f} MB{RESET}\n{BRIGHT_GREEN}BAHASA INDONESIA : Ukuran Total File Sampah : {total_size / (1024 * 1024):.2f} MB{RESET}")
        print(f"{BRIGHT_YELLOW}ENGLISH LANGUAGE : Do You Want To Delete These Files? (Yes/No):{RESET}")
        confirmation = input(f"{BRIGHT_YELLOW}BAHASA INDONESIA : Apakah Anda Yakin Ingin Menghapus FileNya? (Yes/No): {RESET}")
        
        if confirmation.lower() == 'yes':
            delete_files(junk_files)
            print(f"\n{BRIGHT_GREEN}All selected junk files have been deleted.{RESET}")
        else:
            print(f"\n{BRIGHT_RED}Deletion aborted by user.{RESET}")
    else:
        print(f"{BRIGHT_YELLOW}\nNo junk files found.{RESET}")

if __name__ == "__main__":
    open_telegram_link()
    main()
