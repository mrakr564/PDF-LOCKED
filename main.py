import PyPDF2
import getpass
from colorama import Fore, init
from tqdm import tqdm  # Import tqdm for progress bar
logo = """

    \033[91m|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\033[0m
    \033[91m|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\033[0m
    \033[91m||||                                                             ||||           
    \033[91m||||    <Devloper>\033[32m \t\t  Mr.h_akr564\033[0m\t \t\033[91m</Devloper>  ||||\033[0m   
    \033[91m||||                                                             ||||\033[0m
    \033[91m||||               ToolName \033[32m >>>>>>>>>>>>  ("PDF LOCKER") \033[91m\t     ||||\033[0m
    \033[91m||||                                                             ||||\033[0m
    \033[91m||||               Language \033[32m >>>>>>>>>>>>   ("Python")    \033[91m\t     ||||\033[0m
    \033[91m||||                                                             ||||\033[0m
    \033[91m||||    <Github>       \033[32m   https://github.com/    \033[0\033[91m   </Github>    ||||\033[0m
    \033[91m||||                                                             ||||\033[0m
    \033[91m|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\033[0m
    \033[91m|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\033[0m   

"""

print(logo)     
# Initialize colorama for colored output
init()

# Function to lock pdf with tqdm progress bar
def lock_pdf(input_file, password):
   try:  
      with open(input_file, 'rb') as file:
          # Create a PDF reader object
          pdf_reader = PyPDF2.PdfReader(file)
          # Create a PDF writer object
          pdf_writer = PyPDF2.PdfWriter()
          
          # Use tqdm to add pages with progress bar
          for page_num in tqdm(range(len(pdf_reader.pages)), desc="Encrypting PDF", unit="page"):
              pdf_writer.add_page(pdf_reader.pages[page_num])
          
          # Encrypt the PDF with the provided password
          pdf_writer.encrypt(password)
          
          # Write the encrypted content back to the original file
          with open(input_file, 'wb') as output_file:
              pdf_writer.write(output_file)
         # Let the user know it's done
          print(f"{Fore.GREEN}[+] PDF locked successfully.")

   except Exception as e:
       print("\033[91m\tsyntax Error Try Again\033[0m")    

# Get user input
input_pdf = input("    \033[91m--> Enter the path to the PDF file:\033[0m ")
password = getpass.getpass("    \033[91m--> Enter the password to lock the PDF:\033[0m ")

# Lock the PDF using PyPDF2 with tqdm progress bar
print(f'{Fore.GREEN}    [!] Please hold on for a few seconds..')
lock_pdf(input_pdf, password)

