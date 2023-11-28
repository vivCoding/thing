from pypdf import PdfReader, PdfWriter
from pwinput import pwinput

print ("Hello there")
filename = input("Enter name of file to encrypt: ")
password = pwinput("Enter password to encrypt with: ")

try:
    reader = PdfReader(filename)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    print ("Encrypting...")
    writer.encrypt(password, algorithm="AES-256-R5")

    with open("output.pdf", "wb") as f:
        writer.write(f)

    input(f"\nSuccessfully encrypted {filename}. Press any key to exit...")
except Exception as e:
    print (e)
    input(f"\nFailed to encrypt. Press any key to exit...")