#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows
init(autoreset=True)

def display_subdark_banner_enhanced():
    """Display enhanced SubDark tool banner with gradient effects and animations"""
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Gradient color progression for SubDark text
    colors = [
        Fore.LIGHTBLUE_EX,    # S
        Fore.LIGHTCYAN_EX,    # u
        Fore.LIGHTGREEN_EX,   # b
        Fore.LIGHTYELLOW_EX,  # D
        Fore.LIGHTRED_EX,     # a
        Fore.LIGHTMAGENTA_EX, # r
        Fore.LIGHTBLUE_EX,    # k
    ]
    
    # Enhanced ASCII Art for SubDark
    ascii_art = [
        "    ███████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗  ██████╗  ██████╗ ███████╗",
        "    ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔════╝",
        "    ███████╗██║   ██║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║██║  ███╗█████╗  ",
        "    ╚════██║██║   ██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██║   ██║██╔══╝  ",
        "    ███████║╚██████╔╝██████╔╝███████╗██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████╗",
        "    ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝"
    ]
    
    # Display animated banner
    print("\n" * 2)
    
    # Typewriter effect for the banner
    for i, line in enumerate(ascii_art):
        color = colors[i % len(colors)]
        print(f"{color}{line}{Style.RESET_ALL}")
        time.sleep(0.1)  # Small delay for animation effect
    
    print()
    
    # Subtitle with glow effect
    subtitle_ar = f"{Fore.WHITE}{Style.BRIGHT}    أداة متقدمة لكشف الثغرات الأمنية والاختراق الذكي{Style.RESET_ALL}"
    subtitle_en = f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}    Advanced Vulnerability Detection & Smart Exploitation Tool{Style.RESET_ALL}"
    
    print(subtitle_ar)
    print(subtitle_en)
    
    print()
    
    # Features with rainbow colors
    features = [
        (f"{Fore.LIGHTMAGENTA_EX}    ✦ الذكاء الاصطناعي ✦{Style.RESET_ALL}", Fore.LIGHTMAGENTA_EX),
        (f"{Fore.LIGHTCYAN_EX}    ✦ التعلم الآلي ✦{Style.RESET_ALL}", Fore.LIGHTCYAN_EX),
        (f"{Fore.LIGHTYELLOW_EX}    ✦ الأمن السحابي ✦{Style.RESET_ALL}", Fore.LIGHTYELLOW_EX),
        (f"{Fore.LIGHTGREEN_EX}    ✦ إنترنت الأشياء ✦{Style.RESET_ALL}", Fore.LIGHTGREEN_EX),
    ]
    
    # Vulnerabilities scanning capabilities
    vuln_text = f"{Fore.LIGHTRED_EX}    XXE • SSRF • CSRF • RCE • SQLi • XSS • LFI • RFI{Style.RESET_ALL}"
    
    print(vuln_text)
    print()
    
    # Version and development info with box
    version_box = f"{Fore.LIGHTBLUE_EX}┌─────────────────────────────────────────────────────────────────────────┐{Style.RESET_ALL}"
    version_line1 = f"{Fore.LIGHTBLUE_EX}│{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}الإصدار: 2.0.0 | النسخة المتقدمة{Style.RESET_ALL}                              {Fore.LIGHTBLUE_EX}│{Style.RESET_ALL}"
    version_line2 = f"{Fore.LIGHTBLUE_EX}│{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}تم التطوير بواسطة فريق SubDark للأمن السيبراني{Style.RESET_ALL}                    {Fore.LIGHTBLUE_EX}│{Style.RESET_ALL}"
    version_box_bottom = f"{Fore.LIGHTBLUE_EX}└─────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}"
    
    print(version_box)
    print(version_line1)
    print(version_line2)
    print(version_box_bottom)
    
    print("\n" * 1)

def display_cyber_matrix_effect():
    """Display cyber matrix rain effect"""
    import random
    
    matrix_chars = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    print(f"{Fore.GREEN}", end="")
    
    # Create matrix effect
    for _ in range(5):
        line = ""
        for _ in range(80):
            if random.random() > 0.7:
                line += random.choice(matrix_chars)
            else:
                line += " "
        print(f"\r{line}", end="", flush=True)
        time.sleep(0.05)
    
    print(f"{Style.RESET_ALL}\r" + " " * 80 + "\r", end="")

def display_loading_animation_enhanced():
    """Display enhanced loading animation"""
    
    loading_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    loading_texts = [
        "جاري تحميل أدوات SubDark المتقدمة...",
        "جاري تهيئة محركات الذكاء الاصطناعي...",
        "جاري تحميل قواعد بيانات الثغرات...",
        "جاري تفعيل وحدات الأمن السحابي...",
        "تم التحميل بنجاح!",
    ]
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}", end="")
    
    for text in loading_texts:
        for i in range(20):
            char = loading_chars[i % len(loading_chars)]
            print(f"\r{char} {text}", end="", flush=True)
            time.sleep(0.08)
        print()
    
    print(f"{Style.RESET_ALL}\n")

def display_security_warning():
    """Display security warning"""
    warning_text = f"""
{Fore.LIGHTRED_EX}{'═' * 80}{Style.RESET_ALL}
{Fore.LIGHTRED_EX}⚠️  تحذير أمني: هذه الأداة مخصصة للاختبار الأمني فقط ⚠️{Style.RESET_ALL}
{Fore.LIGHTYELLOW_EX}⚡ يجب استخدامها فقط على الأنظمة التي تمتلك صلاحية اختبارها ⚡{Style.RESET_ALL}
{Fore.LIGHTRED_EX}{'═' * 80}{Style.RESET_ALL}
"""
    print(warning_text)

def main():
    """Main function to display the enhanced banner"""
    try:
        display_subdark_banner_enhanced()
        display_cyber_matrix_effect()
        display_loading_animation_enhanced()
        display_security_warning()
        
        # Success sound effect (Windows only)
        if os.name == 'nt':
            try:
                import winsound
                winsound.Beep(800, 150)  # Success beep
                time.sleep(0.1)
                winsound.Beep(1000, 150)  # Higher success beep
            except:
                pass
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}تم إيقاف عرض البانر.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}خطأ في عرض البانر: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()