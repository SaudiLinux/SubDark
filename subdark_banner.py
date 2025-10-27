#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows
init(autoreset=True)

def display_subdark_banner():
    """Display SubDark tool banner with beautiful ASCII art and colors"""
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Define colors
    colors = {
        'cyan': Fore.CYAN,
        'blue': Fore.BLUE,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'red': Fore.RED,
        'magenta': Fore.MAGENTA,
        'white': Fore.WHITE,
        'bright_cyan': Fore.LIGHTCYAN_EX,
        'bright_blue': Fore.LIGHTBLUE_EX,
        'bright_green': Fore.LIGHTGREEN_EX,
        'bright_yellow': Fore.LIGHTYELLOW_EX,
        'bright_red': Fore.LIGHTRED_EX,
        'bright_magenta': Fore.LIGHTMAGENTA_EX,
        'bright_white': Fore.LIGHTWHITE_EX,
        'reset': Style.RESET_ALL
    }
    
    # ASCII Art for SubDark
    ascii_art = [
        f"{colors['bright_cyan']}    ███████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗  ██████╗  ██████╗ ███████╗{colors['reset']}",
        f"{colors['bright_blue']}    ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔════╝{colors['reset']}",
        f"{colors['bright_cyan']}    ███████╗██║   ██║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║██║  ███╗█████╗  {colors['reset']}",
        f"{colors['bright_blue']}    ╚════██║██║   ██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██║   ██║██╔══╝  {colors['reset']}",
        f"{colors['bright_cyan']}    ███████║╚██████╔╝██████╔╝███████╗██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████╗{colors['reset']}",
        f"{colors['bright_blue']}    ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝{colors['reset']}"
    ]
    
    # Additional decorative elements
    decorative_line = f"{colors['bright_yellow']}═" * 80 + colors['reset']
    
    # Tool description
    description = [
        f"{colors['bright_white']}    أداة متقدمة لكشف الثغرات الأمنية والاختراق الذكي{colors['reset']}",
        f"{colors['bright_green']}    Advanced Vulnerability Detection & Smart Exploitation Tool{colors['reset']}"
    ]
    
    # Features
    features = [
        f"{colors['bright_magenta']}    ✦ الذكاء الاصطناعي • التعلم الآلي • الأمن السحابي • إنترنت الأشياء ✦{colors['reset']}",
        f"{colors['bright_cyan']}    ✦ XXE • SSRF • CSRF • RCE • SQLi • XSS • LFI • RFI ✦{colors['reset']}"
    ]
    
    # Version and author info
    version_info = [
        f"{colors['bright_white']}    الإصدار: 2.0.0 | النسخة المتقدمة{colors['reset']}",
        f"{colors['bright_yellow']}    تم التطوير بواسطة فريق SubDark للأمن السيبراني{colors['reset']}"
    ]
    
    # Display the banner
    print("\n" * 2)
    print(decorative_line)
    
    for line in ascii_art:
        print(line)
    
    print()
    for desc in description:
        print(desc)
    
    print()
    for feature in features:
        print(feature)
    
    print()
    for info in version_info:
        print(info)
    
    print(decorative_line)
    print("\n" * 1)

def display_loading_animation():
    """Display loading animation"""
    import time
    
    loading_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    loading_text = "جاري تحميل أدوات SubDark المتقدمة..."
    
    print(f"\n{Fore.CYAN}", end="")
    for i in range(30):
        char = loading_chars[i % len(loading_chars)]
        print(f"\r{char} {loading_text}", end="", flush=True)
        time.sleep(0.1)
    print(f"\r✓ {loading_text} تم التحميل بنجاح!{Style.RESET_ALL}\n")

def main():
    """Main function to display the banner"""
    try:
        display_subdark_banner()
        display_loading_animation()
        
        # Optional: Add sound effect (Windows only)
        if os.name == 'nt':
            try:
                import winsound
                winsound.Beep(1000, 200)  # Beep sound
            except:
                pass
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}تم إيقاف عرض البانر.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}خطأ في عرض البانر: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()