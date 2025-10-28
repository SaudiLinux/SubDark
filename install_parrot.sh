#!/bin/bash

# =====================================================
# SubDark Installation Script for Parrot OS
# =====================================================
# This script automates the installation of SubDark on Parrot OS
# Programmer: SayerLinux
# Email: SaudiLinux1@gmail.com

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_header() {
    echo -e "\n${PURPLE}================================================${NC}"
    echo -e "${PURPLE}$1${NC}"
    echo -e "${PURPLE}================================================${NC}\n"
}

# Check if running on Parrot OS
check_system() {
    print_header "Checking System Compatibility"
    
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        if [[ "$ID" == "parrot" ]] || [[ "$ID_LIKE" == *"debian"* ]]; then
            print_success "Parrot OS detected: $PRETTY_NAME"
        else
            print_warning "This script is optimized for Parrot OS, but continuing anyway..."
        fi
    else
        print_warning "Cannot detect OS, continuing with installation..."
    fi
}

# Update system
update_system() {
    print_header "Updating System Packages"
    
    print_status "Updating package list..."
    sudo apt update
    
    print_status "Upgrading packages..."
    sudo apt upgrade -y
    
    print_success "System updated successfully!"
}

# Install Python and essential tools
install_python_tools() {
    print_header "Installing Python and Essential Tools"
    
    print_status "Installing Python3, pip, and git..."
    sudo apt install -y python3 python3-pip python3-venv git curl wget
    
    print_status "Checking Python version..."
    python3 --version
    
    print_status "Checking pip version..."
    pip3 --version
    
    print_success "Python tools installed successfully!"
}

# Install security tools
install_security_tools() {
    print_header "Installing Security Tools"
    
    print_status "Installing Nmap..."
    sudo apt install -y nmap
    
    print_status "Installing SQLMap..."
    git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git ~/tools/sqlmap 2>/dev/null || print_status "SQLMap already exists"
    
    print_status "Installing Metasploit Framework..."
    sudo apt install -y metasploit-framework
    
    print_success "Security tools installed successfully!"
}

# Create project directory
create_project_dir() {
    print_header "Setting Up Project Directory"
    
    PROJECT_DIR="$HOME/Desktop/SubDark"
    
    if [[ -d "$PROJECT_DIR" ]]; then
        print_warning "SubDark directory already exists, updating..."
        cd "$PROJECT_DIR"
        git pull 2>/dev/null || print_warning "Could not update from git"
    else
        print_status "Creating project directory..."
        mkdir -p "$PROJECT_DIR"
        cd "$PROJECT_DIR"
        
        # Clone repository (if exists) or create basic structure
        print_status "Cloning SubDark repository..."
        git clone https://github.com/your-repo/SubDark.git . 2>/dev/null || {
            print_warning "Could not clone repository, creating basic structure..."
            # Create basic files if git clone fails
            cat > requirements.txt << 'EOF'
colorama==0.4.6
prettytable==3.9.0
requests==2.31.0
python-nmap==0.7.1
beautifulsoup4==4.12.2
lxml==4.9.3
urllib3==2.0.7
certifi==2023.7.22
selenium==4.15.2
cvss==2.3
vulners==2.0.0
numpy==1.24.3
boto3==1.29.7
azure-mgmt-compute==30.3.0
google-cloud-compute==1.14.1
EOF
        }
    fi
    
    print_success "Project directory ready: $PROJECT_DIR"
}

# Install Python dependencies
install_python_deps() {
    print_header "Installing Python Dependencies"
    
    # Upgrade pip first
    print_status "Upgrading pip..."
    pip3 install --upgrade pip
    
    # Install requirements
    if [[ -f "requirements.txt" ]]; then
        print_status "Installing requirements from requirements.txt..."
        pip3 install -r requirements.txt
    else
        print_status "Installing packages individually..."
        pip3 install colorama prettytable requests python-nmap beautifulsoup4 lxml urllib3 certifi selenium cvss vulners numpy boto3 azure-mgmt-compute google-cloud-compute
    fi
    
    print_success "Python dependencies installed successfully!"
}

# Make scripts executable
make_executable() {
    print_header "Setting Up Executable Permissions"
    
    if [[ -f "subdark.py" ]]; then
        chmod +x subdark.py
        print_success "subdark.py is now executable"
    else
        print_warning "subdark.py not found, skipping..."
    fi
    
    # Make other Python scripts executable
    find . -name "*.py" -type f -exec chmod +x {} \; 2>/dev/null || true
    
    print_success "Scripts permissions set!"
}

