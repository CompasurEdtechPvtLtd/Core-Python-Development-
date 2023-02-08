from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",size =30)
pdf.cell(200,10,txt="how to make pdf?",ln=1,align='C')
pdf.cell(200,10,txt="you can use FPDF to make pdf",ln=2,align='C')
pdf.output("mypdf.pdf")
