from time import sleep
from core.errors import InvoiceException
from loguru import logger
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os
import shutil

class InvoiceHandler(object):

    @classmethod
    def generate_invoice(self, file):
        if file is not None:
            file = file.fillna('')
            template_record = file.to_dict('records')
            for item in template_record:
                logger.info(item)
                filename = item['bill_no']
                record = [item]
                self.generate_pdf_css('/html/templates/template.j2', 'style.css', f'../invoices/invoice{filename}.pdf', input_file=record)
            return template_record
        else:
            raise InvoiceException(f"'{file}' url is missing")
        

    
    
    @classmethod
    def render_template(self, filename, input_file):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        logger.info(current_directory)
        env = Environment(loader=FileSystemLoader(current_directory))
        logger.info(env)
        return env.get_template(filename).render(
            input_file[0]
        )

    @classmethod
    def generate_pdf_css(self, template_filename, css_filename, output_filename, input_file):
        pdfkit.from_string(self.render_template(template_filename, input_file), output_filename, css=css_filename)

    @classmethod
    def generate_pdf(self, template_filename, output_filename, input_file):
        pdfkit.from_string(self.render_template(template_filename, input_file), output_filename)
