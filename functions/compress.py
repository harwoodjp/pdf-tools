from subprocess import run, PIPE

def compress_pdf(input_file, output_file):
  command = f"gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile={output_file} {input_file}"
  result = run(command, shell=True, stdout=PIPE, stderr=PIPE)
  if result.returncode == 0:
  	pass
  else:
    print(result.args)
    print(result.stdout)
    raise Exception("compress_pdf failed")