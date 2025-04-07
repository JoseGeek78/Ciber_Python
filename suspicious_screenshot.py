import pyautogui
import psutil

MALICIOUS_PROCESSES = "snifre.exe, sniffer.exe, sniffer, snif.exe, snif.exe, sniff.exe, sniff, sniffler.exe, sniffler"

for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] in MALICIOUS_PROCESSES.split(", "):
        print(f"Suspicious process detected: {proc.info['name']} (PID: {proc.info['pid']})")
        screenshot = pyautogui.screenshot()
        screenshot.save(f"suspicious_process_{proc.info['pid']}.png")
        print(f"Screenshot saved as suspicious_process_{proc.info['pid']}.png")
        break
else:
    print("No suspicious processes found.")
    