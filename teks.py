import os
import time
import random
import requests
from colorama import Fore, Style, init
import subprocess

# Inisialisasi colorama
init(autoreset=True)
def get_terminal_size():
    try:
        cols = int(subprocess.check_output(['tput', 'cols']))
        lines = int(subprocess.check_output(['tput', 'lines']))
        return cols, lines
    except Exception as e:
        print(f"Error getting terminal size: {e}")
        return None, None
def format_phone_number(phone_number):
    """Format nomor telepon untuk digunakan dalam link WhatsApp"""
    return phone_number.strip().replace(' ', '')

def create_whatsapp_link(phone_number, message):
    """Membuat link WhatsApp dari nomor telepon dan pesan"""
    return f"https://wa.me/{format_phone_number(phone_number)}?text={message}"

def load_user_agents(filename='user_agents.txt'):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []

def load_messages(filename='p.txt'):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []

def get_proxies():
    url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text'
    response = requests.get(url)
    proxies = response.text.splitlines()
    return proxies

def get_random_proxy(proxies):
    return random.choice(proxies) if proxies else None

def countdown(seconds):
    """Menampilkan hitung mundur"""
    for i in range(seconds, 0, -1):
        print(f"Menunggu {i} detik...", end='\r')
        time.sleep(1)
    print("Mulai membuka link...")

def open_whatsapp_link(number, text, proxy=None, countdown_time=5):
    link = create_whatsapp_link(number, text)
    user_agent = random.choice(user_agents) if user_agents else 'default-user-agent'
    print(f'Menggunakan proxy: {proxy}')
    print(f'Menggunakan User-Agent: {user_agent}')
    
    if proxy:
        os.environ['HTTP_PROXY'] = proxy
        os.environ['HTTPS_PROXY'] = proxy

    # Hitung mundur sebelum membuka link dengan waktu yang ditentukan
    countdown(countdown_time)  # Hitung mundur selama countdown_time detik

    os.system(f'am start -a android.intent.action.VIEW -d "{link}"')

def reduce_block_risk(min_wait_time, max_wait_time):
    wait_time = random.randint(min_wait_time, max_wait_time)
    # Menampilkan hitung mundur sebelum membuka link berikutnya
    for i in range(wait_time, 0, -1):
        print(f'Menunggu selama {i} detik sebelum membuka link berikutnya...', end='\r')
        time.sleep(1)
    print("Melanjutkan ke link berikutnya...")

    return wait_time

def shuffle_links_and_messages(numbers, messages):
    random.shuffle(numbers)
    random.shuffle(messages)
    return numbers, messages

def menu2():
    """Membuka link WhatsApp dengan proxy dan User-Agent acak"""
    global user_agents
    user_agents = load_user_agents()

    numbers_input = input("Masukkan nomor WhatsApp (pisahkan dengan koma): ")
    numbers = numbers_input.split(',')

    min_wait_time = int(input("Masukkan waktu jeda minimum (detik): "))
    max_wait_time = int(input("Masukkan waktu jeda maksimum (detik): "))

    messages = load_messages()  # Memuat pesan dari file p.txt

    proxies = get_proxies()
    numbers, messages = shuffle_links_and_messages(numbers, messages)

    for i, number in enumerate(numbers):
        if i >= len(messages):
            message = messages[-1]
        else:
            message = messages[i]

        proxy = get_random_proxy(proxies)
        # Menggunakan waktu jeda acak untuk hitung mundur
        wait_time = reduce_block_risk(min_wait_time, max_wait_time)
        open_whatsapp_link(number.strip(), message, proxy, countdown_time=wait_time)

    print('Selesai membuka semua link.')

# Jalankan menu2() untuk memulai
def menu1():
    """Ekstrak teks dari gambar menggunakan pytesseract"""
    img_path = input("Masukkan path gambar (misalnya /storage/emulated/0/randomnum/p.jpg): ")
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img)
    text_no_spaces = text.replace(" ", "").replace("\n", "").replace("-", "").replace("+", ",")
    print("Teks yang diekstrak tanpa spasi dan tanda +:")
    print(text_no_spaces)

