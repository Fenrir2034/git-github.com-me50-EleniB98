from fpdf import FPDF

class ShirtificatePDF(FPDF):
    def header(self):
        # Header: CS50 Shirtificate
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def add_shirt_image(self):
        # Add shirt image centered horizontally
        self.image("shirtificate.png", 40, 40, 130)

    def add_user_name(self, name):
        # Add user's name on top of the shirt in white text
        self.set_font("Arial", "", 14)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, name, 0, 1, "C")

def generate_shirtificate(name):
    pdf = ShirtificatePDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Disable automatic page breaks
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_shirt_image()
    pdf.add_user_name(name)

    pdf.output("shirtificate.pdf")

def main():
    # Prompt user for their name
    name = input("Enter your name: ")

    # Generate shirtificate PDF
    generate_shirtificate(name)

if __name__ == "__main__":
    main()
