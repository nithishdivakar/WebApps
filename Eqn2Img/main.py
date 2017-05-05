import web

from TexCompiler import TexCompiler
import shutil
import os

C = TexCompiler()


urls = (
  '/', 'index',
  '/add', 'process'
)


class index:
  def GET(self):
    with open("index.html","r") as f:
      return ''.join(f.readlines())


tex_template_beg='''
\documentclass[convert={density=3000,outext=.png}]{standalone}
\\begin{document}'''

tex_template_end='''
\end{document}
'''

class process:
  def POST(self):
    i = web.input()
    print i
    print i['texcont']

    with open("ttt.tex","w") as f:
      f.write(tex_template_beg+i['texcont']+tex_template_end)
    output = C.to_pdf("ttt.tex")
    if not os.path.exists('static'):
      os.mkdir('static')
    shutil.copy("ttt.png","static/ttt.png")

    output = str(output)
    print output
    output = output.replace('\n','<br>')
    return "Output: <br>" + str(output)

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.internalerror = web.debugerror
  app.run() 
