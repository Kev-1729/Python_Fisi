from fpdf import FPDF

text = input("Name: ")
pdf = FPDF(format="A4", orientation="P")
pdf.add_page()

pdf.set_font("helvetica", size = 64)

pdf.text(x=pdf.w*0.10, y=pdf.h*0.10, txt="CS50 Shirtificate")

eje_x = pdf.w / 2  # ancho
eje_y = pdf.h / 2  # alto

imagen = "shirtificate.png"

m = 200
n = 200

pdf.image(imagen, x=eje_x - m/2 , y=eje_y - n/2 , w=m, h=n)
text_width = pdf.get_string_width(text)
x_position= eje_x - text_width / 2

pdf.set_text_color(255, 255, 255)
pdf.set_font('Arial', size= 32)
pdf.text(x=x_position + eje_x*0.5 , y=eje_y - eje_y*0.25, txt=f"{text}")

pdf.output("shirtificate.pdf")
