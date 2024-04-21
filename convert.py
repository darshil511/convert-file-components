import os
from PIL import Image
from docx2pdf import convert 
import pdfkit

#need to download docx2pdf, Pillow, wkhtmltopdf and pdfkit on the system 
# Depencies include: docx2pdf, Pillow, wkhtmltopdf and pdfkit
# install wkhtmltopdf from https://wkhtmltopdf.org/downloads.html

source_dir = "E:/mined/Screenshots" #change this to your source directory where all the files with different extensions are there
output_dir = "E:/mined/pdfs" # specify the path to store pdfs of all the corresponding files in sorce directory


# for converting all images of a folder into different respective pdfs
for file in os.listdir(source_dir):
    file_name, file_extension = os.path.splitext(file)

    # Check if the corresponding PDF file already exists
    pdf_path = os.path.join(output_dir, f'{file_name}.pdf')
    if not os.path.isfile(pdf_path):
        try:
            if file_extension.lower() in ('.png', '.jpg', '.jpeg'):
                image = Image.open(os.path.join(source_dir, file))
                image_converted = image.convert('RGB')
                image_converted.save(pdf_path)
                print(f"Converted {file} to PDF")

            elif file_extension.lower() in ('.docx', '.doc'):
                input_file_path = os.path.join(source_dir, file)
                convert(input_file_path, output_dir)
                print(f"Converted {file} to PDF")

            elif file_extension.lower() == '.html':
                config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
                html_page = os.path.join(source_dir, file)
                pdfkit.from_file(html_page, pdf_path, configuration=config)
                print(f"Converted {file} to PDF")

        except Exception as e:
            print(f"Failed to convert {file} to PDF: {e}")
    else:
        print(f"Skipping {file} as PDF already exists")