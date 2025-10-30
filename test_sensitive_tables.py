#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark

def test_sensitive_tables_extraction():
    """Test the new sensitive table extraction functionality"""
    print("Testing sensitive table extraction functionality...")
    
    # Create an instance of SubDark
    tool = SubDark()
    
    # Set a test target
    tool.target = "test-target.com"
    
    # Test the new function
    try:
        result = tool.extract_real_sensitive_tables()
        if result:
            print("✅ Sensitive table extraction function works correctly!")
        else:
            print("❌ Sensitive table extraction function returned False")
    except Exception as e:
        print(f"❌ Error testing sensitive table extraction: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    success = test_sensitive_tables_extraction()
    if success:
        print("\n🎉 All tests passed! The new functionality is working correctly.")
    else:
        print("\n❌ Tests failed. Please check the implementation.")
        sys.exit(1)