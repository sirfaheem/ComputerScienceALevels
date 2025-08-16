#9691_s03_qp_1.pdf
import csv
import os
from io import BytesIO
from PIL import Image
from PyPDF4 import PdfFileReader

# Open the PDF file
pdf_file = open('9691_s03_qp_1.pdf', 'rb')
pdf_reader = PdfFileReader(pdf_file)

# Create a new CSV file
csv_file = open('exam_questions.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

# Write the header row to the CSV file
csv_writer.writerow(['Question Number', 'Question', 'Answer', 'Diagram'])

# Loop through each page in the PDF file
for page_num in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page_num)

    # Extract the text from the page
    text = page.extractText().replace('\n', ' ')

    # Extract the question and answer from the text
    question_start = text.find('Q.')
    question_end = text.find('a)')
    answer_start = text.find('Ans:')
    answer_end = text.find('\n', answer_start)

    question_number = text[question_start:question_end].strip()
    question = text[question_end:answer_start].strip()
    answer = text[answer_start:answer_end].replace('Ans:', '').strip()

    # Check if the page contains a diagram
    if 'Diagram' in text:
        diagram_start = text.find('Diagram')
        diagram_end = text.find('\n', diagram_start)

        # Extract the diagram and save it as a PNG file
        image_stream = BytesIO()
        page.compressContentStreams()
        xObject = page['/Resources']['/XObject'].getObject()
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                image = Image.frombytes("RGB", size, data)
                image.save(image_stream, format="PNG")
                image_stream.seek(0)

        diagram_file = f'{question_number}.png'
        with open(diagram_file, 'wb') as file:
            file.write(image_stream.read())

        # Add the diagram filename to the CSV file
        csv_writer.writerow([question_number, question, answer, diagram_file])
    else:
        # Add the question and answer to the CSV file
        csv_writer.writerow([question_number, question, answer, ''])

# Close the files
pdf_file.close()
csv_file.close()


