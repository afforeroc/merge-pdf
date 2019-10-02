import glob
from PyPDF2 import PdfFileMerger, PdfFileReader
 
def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger(strict=False)
    
    for path in input_paths:
        #pdf_merger.append(PdfFileReader(path, strict=False)) # Other option
        pdf_merger.append(path)

    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)
 
if __name__ == '__main__':
    paths = glob.glob('input/*.pdf')
    paths.sort()
    merger('merged.pdf', paths)