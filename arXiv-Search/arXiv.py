import web
from web import form
import webbrowser
from bs4 import BeautifulSoup
import urllib


render = web.template.render('')

myform = form.Form( 
	form.Textbox(
		"search_query",
		id="search_query",
		description="Search",
		value="Machine learning",
		class_="form-control",
	),
	form.Textbox(
		"start",
		form.notnull,
		form.regexp('\d+', 'Must be a digit'),
		form.Validator('Must be >= 0', lambda x:int(x)>=0),
		description="Start",
		value="0",
		id="start",
		class_="form-control",
	),
	form.Textbox(
		"numb_results",
		form.notnull,
		form.regexp('\d+', 'Must be a digit'),
		form.Validator('Must be more than 0', lambda x:int(x)>0),
		description="Results in page",
		value = "10",
		id="numb_results",
		class_="form-control",
	),
	#form.Checkbox('curly'),
	form.Dropdown(
		'sortBy', 
		[ "lastUpdatedDate", "relevance", "submittedDate", ],
		description="Sort by",
		id = "sortBy",
		class_="form-control",
	),
	form.Dropdown(
		'sortOrder', 
		[ "descending", "ascending",],
		description="Sort Order",
		id="sortOrder",
		class_="form-control",
	),
)


urls = (
	'/', 'index'
)

link_string = 'http://export.arxiv.org/api/query?search_query=ti:\'{search_query}\'&sortBy={sortBy}&sortOrder={sortOrder}&start={start}&max_results={numb_results}'


class index:
	def GET(self):
		form = myform()
		return render.results(form,[])

	def POST(self): 
		form = myform() 
		if not form.validates():
			return render.results(form,[])
		else:
			# form.d.boe and form['boe'].value are equivalent ways of
			# extracting the validated arguments from the form.
			
			url = link_string.format(
				search_query = form['search_query'].value,
				sortBy       = form['sortBy'].value,
				sortOrder    = form['sortOrder'].value,
				start        = form['start'].value,
				numb_results = form['numb_results'].value,
			)
			data = urllib.urlopen(url).read()
			xml_data = BeautifulSoup(data,"lxml")
			
			entries = xml_data.findAll('entry')
			data = []
			for entry in entries:
				authors = [ N.string for N in entry.findAll('name')]
				id = entry.id.string
				updated = entry.updated.string
				published = entry.published.string
				title = entry.title.string
				summary = entry.summary.string
				pdf_link = entry.findAll('link',type="application/pdf")[0]['href']
				#<link href="http://arxiv.org/pdf/cond-mat/0102536v1" rel="related" title="pdf" type="application/pdf"/>
				data.append({
					'authors': authors,
					'id': id,
					'updated': updated,
					'published': published,
					'title': title,
					'pdf_link': pdf_link,
					'summary': summary,
				})
			return render.results(form, data)


if __name__ == "__main__": 
	app = web.application(urls, globals())
	webbrowser.open_new_tab("http://0.0.0.0:8080")
	app.run()
