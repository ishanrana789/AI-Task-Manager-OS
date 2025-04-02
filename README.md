
# Secure File Management System 🔒

![Security Shield Icon](media/image1.png)  
*A robust system for secure file storage with encryption, 2FA, and threat detection.*

---

## 📌 **Overview**
This **Secure File Management System** provides end-to-end protection for sensitive files through:
- **Password-based authentication** with SHA-256 hashing  
- **Two-Factor Authentication (2FA)** via Google Authenticator (TOTP)  
- **AES (Fernet) encryption** for file security  
- **Threat detection** for malicious/large files  
- **Secure file operations**: Upload, delete, and view metadata  

**Use Case**: Ideal for individuals and organizations handling confidential data.

---

## 🚀 **Features**
| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **User Authentication** | Secure login with password + OTP (Google Authenticator).                   |
| **AES File Encryption** | Files encrypted before storage (Fernet implementation).                    |
| **Threat Detection**    | Flags executables (`.exe`, `.bat`) and files >10MB.                        |
| **File Operations**     | Upload (auto-encrypt), delete, view metadata (size, timestamps).           |
| **Account Recovery**    | Reset OTP secret if lost.                                                  |

---

## 🛠 **Technologies & Libraries**
| Category       | Tool/Library          | Purpose                                |
|----------------|-----------------------|----------------------------------------|
| **Core**       | Python 3.x            | Backend logic                          |
| **Security**   | `cryptography` (AES)  | File encryption/decryption             |
| **Auth**       | `pyotp`               | TOTP generation for 2FA               |
| **Hashing**    | `hashlib` (SHA-256)   | Secure password storage                |

---

## 🔧 **Setup & Installation**
### Prerequisites
- Python 3.8+
- Google Authenticator app (Android/iOS)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/anshikaraj08/OS-CA.git
   cd OS-CA
   Install dependencies:

bash
Copy
pip install cryptography pyotp
Run the system:

bash
Copy
python secure_file_manager.py
🔑 Usage Guide
1️⃣ Register a User
Run the script → Choose Register → Note the generated OTP secret.

Save this secret securely (required for account recovery).

2️⃣ Set Up Google Authenticator
Open Google Authenticator app.

Tap + (Add Account) → Enter a key manually.

Paste the OTP secret from Step 1.

3️⃣ Login with 2FA
Enter username/password.

Input the 6-digit OTP from Google Authenticator.

4️⃣ File Operations
Command	Action
Upload	Encrypts and stores files securely.
Delete	Permanently removes files.
List	Shows encrypted files + metadata.
Detect	Scans for threats (executables/large files).
🛡️ Security Measures
AES-256 Encryption: Files encrypted with Fernet.

2FA: Time-based OTPs (TOTP) via pyotp.

Threat Checks: Blocks .exe/.bat and files >10MB.

Secure Storage: Passwords hashed with SHA-256.

📜 License
MIT License. See LICENSE for details.

🤝 Contributors
Anshika Raj

Melna Anna Soni

Alafeya Qaiser

📬 Contact
For issues or feedback, email: your-email@example.com

Copy

---

### Key Notes:
1. **Focused Content**: Only includes the **Secure File Management System** (removed AI Task Manager references).  
2. **Threat Detection**: Explicitly mentions blocking executables and large files (>10MB).  
3. **Step-by-Step Guides**: Clear instructions for 2FA setup and file operations.  
4. **Security Emphasis**: Highlights AES, SHA-256, and TOTP in a dedicated section.  

Let me know if you'd like to add screenshots or modify any sections! 🔐
   
