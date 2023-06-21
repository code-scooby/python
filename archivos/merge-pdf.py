# Import the library
from pypdf import PdfWriter

# Create an instance of PdfWriter
merger = PdfWriter()

# List of PDF files to merge
list_pdf = ["file1.pdf", "file2.pdf"]

# Loop through the list of PDF files and merge them
for pdf in list_pdf:
    merger.append(pdf)

# Write the merged PDF to the output file
merger.write("merged-pdf.pdf")

# Close the PdfWriter instance
merger.close()