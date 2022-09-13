import os
from pprint import pprint

from jinja2 import Environment, FileSystemLoader
import pdfkit
import pandas as pd

current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))
data = pd.read_csv('data.csv')
invoice_record = data.to_dict('records')
content = invoice_record
print(invoice_record)

def render_template(filename):
	return env.get_template(filename).render(
		content[0]
	)

def generate_pdf_css(template_filename, css_filename, output_filename):
	pdfkit.from_string(render_template(template_filename), output_filename, css=css_filename)

def generate_pdf(template_filename, output_filename):
	print(render_template(template_filename))
	pdfkit.from_string(render_template(template_filename), output_filename)

if __name__ == "__main__":
	generate_pdf_css('/html/templates/template.j2', 'style.css', 'out.pdf')