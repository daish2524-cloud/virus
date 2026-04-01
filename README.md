# 💀 HARDCOR RANSOMWARE v4.0 - Penetration Testing Simulator 💀

![Ransomware Demo](https://via.placeholder.com/1200x600/000000/FF0000?text=💀+HARDCOR+RANSOMWARE+v4.0)
*Professional ransomware simulation for authorized penetration testing*

*This is a code that i created because i was bored*

## 📋 Overview

**HARDCOR RANSOMWARE v4.0** is a **fully-functional ransomware simulator** designed for **authorized penetration testing** and **red team exercises**. This tool simulates real-world ransomware behavior including:

- 🔒 Fullscreen lockout with matrix-style visual effects
- 🔊 Audio torture (continuous error sounds + beeps)
- 🖱️ Mouse/keyboard hijacking
- 🌐 Browser tab flooding (100+ tabs)
- 📁 File encryption simulation (creates .CRYPTO copies)
- 🔔 Windows notification spam
- 💻 CMD window flooding
- 🛡️ Task Manager killer

> **⚠️ CRITICAL: AUTHORIZED USE ONLY ⚠️**

## 🎓 Educational Purposes Only

```
This code is for EDUCATIONAL PURPOSES and created by Dairon
I have permission and am authorized to perform this pentest
```

## 🛠️ System Requirements

| Requirement | Version |
|-------------|---------|
| **OS** | Windows 10/11 (x64) |
| **Python** | 3.6+ (tested on 3.11) |
| **Dependencies** | **NONE** - Pure Python stdlib |
| **Permissions** | Administrator recommended |

## 🚀 Installation (2 Minutes)

```bash
# 1. Save code as ransomware.py
# 2. NO INSTALL REQUIRED - Pure Python!
# 3. Run directly:
python ransomware.py
```

**That's it!** No pip installs, no external dependencies.

## 🎮 Usage Guide

### 1. **Launch Test Mode**
```bash
python ransomware.py
# Prompt: LAUNCH APOCALYPSE? (y/n): 
# Enter 'n' for safe demo
```

### 2. **Full Apocalypse Mode**
```
LAUNCH APOCALYPSE? (y/n): y
```
**Password: `8846`**

![Demo Flow](https://via.placeholder.com/800x400/1a1a1a/00FF00?text=1.+Launch+-+2.+Watch+Chaos+-+3.+Enter+8846)

### 3. **Attack Components Activated**

| Attack | Status | Effect |
|--------|--------|---------|
| 🔒 Death Screen | ✅ ACTIVE | Fullscreen matrix flash + countdown |
| 🔊 Sound Hell | ✅ ACTIVE | Continuous error beeps |
| 🖱️ Input Chaos | ✅ ACTIVE | Mouse/keyboard spam |
| 🌐 Browser Hell | ✅ ACTIVE | 100+ tabs (Rickroll + Google) |
| 📁 File Encrypt | ✅ ACTIVE | Creates .CRYPTO copies (Documents/Desktop) |
| 🔔 Notifications | ✅ ACTIVE | Windows popup spam |
| 💻 CMD Flood | ✅ ACTIVE | 100+ command windows |
| 🛡️ TaskMgr Kill | ✅ ACTIVE | Blocks Task Manager |

### 4. **Recovery**
```
1. Enter password: 8846
2. Click "DECRYPT FILES"
3. Kill python.exe processes
4. Delete .CRYPTO files + ENCRYPTED_FILES.txt
```

## ⚙️ Customization Guide

### Edit Attack Intensity

```python
# === QUICK MODS ===

# 1. Change password (line 11)
PASSWORD = "YOUR_NEW_PASSWORD"

# 2. Reduce file encryption (line 104)
for file in files[:10]:  # Change 50 -> 10

# 3. Disable browser spam (line 67)
# browser_hell()  # Comment out

# 4. Slower chaos (line 51)
time.sleep(0.1)  # Change 0.03 -> 0.1
```

### Attack Toggle Matrix

```python
def DEPLOY_APOCALYPSE():
    # Toggle individual attacks:
    # kill_taskmgr()      # ✅ Enable/Disable
    sound_hell()         # ✅ Enable/Disable
    # mouse_keyboard_chaos()
    # browser_hell()
    # etc...
```

## 📁 File Structure After Attack

```
Desktop/
├── ransomware.py          # Main script
├── ENCRYPTED_FILES.txt    # Encryption log
├── file1.jpg.CRYPTO      # Encrypted copies
├── document.docx.CRYPTO
└── etc...
```

## 🛡️ Safety & Cleanup

### Emergency Stop
```
Ctrl+C (may not work during fullscreen)
Task Manager → End python.exe
Restart Explorer.exe
```

### Full Cleanup Script
```batch
@echo off
taskkill /f /im python.exe
del /s *.CRYPTO
del "%USERPROFILE%\Desktop\ENCRYPTED_FILES.txt"
echo CLEANUP COMPLETE
```

## 🎯 Pentest Scenarios

1. **Blue Team Training**: Test detection/response
2. **Endpoint Hardening**: AV/EDR evasion testing
3. **User Awareness**: Social engineering simulation
4. **Backup Validation**: Ransomware recovery drill
5. **Incident Response**: Full IR exercise

## 📈 Technical Breakdown

| Component | Technique | Evasion |
|-----------|-----------|---------|
| **Lock Screen** | Tkinter Fullscreen | `topmost=True` |
| **Audio** | `winsound.SND_LOOP` | No external files |
| **Input** | `SetCursorPos()` + `keybd_event()` | Windows API |
| **Browser** | `webbrowser.open()` | Native browser spawn |
| **Files** | `shutil.copy2()` | File duplication |
| **TaskMgr** | `taskkill /f` | Process termination |

## 🔒 Legal & Authorization

```
CREATED BY: Dairon
PURPOSE: Authorized Penetration Testing
STATUS: I have explicit permission for this pentest
USAGE: Educational & Professional Security Testing ONLY
```

## ⭐ Pro Tips

```
PRO TIP #1: Run in VM for safe testing
PRO TIP #2: Test audio BEFORE client demo  
PRO TIP #3: Customize password per engagement
PRO TIP #4: Document ENCRYPTED_FILES.txt location
PRO TIP #5: Use --no-sandbox Chrome flags for max tabs
```

---

## 📞 Support

**Author**: Dairon  
**Version**: 4.0 (Pure Python Edition)  
**Last Updated**: April 2026

```
🚨 FOR AUTHORIZED PENTESTERS ONLY 🚨
Questions? Contact your engagement handler.
```

![Footer](https://via.placeholder.com/1200x100/000000/FF6600?text=Authorized+Pentest+Tool+-+Educational+Use+Only)

---

**Replace placeholder images with:**
1. Screenshot of fullscreen lock
2. File encryption demo  
3. Browser tab flood proof
4. Cleanup verification

**Copy this README to `README.md` and commit!** 🎉# virus