def menu3():
    """Membuat file VCF kontak dari input pengguna"""
    input_contacts = input("Masukkan nomor kontak, pisahkan dengan koma (misal: 6285693672915,6285702068862,...): ")
    base_name = input("Masukkan nama dasar untuk kontak (misal: Contact): ")
    output_filename = input("Masukkan nama file output (misal: hasil.vcf): ")
    contacts = input_contacts.split(',')

    if contacts:
        with open(output_filename, "w") as file:
            for index, contact in enumerate(contacts, start=1):
                file.write("BEGIN:VCARD\n")
                file.write("VERSION:3.0\n")
                file.write(f"N:;{base_name} {index};;;\n")
                file.write(f"FN:{base_name} {index}\n")
                file.write(f"TEL;TYPE=CELL:{contact.strip()}\n")
                file.write("END:VCARD\n")
        print(f"Kontak telah disimpan dalam file '{output_filename}'")
    else:
        print("Tidak ada kontak yang dimasukkan.")
import random
import time

def generate_user_agent():
    platforms = ["Windows NT 10.0", "Windows NT 11.0", "Linux x86_64", "Macintosh; Intel Mac OS X 10_15_7", "Macintosh; Intel Mac OS X 11_0_1", "Macintosh; Intel Mac OS X 12_0", "iPhone; CPU iPhone OS 15_1 like Mac OS X", "iPhone; CPU iPhone OS 16_0 like Mac OS X", "Android 12; Pixel 6 Pro", "Android 13; Pixel 7 Pro", "iPad; CPU OS 15_1 like Mac OS X", "iPad; CPU OS 16_0 like Mac OS X", "BlackBerry; BlackBerry 10.3.3", "SymbianOS/9.4; Series60/5.0 Nokia5800", "Meego 1.2 Harmattan", "Tizen 3.0", "Tizen 4.0"]
    browsers = ["Chrome/103.0.5060.114", "Chrome/104.0.5112.81", "Firefox/102.0", "Firefox/103.0", "Safari/605.1.15", "Safari/606.1.56", "Edge/103.0.1264.62", "Edge/104.0.1293.54", "Opera/89.0.4447.83", "Opera/90.0.4480.54", "OPR/75.0.3969.271", "OPR/76.0.4017.107", "UCBrowser/13.4.2.184", "UCBrowser/14.0.0.215", "Mobile Safari/604.1", "Mobile Safari/605.1", "CriOS/103.0.5060.114", "CriOS/104.0.5112.81", "FxiOS/102.0", "FxiOS/103.0"]
    versions = ["10.0", "10.1", "10.2", "10.3", "11.0", "11.1", "11.2", "11.3", "12.0", "12.1", "12.2", "12.3", "13.0", "13.1", "13.2", "13.3", "14.0", "14.1", "14.2", "14.3", "15.0", "15.1", "15.2", "15.3", "16.0", "16.1", "16.2", "16.3"]
    devices = ["x64", "x86", "arm64", "iPhone10,4", "iPhone11,8", "iPhone12,1", "iPhone13,2", "iPhone14,5", "Nexus 5", "Nexus 6P", "Galaxy S10", "Galaxy S22", "Galaxy Note 20", "Galaxy Z Fold3", "Pixel 5", "Pixel 6", "Pixel 6 Pro", "Pixel 7", "Pixel 7 Pro", "iPad7,4", "iPad8,3", "iPad9,7", "iPad10,2", "BlackBerry 9900", "BlackBerry Z10", "Meego 1.2 Harmattan", "Tizen 2.3 TV", "Tizen 4.0 TV"]
    engine_versions = ["537.36", "603.2.4", "602.1", "14.14393", "605.1.15", "606.1.56", "608.1.25", "611.1.22", "612.1.16", "613.1.30", "604.1.38", "538.1"]

    platform = random.choice(platforms)
    browser = random.choice(browsers)
    version = random.choice(versions)
    device = random.choice(devices)
    engine_version = random.choice(engine_versions)

    if platform == "iPhone; CPU iPhone OS 15_1 like Mac OS X" or platform == "iPhone; CPU iPhone OS 16_0 like Mac OS X" or platform == "Android 12; Pixel 6 Pro" or platform == "Android 13; Pixel 7 Pro" or platform == "iPad; CPU OS 15_1 like Mac OS X" or platform == "iPad; CPU OS 16_0 like Mac OS X":
        user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/{version} Mobile/{device} Safari/604.1"
    elif platform == "BlackBerry; BlackBerry 10.3.3" or platform == "SymbianOS/9.4; Series60/5.0 Nokia5800" or platform == "Meego 1.2 Harmattan" or platform == "Tizen 3.0" or platform == "Tizen 4.0":
        user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/538.1 (KHTML, like Gecko) Version/{version} Mobile Safari/538.1"
    else:
        user_agent = f"Mozilla/5.0 ({platform}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) {browser} Safari/{engine_version}"

    return user_agent

