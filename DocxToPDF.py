import comtypes.client
import os

def word_to_pdf(input_path, output_path=None):
    """
    Convert a Word file (.docx) to a PDF file using comtypes.

    Args:
        input_path (str): Path to the Word file to be converted.
        output_path (str, optional): Path to save the converted PDF file. Defaults to None.
    """
    # Check if the file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file '{input_path}' does not exist.")

    # Set default output path if not provided
    if output_path is None:
        output_path = input_path.replace(".docx", ".pdf")

    # Initialize Word application
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(input_path)
    
    # Save as PDF
    doc.SaveAs(output_path, FileFormat=17)  # FileFormat=17 is for PDF
    doc.Close()
    word.Quit()

    return output_path

# Example usage
if __name__ == "__main__":
    word_file = r"PATH TO WORD FILE"  # Replace with the path to your Word file
    pdf_file = word_to_pdf(word_file, output_path=r"\.")
    print(f"Word file converted to PDF: {pdf_file}")
