# Необходимо наличие Pandoc, установить choco install pandoc

import subprocess

def convert_to_pptx(md_template, pptx_output):
    subprocess.check_call(["pandoc","-o",pptx_output,md_template])