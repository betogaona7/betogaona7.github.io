
# coding=<UTF-8>

import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> 
    <title>Alberto Gaona | Projects</title>
    
    <link href='../../img/icon.ico' rel='shortcut icon' type='image/ico'/>

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <link rel="stylesheet" type="text/css" href="../../css/style.css" />

    <style type="text/css" media="screen">
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <div>
        <h1>Alberto Gaona</h1>
        <h2>Projects</h2>
    <div>
        
    <div class="container">
        {project_tiles}
    </div>

    <footer class="footer">
        <div class="inner-container">
            <ul class="footer-links">
                <li><a href="http://www.facebook.com/betogaona07" target="_blank" rel="noopener"> Facebook </a></li>
                <li><a href="http://www.github.com/betogaona7" target="_blank" rel="noopener"> Github </a></li>
                <li><a href="http://www.instagram.com/betogaona7" target="_blank" rel="noopener"> Instagram </a></li>
                <li><a href="http://www.instagram.com/betogaona7" target="_blank" rel="noopener"> Blog </a></li>
            </ul>
        </div>

        <div class="footer-copy">
            2018 Alberto Gaona - <a href="mailto:albertoo_3c@hotmail.com"> Contact </a>
        </div>
    </footer>
</body>
</html>
'''

# A single movie entry html template
project_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{project_information}" data-toggle="modal" data-target="#trailer">
    <img src="{project_animation}" width="370" height="250">
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
            project_information=project.information,
            project_storyline=project.storyline,
            project_link=project.link
        )
    return content


def open_project_page(projects):
    # Create or overwrite the output file
    output_file = open('projects.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        project_tiles=create_project_tiles_content(projects))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)