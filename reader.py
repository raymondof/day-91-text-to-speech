from PyPDF2 import PdfReader


class Reader:
    def __init__(self, story):
        # create a pdf reader object
        self.reader = PdfReader(story)
        self.pages_in_pdf = len(self.reader.pages)
        self.text_string = ""

    def read(self):
        for page_no in range(self.pages_in_pdf):
            page = self.reader.pages[page_no]
            self.text_string += page.extract_text() + " "
        return self.text_string
