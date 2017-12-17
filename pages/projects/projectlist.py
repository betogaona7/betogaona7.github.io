import media 
import projects


DL_project1 = media.Project("Bike Share",

						  "Imagine yourself owning of a bike sharing company like CycleHop and you want to predict how many bikes "  \
						  "you need because if you have too few you're losing money from potential riders or vice versa if you have "\
						  "too many you're wasting money on bikes that are just sitting around. This project predict the number of " \
						  "bikeshare users on a given day from historical data, so you can know how many bikes you will need in the "\
						  "near future.",

						  "https://media.giphy.com/media/r5ULIvOOtdIWs/giphy.gif",
						  "",
						  """
						  Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and 
						  return back has become automatic. Through these systems, user is able to easily rent a bike from a particular position
						  and return back in another position. Currently, there are about over 500 bike-sharing programs around the world 
						  which is composed of over 500 thousands bicycles.<br/><br/>

						  This project is a simple neural network to make predictions of bike-sharing usage. Using a 
						  <a target='_blank' rel='noopener' href='https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset'>dataset</a> that 
						  has the number of riders for each hour of each day from January 1, 2011 to December 31, 2012. The data is pretty complicated. 
						  The weekends have lower over all rideship and there are spikes when people are biking to and from work during the week.
						  Also have information about temperature, humidity, and windspeed. all of these likely affecting the number of riders.<br/><br/>

						  The network has two layers, a hidden layer and an output layer. The hidden layer use the sigmoid function for activations.
						  The output layer has only one node and is used for regression, the output node is the same as the input node.<br/><br/>

						  In the following graph we can compare our predictions with the actual data:
						  <br/><br/>
						  <div style='text-align: center;'>
						  	<img src='./img/bikeshare-graph.png' alt='Bike share results'>
						  </div><br/><br/>
						  """,
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-BikeShare")

DL_project2 = media.Project("Image Classification",

						  "Vision is the main way humans gain information about the world, with the passage of time we have been able "  \
						  "to give eyes to the machines, from that, amazing applications have been created. For example, a company "	 \
						  "called Orbital Insigths analyze satellite imagery to count cars and oil tank levels automatically to predict "\
						  "such things as mall sales and oil production. In this project I developed a program capable of recognize and "\
						  "classify ten different types of images.",

						  "https://media.giphy.com/media/PnabT7xYZ3ffG/giphy.gif",
						  "",
						  "Technical description not available yet -",
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Classification")

DL_project3 = media.Project("TV Scripts Generator",

						  "The way to write a script for a TV show is to actually write a script. A pen is useful, typing is also good. "   \
						  "Keep putting words on the page, but if for some reason you don't feel good, you're sick or you just feel stuck, "\
						  "try to use a computer that writes it for you. This project generates an original piece of writing after being "  \
						  "trained using your existing scripts, therefore, the new piece will conserve your own writing style.",

						  "http://media3.giphy.com/media/kEKcOWl8RMLde/giphy.gif",
						  "",
						  "Technical description not available yet -",
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Scripts")

DL_project4 = media.Project("Machine Translation",

						  "Language is the backbone of our civilitation. Without written records of previous scientific discoveries, we could never "  \
						  "accomplish great events like traveling to space. We've accomplish a lot in the world where 13 of the most common languages "\
						  "are natively spoken by less than 50 percent of the population. What would the world be like if we could all work together " \
						  "without a language barrier?. This project is an English to French translator.",

						  "https://media.giphy.com/media/tu54GM19sqJOw/giphy.gif",
						  "",
						  "Technical description not available yet -",
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Translation")

DL_project5 = media.Project("New Faces Generator",

						  "Imagine you work for a movie production company, and your job is to design the characters in a movie. You would usually draw "  \
						  "a bunch of different concepts before arriving at the final design. What if you had a program that could do this for you?. This "\
						  "project generate new faces using celebrity images.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  "Technical description not available yet -",
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Faces")

AI_project1 = media.Project("The Sudoku Puzzle",

						  "Surely you have played Sudoku at least once in your life, Sudoku is that puzzle game that comes in magazines, newspapers, etc. "\
						  "The goal is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids that compose the "  \
						  "grid contains all of the digits from 1 to 9. Have you ever been stuck trying to solve one?. This project is a play-game agent " \
						  "for solve diagonal sudoku puzzles.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  "Technical description not available yet -",
						  "https://github.com/betogaona7/AI-projects/tree/master/AIND-Sudoku")

AI_project2 = media.Project("The Isolation Game",

						  "Isolation is a two-player game in which the players alternate turns moving a single piece from one cell to another on a board. "\
						  "Whenever either player occupies a cell, the cell becomes blocked for the remainder of the game. The first player with no "      \
						  "remaining legal moves loses, and the opponent is declared the winner. In this version each player is restricted to L-shaped "   \
						  "movements on a 7x7 board. This project is a game-playing agent to win the isolation game.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  "Technical description not available yet -",
						  "https://github.com/betogaona7/AI-projects/tree/master/AIND-Isolation")

AI_project3 = media.Project("Air Cargo Planner",

						  "Have you asked yourself how companies like DHL schedule all their shipments?, This project solves a group of problems for an "\
						  "Air Cargo transport system using a planning search agent, in which we see how an agent take advantage of the structure of a " \
						  "problem to construct a complex plan of action.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  "Technical description not available yet -",
						  "https://github.com/betogaona7/AI-projects/tree/master/AIND-Planning")

AI_project4 = media.Project("Sign Language Recognizer",

						  "According to the World Health Organization (WHO) 360 millon people worldwide have disabling hearing loss of which 70 million "\
						  "people use sign language as their first language. Now, how many interpreters are there? much less than half. In this project "\
						  "I built a system that can recognize words communicated using the American Sign Language (ASL).",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  """
						  The overall goal of this project was to built a word recognizer for American Sign Language video sequences, demonstrating
						  the power of probabilistic models. In particular, this project employs Hidden Marcov Models (HMMs)  that use a preprocessed
						  <a target='_blank' rel='noopener' href='http://www-i6.informatik.rwth-aachen.de/%7Edreuw/database-rwth-boston-104.php'>dataset</a> 
						  of tracked hand and nose positions extracted from video to identify individual words from test sequences.<br/><br/>

						  The next video is an example of how the hand locations are tracked:<br/><br/></p>
						  
						  <div style='text-align: center;'>
						  	<video controls>
						      	<source src='./img/Recognizer.mp4' type='video/mp4'>
						    </video>
						  </div><br/><br/><p>
						  
						  I experimented with four feature sets and three model selection methods (that is 12 possible combinations). The best combination
						  was features-ground (those are differences between hand and nose locations) with Selector CV (Log likelihood with Cross-validation folds) 
						  that gets a Word Error Rate (WER) of 53%. This can be improved by adding techniques like Context training, Statistical Grammar, 
						  State typing, Segmentally Boosted HMMs and probably many more that will help us obtain even lower WER.<br/><br/>
						  """,
						  "https://github.com/betogaona7/AI-projects/tree/master/AIND-Recognizer")

OWN_project1 = media.Project("Mariya",

						  "Taking advantage of technology and all available resources, we intend to put an end to the communication barrier between the "
						  "Wixarica (Huicholes) community and the rest of the world, seeking to rescue their stories and knowledge which they consider "
						  "sacred. Mariya is a translation device that seeks to save a Mexican culture.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "https://player.vimeo.com/video/195152250",

						  """<div style='text-align: center;'>
						  		<video controls poster='./img/huicholdos.png'>
                                <source src='./img/Mariya.mp4' type='video/mp4'>
                                </video>
                          	 </div><br/><br/><p>

						  A Mexican project that opens a communication portal between an indigenous community and the rest of the world. The Wixarikas
						  erroneously known as Huicholes are part of a Mexican town. Globally known for their art: The Huichol art.<br/> <br/>

						  Do you know that every piece of art they create really tells a story? each bracelet, each table, each figure tells something 
						  about their culture. Those stories create an identity for them. Through their tales, which have passed from generation to 
						  generation, they create a heritage to encourage new generations to follow in the footsteps of their ancestors.<br/> <br/>

						  Apart from facing the possible disapperence of their sacred land due mining, day by day they face a problem that goes unnoticed:
						  'migration'. Being located in the highest part of the Sierra Madre Occidental, communication and access to new technologies is 
						  almost impossible. This force the new generations to migrate to the big cities, confronting the language problem that threatens 
						  the extinction of their native language.<br/> <br/>

						  The Mariya project tries to demonstrate that the technology is not fought with the ancestral customs of a town, giving the floor
						  to those who deserve to be heard, seeking to rescue their stories and knowledge which they consider sacred.<br/> <br/>

						  Fall in love with the Wixarika culture with the documentary: <a target='_blank' rel='noopener' href='https://huicholesfilm.com/en/'>
						  Huicholes the last peyote guardians</a>.
						  <br/>Learn more about the Mariya project by visiting the <a target='_blank' rel='noopener' href='https://proyectomariya.github.io/'>
						  official website</a>.<br/><br/>""",
						  
						  "https://github.com/proyectomariya/translate")

"""
Un proyecto Mexicano que abre un portal de comunicacion entre una comunidad indigena y el resto del mundo. Los Wixaricas 
erroneamente conocidos como Huicholes son parte de un pueblo Mexicano, mundialmente conocidos por su arte: el arte huichol.
sabias tu que cada pieza de arte que ellos crean realmente cuenta una historia. cada pulsera, cada tabla, cada figura cuenta
algo de su cultura.

Esas historias les crean una identidad. A traves de sus cuentos, los cuales han pasado de generacion en generacion crean una 
herencia para incentivar a las nuevas generaciones a seguir los pasos de sus antepasados. 

Aparte de enfrentarse a la posible desaparecion de su tierra sagrada debido a la mineria canadiense, dia a dia se enfrentan a 
un problema que pasa desapercibido: "la migracion". Al estar asentados en lo mas alto de la Sierra madre occidental, la 
comunicacion y el acceso a las nuevas tecnologias les resulta casi imposible. Esto obliga a las nevas generaciones migrar a 
las grandes ciudades, enfrentandose con el problema del lenguaje que amenza con la extincion de su lengua materna. 

Proyecto Mariya pretende demostrar que la tecnologia no esta peleada con las costrumbres ancestrales de un pueblo, dandole la 
palabra a los que mrecen ser escuchados. buscando rescatar sus historias y conocimientos los cuales ellos consideran como 
sagrados.

Conoce mas sobre los huicholes con este interseante documental: https://huicholesfilm.com/en/'
Visita la pagina del dispositivo: https:projectomariya.github.io
"""
projectslist = [OWN_project1, DL_project1, AI_project4, AI_project3, DL_project3, DL_project5, AI_project2, AI_project1, DL_project2, DL_project4 ]
projects.open_project_page(projectslist)

