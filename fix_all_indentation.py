#!/usr/bin/env python3
"""
Script to fix all indentation issues in subdark.py interactive_menu method
"""

def fix_all_indentation():
    # Read the original file
    with open('subdark.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the start and end of the interactive_menu method
    start_line = -1
    end_line = -1
    
    for i, line in enumerate(lines):
        if 'def interactive_menu(self):' in line:
            start_line = i
            break
    
    if start_line == -1:
        print("Could not find interactive_menu method")
        return
    
    # Find the end of the interactive_menu method
    for i in range(start_line + 1, len(lines)):
        line = lines[i]
        # Look for the next method definition or class definition
        if line.strip().startswith('def ') and 'def interactive_menu' not in line:
            end_line = i
            break
        if line.strip().startswith('class '):
            end_line = i
            break
        
        # If we reach the end of file
        if i == len(lines) - 1:
            end_line = len(lines)
            break
    
    if end_line == -1:
        print("Could not find end of interactive_menu method")
        return
    
    print(f"Found interactive_menu method from line {start_line} to {end_line}")
    
    # Fix indentation for all choice blocks
    for i in range(start_line, end_line):
        line = lines[i]
        
        # Fix choice statements (if choice ==, elif choice ==, else)
        if ('if choice ==' in line or 'elif choice ==' in line or 
            (line.strip().startswith('else:') and 'choice' in lines[i-1])):
            # Ensure proper indentation (8 spaces for the choice statements)
            if not line.startswith('        '):
                lines[i] = '        ' + line.lstrip()
        
        # Fix the content inside choice blocks
        elif i > start_line and ('if choice ==' in lines[i-1] or 'elif choice ==' in lines[i-1] or 
                               (lines[i-1].strip().startswith('else:') and 'choice' in lines[i-2])):
            # Ensure proper indentation (12 spaces for the content inside choice blocks)
            if not line.startswith('            '):
                lines[i] = '            ' + line.lstrip()
    
    # Write the fixed file
    with open('subdark.py', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("All indentation issues fixed successfully")

if __name__ == "__main__":
    fix_all_indentation()