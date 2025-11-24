from fpdf import FPDF

def get_center_x(text):
    p_w = pdf.w
    t_w = pdf.get_string_width(text)
    return (p_w - t_w)/2


pdf = FPDF()
pdf = FPDF(orientation = 'p', format=(210, 297)) # ) #
pdf.add_page()

pdf.set_font("helvetica", size=48)
text = "CS50 Shirtificate"

text_width = pdf.get_string_width(text)
x_val = get_center_x(text)
pdf.set_x(x_val)            # format to set text to center

pdf.cell(0, 57, text)  # set text


page_width = pdf.w
img = r"shirtificate.png"
pdf.image(img, (page_width - 200), 70 , h=190)


# text_2 = "Benoit Kuriakose took CS50"
user_name = input("Name: ").strip()
text_2 = f"{user_name} took CS50"
pdf.set_font("helvetica", size=23)

x_val = get_center_x(text_2)
pdf.set_x(x_val)            # format to set text to center

pdf.set_text_color(255, 255, 255)   # set text color to white
pdf.cell(0, 255, text_2)  # set text

pdf.output("shirtificate.pdf")
