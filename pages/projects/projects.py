
# coding=<UTF-8>

import webbrowser
import os
import re

# Styles and scripting for the page
page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> 
    <title>Alberto Gaona</title>
    <link href='./img/aglogo.ico' rel='icon' type='image/ico'/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- For the landing -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script type="text/javascript" src="js/transition.js"></script> 

    <!-- For the project section -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <!-- My styles -->
    <link rel="stylesheet" type="text/css" href="css/transition.css" />
    <link rel="stylesheet" type="text/css" href="css/riple.css">
    <link rel="stylesheet" type="text/css" href="css/style.css?v={random number/string}" />
</head>
<body>
'''

# The main page layout and title bar
page_content = '''
<div class="modal" id="trailer">
    <div class="modal-dialog">
        <div class="modal-content">
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
            </a>
            <div class="scale-media" id="technical-speech"></div>
        </div>
    </div>
</div>

<div>
    <a href="" class=".link cleanlink"><h1>Alberto Gaona</h1></a>
    <h2 style="color:#676767;">Projects</h2>
</div>

<div class="container">
    <div class="row">
        {project_tiles}
    </div>
</div>
'''

page_footer = '''
<footer class="footer">
    <div class="inner-container">
        <ul class="footer-links">
            <li><a class="color-nol" href="https://www.facebook.com/betogaona07" target="_blank" rel="noopener"> Facebook </a></li>
            <li><a class="color-nol" href="https://www.github.com/betogaona7" target="_blank" rel="noopener"> Github </a></li>
            <li><a class="color-nol" href="https://www.linkedin.com/in/betogaona7/" target="_blank" rel="noopener"> LinkedIn </a></li>
            <li><a class="color-nol" href="https://www.instagram.com/betogaona7" target="_blank" rel="noopener"> Instagram </a></li>
            <li><a class="color-nol" href="https://betogaona7.github.io/blog" target="_blank" rel="noopener"> Blog </a></li>
        </ul>
    </div>

    <div class="footer-copy color-nol" style="margin-bottom: 15px;">
        © 2018 Alberto Gaona - <a href="mailto:albertoo_3c@hotmail.com"> Contact </a>
    </div>
</footer> 

</body>
</html>
'''

# A single movie entry html template
project_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center size" 
project-name="{project_title}" 
technical-description="{project_information}" 
video-url="{project_video}" 
github-url="{project_link}"
data-toggle="modal" data-target="#trailer">
    <img src="{project_animation}" class="project-img">
    <h3>{project_title}</h3>
    <h4>{project_storyline}</h4>
    <h5>Read more...</h5>
</div>
'''


def create_project_tiles_content(projects):
    # The HTML content for this section of the page
    content = ''
    for project in projects:
        # Append the tile for the movie with its content filled in
        content += project_tile_content.format(
            project_title=project.title,
            project_animation=project.animation,
            project_video=project.video,
            project_information=project.information,
            project_storyline=project.storyline,
            project_link=project.link
        )
    return content


def open_project_page(projects):
    # Create or overwrite the output file
    output_file = open('projects.html', 'w')
    # Replace the movie tiles placeholder generated content
    rendered_content = page_content.format(
        project_tiles=create_project_tiles_content(projects))
    # Output the file
    output_file.write(page_head + rendered_content + page_footer)
    output_file.close()
    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open(output_file.name, new=2)