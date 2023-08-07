from fpdf import FPDF
import random
import string
import base64

class create_pdf():    
    
    @classmethod
    def create_file_pdf(seft, name, last_name, age, phone, email):
        
        random_string =   ''
        
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10))
        
        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        
        pdf.multi_cell(w = 0, h = 50, txt = "Chelita Software - FullStack Test", border = 0, align = 'C', fill = 0)
        
        pdf.cell(w = 20, h = 15, txt = 'Nombre:', border = 0, align = 'L', fill = 0)
        pdf.set_font('Arial', '', 16)
        pdf.cell(w = 90, h = 15, txt = name, border = 0, align = 'L', fill = 0)
        pdf.cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        pdf.multi_cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(w = 20, h = 15, txt = 'Apellido:', border = 0, align = 'L', fill = 0)
        pdf.set_font('Arial', '', 16)
        pdf.cell(w = 90, h = 15, txt = last_name, border = 0, align = 'L', fill = 0)
        pdf.cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        pdf.multi_cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(w = 20, h = 15, txt = 'Edad', border = 0, align = 'L', fill = 0)
        pdf.set_font('Arial', '', 16)
        pdf.cell(w = 90, h = 15, txt = age, border = 0, align = 'L', fill = 0)
        pdf.cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        pdf.multi_cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(w = 20, h = 15, txt = 'Telefono:', border = 0, align = 'L', fill = 0)
        pdf.set_font('Arial', '', 16)
        pdf.cell(w = 90, h = 15, txt = phone, border = 0, align = 'L', fill = 0)
        pdf.cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        pdf.multi_cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)

        pdf.set_font('Arial', 'B', 16)
        pdf.cell(w = 20, h = 15, txt = 'Correo', border = 0, align = 'L', fill = 0)
        pdf.set_font('Arial', '', 16)
        pdf.cell(w = 90, h = 15, txt = email, border = 0, align = 'L', fill = 0)
        pdf.cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        pdf.multi_cell(w = 0, h = 15, txt = '', border = 0, align = 'L', fill = 0)
        pdf.output(random_string +'.pdf')
        
        return random_string
    
    @classmethod
    def get_file_pdf(seft, id):    
        with open(id + '.pdf', 'rb') as pdf_file:
            my_base64 = base64.b64encode(pdf_file.read())
        return my_base64