import webbrowser

class Project():
	""" This class provides a way to store project related information""" 
	def __init__(self, project_title, project_storyline, project_animation, project_information, project_link):
		self.title = project_title
		self.storyline = project_storyline
		self.animation = project_animation
		self.information = project_information
		self.link = project_link

	def show_popup(self):
		webbrowser.open(self.project_information)