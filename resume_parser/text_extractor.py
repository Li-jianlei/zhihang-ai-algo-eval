from tika import parser
import os

# Function for converting PDF files to text
def convert_pdf_to_text(dir):
    output = []  # Create an empty list to store the text from PDF files
    
    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(dir):
        for file in files:
            path_to_pdf = os.path.join(root, file)  # Get the full path of the PDF file
            [stem, ext] = os.path.splitext(path_to_pdf)
            
            # Check if the file has a ".pdf" extension
            if ext == '.pdf':
                print("Processing " + path_to_pdf)
                
                # Use Tika to extract text from the PDF
                pdf_contents = parser.from_file(path_to_pdf, service='text')
                
                path_to_txt = stem + '.txt'
                # If you want to save the text to a text file, you can uncomment the following code:
                # with open(path_to_txt, 'w', encoding='utf-8') as txt_file:
                #     print("Writing contents to " + path_to_txt)
                #     txt_file.write(pdf_contents['content'])
                
                output.append(pdf_contents['content'])  # Append the text content to the output list
    
    return output  # Return a list of text extracted from the PDF files
