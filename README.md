# Image-to-Text Converter using OCR Technology  

This project leverages **Tesseract-OCR** to extract text from images, supporting English language text detection. It includes step-by-step setup and configuration to train custom OCR models and run text extraction scripts.  

---

## Steps to Set Up  

### Step 1: Install Tesseract-OCR  
1. Download the latest version of Tesseract-OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki).  
2. Run the setup, select the languages of your choice, and complete the installation.  
3. Add the **Tesseract-OCR** path to your system’s environmental variables.  
   - Open CMD and type:  
     ```shell
     tesseract --version
     ```
   - If the version appears, the setup is successful.  

---

### Step 2: Install Required Tools  
1. Install Git Bash and Windows Package Manager (Winget):  
   - To check if Winget is already installed, open CMD and type:  
     ```shell
     winget --version
     ```  
     If the version is shown, it’s already installed.  

2. Install `wget` using Winget:  
   ```shell
   winget install wget