# Test installation
test_installation() {
    print_header "Testing Installation"
    
    print_status "Testing Python imports..."
    
    # Test basic imports
    python3 -c "import colorama; print('✅ colorama imported successfully')" || print_error "colorama import failed"
    python3 -c "import requests; print('✅ requests imported successfully')" || print_error "requests import failed"
    python3 -c "import nmap; print('✅ python-nmap imported successfully')" || print_error "python-nmap import failed"
    
    print_status "Testing SubDark initialization..."
    
    # Test SubDark import if file exists
    if [[ -f "subdark.py" ]]; then
        python3 -c "
import sys
sys.path.append('.')
try:
    from subdark import SubDark
    print('✅ SubDark imported successfully')
except Exception as e:
    print(f'⚠️  SubDark import warning: {e}')
" || print_warning "SubDark import test failed (this is normal if some dependencies are missing)"
    fi
    
    print_success "Installation test completed!"
}

# Create desktop shortcut
create_shortcut() {
    print_header "Creating Desktop Shortcut"
    
    SHORTCUT_FILE="$HOME/Desktop/SubDark.desktop"
    PROJECT_DIR="$HOME/Desktop/SubDark"
    
    cat > "$SHORTCUT_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=SubDark
Comment=Advanced Security Assessment Tool
Exec=python3 $PROJECT_DIR/subdark.py
Icon=$PROJECT_DIR/icon.png
Path=$PROJECT_DIR
Terminal=true
StartupNotify=true
Categories=Security;Network;
Keywords=security;vulnerability;scanner;
EOF

    chmod +x "$SHORTCUT_FILE"
    print_success "Desktop shortcut created!"
}

# Print final instructions
print_final_instructions() {
    print_header "Installation Complete! 🎉"
    
    echo -e "${GREEN}تهانينا! تم تثبيت SubDark بنجاح على نظام Parrot OS الخاص بك.${NC}"
    echo
    echo -e "${CYAN}لتشغيل الأداة:${NC}"
    echo -e "  cd ~/Desktop/SubDark"
    echo -e "  python3 subdark.py"
    echo
    echo -e "${CYAN}أو استخدم الاختصار على سطح المكتب${NC}"
    echo
    echo -e "${YELLOW}المميزات المتوفرة:${NC}"
    echo -e "  🔍 فحص الثغرات الذكي"
    echo -e "  🤖 التنبؤ بالثغرات باستخدام الذكاء الاصطناعي"
    echo -e "  ☁️ فحص الأمان السحابي"
    echo -e "  📱 اختبار أمان تطبيقات الجوال"
    echo -e "  🌐 فحص إنترنت الأشياء (IoT)"
    echo -e "  📊 إنشاء تقارير احترافية"
    echo
    echo -e "${RED}⚠️  تحذير:${NC}"
    echo -e "  تأكد من الحصول على إذن قبل اختبار أي نظام"
    echo -e "  استخدم الأداة فقط لأغراض تعليمية واختبار الأنظمة التي تمتلكها"
    echo
    echo -e "${GREEN}للدعم الفني:${NC}"
    echo -e "  📧 البريد الإلكتروني: SaudiLinux1@gmail.com"
    echo -e "  📱 التليجرام: @SayerLinux"
    echo
    echo -e "${PURPLE}تم التثبيت بنجاح! استمتع باكتشاف الثغرات الأمنية وتحسين أمان أنظمتك!${NC}"
}

# Main installation function
main() {
    print_header "SubDark Installation Script for Parrot OS"
    
    echo -e "${CYAN}مرحباً بك في برنامج تثبيت SubDark لنظام Parrot OS!${NC}"
    echo -e "${CYAN}هذا البرنامج سيساعدك في تثبيت جميع المتطلبات وتشغيل الأداة بدون أخطاء.${NC}"
    echo
    
    read -p "هل تريد المتابعة؟ (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_warning "تم إلغاء التثبيت."
        exit 1
    fi
    
    # Run installation steps
    check_system
    update_system
    install_python_tools
    install_security_tools
    create_project_dir
    install_python_deps
    make_executable
    test_installation
    create_shortcut
    print_final_instructions
}

# Run main function
main "$@"