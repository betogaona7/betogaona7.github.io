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
						  """
						  Since humans started imagining machines moving around and interacting with the world, we have given them eyes. Look at 
						  <a target='_blank' rel='noopener' href='https://www.youtube.com/watch?v=ARJ8cAGm6JE'>HAL9000</a> from 2001: A space 
						  Odyssey. He is just one big eye.<br/><br/>

						  Today, we want automated cars to be able to distinguish between people, and trees, and the road. We are enabling our 
						  cars to do this using Covolutional Neural Networks (CNNs).<br/><br/>

						  Starting with the work of Yann LeCun in the late 90s, convolutional networks, typically shortened to cognets, gained 
						  popularity for detecting and recognizing hand written characters and images. In 2012 a huge dataset called ImageNet 
						  was released with 1,000 labeled categories and over a million training images. Alex Krizhevskys AlexNet, used a deep 
						  convolutional network trained on GPUs to achieve a 15% error rate on ImageNet, and this is easily beat the second best
						  attempt that had 26% errors.<br/><br/>

						  In this project I built a Convolutional Neural Network with TensorFlow and it recognize objects and images. Here I used 
						  the <a target='_blank' rel='noopener' href='https://www.cs.toronto.edu/~kriz/cifar.html'>CIFAR-10 dataset</a> which consists of 
						  60,000 images of ten different objects. This dataset is commonly used in computer vision research.<br/><br/>

						  The following image is an example of the predictions made by the network.<br/><br/></p>
						  <div style='text-align: center;'>
						  	<img src='./img/classifier.png' alt='CNN results'>
						  </div><br/><br/><p>
						  """,
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Classification")

