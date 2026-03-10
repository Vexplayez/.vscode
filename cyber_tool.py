import time
import os


os.system('')

print("--- [ Vex_playez Security Terminal ] ---")
time.sleep(1)

target = input("Enter Target Name to Scan: ")
print(f"🔍 Searching for vulnerabilities in {target}...")

for i in range(1, 4):
    print("." * i)
    time.sleep(0.5)

print("⚠️ Warning: Weak Password Detected!")
password = input("Try to bypass the system. Enter Password: ")

if password == "1234":
    
    print("\033[92m✅ ACCESS GRANTED! You are inside the system. [Vex_playez Dashboard]\033[0m")
else:
    
    print("\033[91m❌ ACCESS DENIED! ALARM TRIGGERED!\033[0m")
    print("\a")