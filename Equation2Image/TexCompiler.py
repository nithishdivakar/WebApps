import os
import subprocess


class TexCompiler(object):
  """

  """

  def __init__(self):
    pass


  def to_pdf(self, input_file):
    #command = ['latexmk', '--pdf','--interaction=nonstopmode', input_file]
    command = ['pdflatex', '-shell-escape', input_file]
    print command
    try:
      output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
      print(e.output.decode())
    return output




if __name__ == "__main__":
  C = TexCompiler()
  C.to_pdf("bla.tex")