DL_project3 = media.Project("TV Scripts Generator",

						  "The way to write a script for a TV show is to actually write a script. A pen is useful, typing is also good. "   \
						  "Keep putting words on the page, but if for some reason you don't feel good, you're sick or you just feel stuck, "\
						  "try to use a computer that writes it for you. This project generates an original piece of writing after being "  \
						  "trained using your existing scripts, therefore, the new piece will conserve your own writing style.",

						  "http://media3.giphy.com/media/kEKcOWl8RMLde/giphy.gif",
						  "",
						  """
						  This project generates Simpsons TV scripts. Specifically for a scene in the Moes tavern, using a Recurrent Neural Network (RNN) 
						  that was trained with a subset of the <a target='_blank' rel='noopener' href='https://www.kaggle.com/wcukierski/the-simpsons-by-the-data'>
						  Simpsons dataset </a> of scripts from 27 seasons. For example: <br/><br/></p>
						  <div style='text-align: center;'>
						  	<img src='./img/scripts-script.png' alt='Simpson script'>
						  </div><br/><br/><p>
						  It is okey if the TV script does not make much sense. The network was trained on less than a megabyte of text. In order to improve
						  results we need to use a smaller voacabulary or get more data. Luckly there is more data! As mentioned in the beginning, this is 
						  a subset of another database. Train on all the data would take too long. <br/><br/>
						  """,
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Scripts")
"""
This project generates Simpsons TV scripts. Specifically for a scene in the Moes tavern, using a Recurrent Neural Network (RNN) 
that was trained with a subset of the <a target='_blank' rel='noopener' href='https://www.kaggle.com/wcukierski/the-simpsons-by-the-data'>
Simpsons dataset </a> of scripts from 27 seasons. For example: <br/><br/></p>
<div style='text-align: center;'>
	<img src='./img/scripts-script.png' alt='Simpson script'>
</div><br/><br/><p>
It is okey if the TV script does not make much sense. The network was trained on less than a megabyte of text. In order to improve
results we need to use a smaller voacabulary or get more data. Luckly there is more data! As mentioned in the beginning, this is 
a subset of another database. Train on all the data would take too long. 


The network has only 2 layers because going deeper rarely helps much more (The exception are the Convolutional Neural Networks)
with Long Short Term Memory (LSTM) cells that are the basic unit in this kind of nets.
"""

DL_project4 = media.Project("Machine Translation",

						  "Language is the backbone of our civilitation. Without written records of previous scientific discoveries, we could never "  \
						  "accomplish great events like traveling to space. We've accomplish a lot in the world where 13 of the most common languages "\
						  "are natively spoken by less than 50 percent of the population. What would the world be like if we could all work together " \
						  "without a language barrier?. This project is an English to French translator.",

						  "https://media.giphy.com/media/tu54GM19sqJOw/giphy.gif",
						  "",
						  """
						  Take a peek into the realm of neural network machine translation. In this project I taught a sequence-to-sequence 
						  (seq2seq) model how to translate from one language to another training it on a dataset of English to French sentences.<br/><br/>

						  Recurrent Neural Networks (RNNs) are a powerful class of neural networks that deal with sequential data. They are
						  especially suited for language and translation tasks because they can extend to sequences of any length. But more 
						  importantly they share their parameters across different timesteps. So when they do learn a language model, they
						  do it a lot more efficiently than a traditional feedforward network would.<br/><br/>

						  The challenge with neural networks is to find the right dataset to feed your model and guide it through the
						  learning process.<br/><br/>

						  The seq2seq model can do amazing things. If you have a dataset with questions and answers you can make a Question-Answering model,
						  or if you have a dataset with new articles and their summaries you can make a summarization bot, or like in this project,
						  if you have a dataset with english phrases and french phrases you can make an English to French translator.<br/><br/></p>

						  <div style='text-align: center;'>
						  	<img src='./img/traductor-example.png' alt='English to French sentence'>
						  </div><br/><br/><p>

						  Since the dataset I used only has a vocabulary of 227 English words of thousands that you use, you are going to see good results
						  using these words. If you want to create a better translation model, you will need better data. You can train on the
						  <a target='_blank' rel='noopener' href='http://www.statmt.org/wmt10/'>WMT10 French-English courpus dataset</a>. 
						  This dataset has more vocabulary and richer in topics discussed, however, this will take 
						  you days to train, so make sure you have a GPU and the neural network is perfoming well on this dataset.<br/><br/> 
						  """,
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Translation")

DL_project5 = media.Project("New Faces Generator",

						  "Imagine you work for a movie production company, and your job is to design the characters in a movie. You would usually draw "  \
						  "a bunch of different concepts before arriving at the final design. What if you had a program that could do this for you?. This "\
						  "project generate new faces using celebrity images.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  """
						  This is a Generative Adversarial Network (GAN) that use the 
						  <a target='_blank' rel='noopener' href='http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html'>CelebFaces Attributes dataset (CelebA)</a> 
						  consisting of more than 200,000 of celebrity images with annotations as training to generate new images of faces.<br/><br/>

						  GANs are used for generating realistic data. The word adversarial in Generative Adversarial Networks means that we have two networks,
						  the generator and the discriminator which are in a competition with each other. The generator wants to minimize the value function 
						  and the discriminator wants to maximize the value function.<br/><br/> 

						  We can think of this process as being like a competition between counterfeiters and police. The generator net is like a group of
						  counterfeiters trying to produce fake money and pass it off as real. The police try to catch counterfeiters using fake money but
						  still want to let everyone else spend their real money. Over time the police get better at detecting counterfeit money and the 
						  conterfeiters get better at faking it. Eventually the counterfeiters are forced to make perfect replicas of real money.<br/><br/>

						  When we train a GAN on the CelebA dataset we can watch it being generating random images, gradually learn to generate faces. That is 
						  the basic idea of how GANs work.<br/><br/>

						  In the project CelebA images were cropped to remove parts of the image that do not include a face, then resized down to 28x28 pixels. 
						  The following image is an example of how the generated faces look.<br/><br/></p>

						  <div style='text-align: center;'>
						  	<img src='./img/faces-example.png' alt='Faces'>
						  </div><br/><br/><p>

						  Note that some faces look like horror movie characters!<br/><br/>
						  """,
						  "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Faces")

AI_project1 = media.Project("The Sudoku Puzzle",

						  "Surely you have played Sudoku at least once in your life, Sudoku is that puzzle game that comes in magazines, newspapers, etc. "\
						  "The goal is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids that compose the "  \
						  "grid contains all of the digits from 1 to 9. Have you ever been stuck trying to solve one?. This project is a play-game agent " \
						  "for solve diagonal sudoku puzzles.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  """
						  This project can solve any Sudoku puzzle, also have some extensions. The first extension is an implementation of the naked 
						  twins technique. The second is a modification to solve diagonal sudokus. <br/><br/>

						  The naked twins technique is the following. Consider the following puzzle, and look the two highlighted boxes, F3 and I3.<br/><br/></p>

						  <div style='text-align: center;'>
						  	<img class='sudoku-img' src='./img/naked-twins.png' alt='Naiked twins 1'>
						  </div><br/><br/><p>

						  As we can see, both belong to the same column, an both permit the values 2 and 3. Now, we do not know which one has a 2 and 
						  which one has a 3, but we know one thing for sure - the values 2 and 3 are locked in those two boxes, so no other box in their
						  same unit (the third column) can contain the values 2 or 3.<br/><br/>
						  Thus, we go over all the boxes in the same unit, and remove the values 2 and 3 from their possible values.<br/><br/></p>

						  <div style='text-align: center;'>
						  	<img class='sudoku-img' src='./img/naked-twins-2.png' alt='Naiked twins 2'>
						  </div><br/><br/><p>

						  As you can see, we've removed the values 2 and 3 from the boxes D3 and E3. This is naked twins techinique. A diagonal sudoku 
						  is like a regular sudoku, except that among the two main diagonals, the number 1 to 9 should all appear exactly once. The next
						  video is an example where the agent solves a diagonal sudoku.<br/><br/></p>

						  <div style='text-align: center;'>
						  	<video controls class='sudoku-vid'>
						  	  	<source src='./img/Sudoku.mp4' type='video/mp4'>
						  	</video>
						  </div><br/><br/><p>
						  """,
						  "https://github.com/betogaona7/AI-projects/tree/master/AIND-Sudoku")

AI_project2 = media.Project("The Isolation Game",

						  "Isolation is a two-player game in which the players alternate turns moving a single piece from one cell to another on a board. "\
						  "Whenever either player occupies a cell, the cell becomes blocked for the remainder of the game. The first player with no "      \
						  "remaining legal moves loses, and the opponent is declared the winner. In this version each player is restricted to L-shaped "   \
						  "movements on a 7x7 board. This project is a game-playing agent to win the isolation game.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  """
						  Game playing has long been one of the cornerstones of AI advancements. One of the biggest advancements in recent AI has been in this 
						  field through Googles Go winning AlphaGo AI. Similary, one of the seminal events of the 20th century was seeing IBMs Deep Blue defeat
						  Gary Kasparov, a world chess champion in a game of chess.<br/><br/>

						  In this project I designed and implemented a game-playing agent to play a game using adversarial search. The agent play Isolation. A 
						  two-player game in which the players alternate turns moving a single piece from one cell to another on the board. Whenever either player
						  occupies a cell, that cell becomes blocked for the remainder of the game. The first player with no remaining legal moves loses, and the
						  opponent is declared winner. Each player is restricted to L-shaped movements (like a knight in chess) on a 7 by 7 board, however, the 
						  player can jump blocked or occupied spaces (just like knight in chess).<br/><br/>

						  The goal was to program a player that beats its opponent consistently at this game. Additionally the agent have a fixed time limit each 
						  turn to search for the best move and respond. If the time limit expires during a players turn, that player forfeits the match, and the 
						  opponent wins.<br/><br/>

						  I used three different heuristics to perfom the adversarial search and compare their perfomance:<br/>
						  <ul type='disk'>
						  <li><p>The basic heuristic - Evaluate how good is the board for the player and how good it is for the opponent, then substract the opponents
						  score from the players. This heuristics would penalize our computer player with more potential moves which is counter productive, It 
						  continues to take into account boards where the current player can make a larger number of moves and also penalizes boards where the 
						  opponet can make a larger number of moves.</p></li>
						  <li><p>The lucky heuristic - This heuristic take into account the number of locations that are still available on the board, however this 
						  number do not reflect the goodness of the board but confirm the next statement: Both the number of open spaces and the number of moves
						  made are the same for every position for the same depth, thus any heuristic that relies only on these two exactly as effective (minus
						  very slight perfomance penalty) as a zero score function.</p></li>
						  <li><p>The coward heurisitc - It is called coward because the goal is get as far away from the opponent as possible, here is the otherwise of
						  the basic heuristic evaluation function.</p></li></ul><br/><br/><p>

						  In conclution the best was the basic heuristic because it obtains a better win rate, it is no computationally complex and it evaluate very well 
						  how the current board configuration is for our player.<br/><br/></p>

						  <div style='text-align: center;'>
						    <img src='./img/isolation.gif' alt='Isolation gif'>
						  </div><br/><br/><p>
						  """,
						  "https://github.com/betogaona7/AI-projects/tree/master/AIND-Isolation")

AI_project3 = media.Project("Air Cargo Planner",

						  "Have you asked yourself how companies like DHL schedule all their shipments?, This project solves a group of problems for an "\
						  "Air Cargo transport system using a planning search agent, in which we see how an agent take advantage of the structure of a " \
						  "problem to construct a complex plan of action.",

						  "https://media.giphy.com/media/TGHMbONT5eGgU/giphy.gif",
						  "",
						  """
						  In this project I defined a group of problems in classical PDDL (Planning Domain Definition Language) that use
						  a planning search agent to solve deterministic logistics problems for an Air Cargo transport system. For example
						  the next problem:</br></br></p>

						  <div style='text-align: center;'>
						  	<img src='./img/planner-problem.png' alt='Planner problem'>
						  </div><br/><br/><p>

						  Then setup the problems for search of two types: Non-heuristic searches and Heuristic searches. The non-heuristic
						  searches include Breadth-First search (BFS), Depth-First graph search (DFS) and Uniform-Cost search (UCS). Of them the most
						  efficient was the UCS algorithm.</br></br>

						  For the heuristic searches I used the A star algorithm (A*) with two different heuristics:</br></p>
						  <ul type='disk'>
						  	<li><p>Ignore preconditions heuristic - The minimum number of actions that must be carried out from the current state in order 
						  	to satisfy all of the goal conditions by ignoring the preconditions required for an action to be executed.</p></li>
						  	<li><p>Level sum heuristic - The sum of level costs of the individual goals (admissible if goals independent).</p></li>
						  </ul></br><p>
						  A* with ignore preconditions heuristic was the one that works best. The following image is the answer to the problem
						  posed in the previous image solved by both algorithms (A* and UCS):<br/><br/></p>

						  <div style='text-align: center;'>
						  	<img class='planner' src='./img/planner-solution.png' alt='Planner solution'>
						  </div><br/><br/><p>

						  UCS takes 157 seconds to solve it while A* only takes 30 seconds. That is one of the great advantages of using 
						  heuristics.<br/><br/>
						  """,
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

