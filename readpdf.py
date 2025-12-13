import pypdf
import pypdf.errors 


def Ispdf(file : str):

    try:

        pypdf.PdfReader(file)
        return True
    
    except pypdf.errors.PdfReadError:

        return False
    
def extractContent(file : str):

    pdf_aberto = pypdf.PdfReader(file)
    pagina = pdf_aberto.pages[0]
    texto_extraido = pagina.extract_text(extraction_mode = "plain")

    return texto_extraido

def FilterCostumerData(text : str):

    Start = text.index("Destinatário") + len("Destinatário") + 1
    End = text.index("Detalhamento")
    
    Costumer_data = []
    data = ''

    for i in range(Start, End):

        if text[i] == '\n':

            Costumer_data.append(data)
            data = ''

        else:

            data += text[i]

    return Costumer_data