def menu4():
    """Membuat file user agents dari input pengguna"""
    num_user_agents = int(input("Berapa banyak user agent yang ingin dibuat? "))
    output_filename = input("Masukkan nama file output (misal: user_agents.txt): ")
    
    with open(output_filename, "w") as file:
        for _ in range(num_user_agents):
            user_agent = generate_user_agent()
            file.write(user_agent + "\n")
            time.sleep(random.uniform(0.0, 0.0))  # Tunda antara 0.1 hingga 0.2 detik
    print(f"{num_user_agents} user agents tersimpan di '{output_filename}'")

def main_program():
    """Menampilkan menu utama dan mengarahkan ke fungsi yang sesuai berdasarkan pilihan pengguna"""

    print(Fore.RED + Style.BRIGHT +  """       .                                 
        ...        .     :.             
  ..:: .@@8;;8.     8 8 8 8St;%.  .  .  
 :X8:t%X8 8@S88%.;;;;:t;%8S 8S8: ::   . 
 ;8t8;:   88S%: t8888888@%88S88S:...    
 :8   8 : X8@88888888t %@888X 8888.. .: 
 ;8:    888@S888  %@t88  .    S;. 8: .  
 ..%   S8%8X@888X   ;%  8@t%8S8 :t%@ %; 
   8X888S8S %SX88@X:S888S ;8%S@8 .8  8@ 
  88 X88  ..8SX8tX888S 88tt8S  8St.8 S%.
 :@8..88  .:88  8X88%888XX8S;  t@ %;8 t 
 @S8;8%8.;%S88%S8SS88 888888888 SX;t% X 
 :S888t8tX8 8@S8888 S888X   S8St8 88Xt8S
   888 8X8XSt88S8X8:88Xtt88 t88X8%8 8  :
   888 88SX888SS.88:8%X 8888S%@8  88; 8t
 X%S 88%8X@%tX88888;88 X 8X8@88XS.tS8 @ 
    %@XS8S888 888  S8X%8@;  888S8 8888  
  8%888888888t8888 8S%@X;% .8888S;S %8% 
   8 S   8888 :t  XX8 @:: t8%  ::t8@88t 
  .:S 8X. %%8     8   t. 8  % 8.. 8 .;  
  . :8 X@  X888888@@  @8X%%88t.@88      
    ;@8S888; % @8888888888888888X%      
  .  %t :8SS8X..;;8X S@X:8X8SX88:.    . 
        t: 8@888888@8888888XS :.  .     
   .    . ..%% %;@8X @@t%....   .  .  . .""")
    print(Fore.CYAN + Style.BRIGHT + "ミ☞𝙿 𝙸 𝙻 𝙸 𝙷 𝙼 𝙴 𝙽 𝚄 𝙽 𝚈 𝙰:")
    print(Fore.YELLOW + Style.BRIGHT + "1. MEMBUAT LINK WHATSAPP")
    print(Fore.MAGENTA + Style.BRIGHT + "2. MENYALIN TEKS DARI GAMBAR")
    print(Fore.BLUE + Style.BRIGHT + "3. MEMBUAT FILE VCF KONTAK")
    print(Fore.GREEN + Style.BRIGHT + " 4. MEMBUAT USER AGENT RANDOM")
    
    choice = input("Masukkan pilihan (1, 2, atau 3): ")
    
    if choice == '1':
        menu2()
    elif choice == '2':
        menu1()
    elif choice == '3':
        menu3()
    elif choice == '4':
        menu4()    
    else:
        print("Pilihan tidak valid!")

def check_terminal_size(min_cols=1, min_lines=1):
    cols, lines = get_terminal_size()
    if cols is not None and lines is not None:
        if cols > min_cols and lines > min_lines:
            main_program()
        else:
            print(Fore.RED + "UKURAN LAYAR KURANG BESAR,SILAHKAN CUBIT LAYARNYA")
            print(Fore.RED + "UKURAN LAYAR KURANG BESAR,SILAHKAN CUBIT LAYARNYA")
            print(Fore.RED + "UKURAN LAYAR KURANG BESAR,SILAHKAN CUBIT LAYARNYA")
    else:
        print("Tidak dapat memeriksa ukuran layar.")

if __name__ == "__main__":
    check_terminal_size()
