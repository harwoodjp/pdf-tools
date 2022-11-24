from subprocess import run, PIPE

def split_to_png(input_file, output_dir):
  command = f"gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 -dDownScaleFactor=3 -sOutputFile={output_dir}/%04d.png {input_file}"
  result = run(command, shell=True, stdout=PIPE, stderr=PIPE)
  if result.returncode == 0:
    print(f"Split to PNG succeeded for {input_file}")   
  else:
    print(f"Split to PNG failed for {input_file}")
    print(result.args)
    print(result.stdout)
    raise Exception("split_to_png failed")
