#!/usr/bin/env python3
"""
Script to fix indentation issues in subdark.py
"""

def fix_indentation():
    # Read the original file
    with open('subdark.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the start of the interactive_menu method
    start_line = -1
    for i, line in enumerate(lines):
        if 'def interactive_menu(self):' in line:
            start_line = i
            break
    
    if start_line == -1:
        print("Could not find interactive_menu method")
        return
    
    # Find the end of the interactive_menu method
    end_line = -1
    indent_level = None
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
    
    # Fix indentation for the choice blocks
    in_choice_block = False
    for i in range(start_line, end_line):
        line = lines[i]
        
        # Check if we're in a choice block
        if 'if choice ==' in line or 'elif choice ==' in line:
            in_choice_block = True
            # Ensure proper indentation (8 spaces for the choice statements)
            if not line.startswith('        '):
                lines[i] = '        ' + line.lstrip()
        elif in_choice_block and line.strip() == '':
            # Empty line in choice block
            lines[i] = '        ' + line
        elif in_choice_block and not line.startswith('        '):
            # This should be part of the choice block but has wrong indentation
            lines[i] = '        ' + line
        else:
            in_choice_block = False
    
    # Write the fixed file
    with open('subdark.py', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("Indentation fixed successfully")

if __name__ == "__main__":
    fix_indentation()