# Image-to-Text Converter using OCR Technology  

This project leverages **Tesseract-OCR** to extract text from images, supporting English language text detection. It includes step-by-step setup and configuration to train custom OCR models and run text extraction scripts.  

---

## Steps to Set Up  

- Make sure that Python with latest version and Git Bash is installed in your system.
  
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
   ```

3. Download **make** from this link:
   Download Make [here](https://sourceforge.net/projects/ezwinports/files/make-4.4.1-without-guile-w32-bin.zip/download?use_mirror=cyfuture).
                                    OR
   I already uploaded zip file in the repository named as **make-4.4.1-without-guile-w32-bin**
   - Create a folder in Disk C and name it Tools.
   - Extract the make zip file into the Tools folder.

5. Add the path to the make-4.4.1 folder to your system’s environmental variables.
   ```shell
   make --version
   wget --version
   ```
   
### Step 3: Clone the Training Repository

1. Clone the Tesseract OCR training repository:
   ```shell
   git clone https://github.com/tesseract-ocr/tesstrain
   ```
   - Save it in a folder named OCR.

2. Inside the tesstrain folder, locate the ocrd-testset.zip file.
   - Create a folder named Data within tesstrain.
   - Extract ocrd-testset.zip into the Data folder.

3. Rename the folder from ocrd-testset to sample-ground-truth.

### Step 4: Train the OCR Model

1. Open the tesstrain folder.

2. Right-click in the folder and select Git Bash Here.

3. Start training the model by running the command:
   ```shell
   make training MODEL_NAME=sample START_MODEL=deu_latf TESSDATA=../tessdata/ MAX_ITERATIONS=500 LEARNING_RATE=0.001
   ```

4. Allow the process to complete; this may take several minutes.

5. After training, navigate to the Data folder and locate the file sample.traineddata.
   - Copy this file to:
   ```text
   C:\Program Files\Tesseract-OCR\tessdata\
   ```

### Step 5: Train the OCR Model

1. Open the OCR folder in VS Code.

2. Run following command in the cmd to install the required libraries for program execution.
   ```shell
   pip install -r requirements.txt
   ```

3. Run the **app.py** file with correct directories.

4. In Terminal, a port link will be generated through flask, holding CTRL and left mouse button, click on it and it will take you to web interface.

   ![image](https://github.com/user-attachments/assets/29cd72da-2f42-41d5-a212-f2ca07f84809)

5. Make sure that picture have the English language text written on it.
