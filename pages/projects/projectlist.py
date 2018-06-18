import media 
import projects

DL_project1 = media.Project("Bike Sharing Predictor",
	"Imagine yourself owning of a bike sharing company like CycleHop, and you want to predict how many bikes you need because "\
	"if you have too few, you're losing money from potential riders or vice versa if you have too many you're wasting money on "\
	"bikes that are just sitting around. This project predicts the number of bike-share users on a given day from historical data, "\
	"so you can know how many bikes you will need.",
	"https://media.giphy.com/media/l0HUiSjiHbUO24oGQ/giphy.gif",
	"",
	"""
	Bike sharing systems are a new generation of traditional bike rentals where the whole process of membership, rental and 
	return back has become automatic. They allow users to easily rent a bike from a particular position an return back to 
	another position. Currently, there are +500 bike-sharing programs around the world composed of over thousand bicycles.
	<br/><br/>

	This project is a simple feedforward neural network that predicts daily bike rental ridership. I used a
	<a target='_blank' rel='noopener' href='https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset'>dataset</a> that 
	has the number of riders for each hour of each day from January 1, 2011, to December 31, 2012, to train it. The data is 
	pretty complicated because the weekends have lower overall ridership and there are spikes when people are biking to and 
	from work during the week. Also, there is information about temperature, humidity, and wind speed. All of this likely 
	affect the number of riders.
	<br/><br/>

	The network has two layers: a hidden layer and an output layer. The hidden layer uses the sigmoid function for activations 
	while the output layer has only one node used for the regression. The output node is the same as the input node. That means, 
	the activation function is f(x) = x.
	<br/><br/>

	The following chart shows the network predictions compared with the actual data.
	<br/><br/>

	<div style='text-align: center;'>
		<img src='./img/bikeshare-graph.png' alt='Network prediction results' class='bikeshare-img'>
	</div><br/><br/>
	""",
	"https://github.com/betogaona7/DLNF-projects/blob/master/DLNF-BikeShare/DLND%20Your%20first%20neural%20network.ipynb")

DL_project2 = media.Project("Image Classification",
	"Vision is the main way in which humans gain information about the world, and with the passage of time, we have been able to "\
	"give eyes to machines. From that, amazing applications have been created. For example, a company called Orbital Insights analyzes "\
	"satellite imagery to count cars and oil tank levels automatically to predict such things as mall sales and oil production. In "\
	"this project, I developed a program that recognizes and identifies ten different types of objects in images.",
	"https://media.giphy.com/media/l0HU1QXrScjR6PUdi/giphy.gif",
	"",
	"""
	Since humans started imagining machines moving around and interacting with the world, we have given them eyes. Look at
	<a target='_blank' rel='noopener' href='https://www.youtube.com/watch?v=ARJ8cAGm6JE'>HAL9000</a> from 2001: A Space Odyssey. 
	He is just one big eye.
	<br/><br/>

	Today, we want automated cars to be able to distinguish between people, trees, and the road. We are enabling our cars to do this
	using convolutional neural networks.
	<br/><br/>

	Starting with the work of Yann LeCun in the late 90s, convolutional networks, typically shortened to cognets, gained popularity 
	for detecting and recognizing handwritten characters and images. In 2012 a huge dataset called ImageNet was released with 1,000 
	labeled categories and over a million training images. Alex izhevsky s AlexNet used a deep convolutional network trained on GPUs 
	to achieve a 15% error rate on ImageNet, and this is easily beat the second best attempt that had 26% errors.
	<br/><br/>

	Using the TensorFlow framework, I built a convolutional neural network which recognizes objects and images.  To train the model I 
	used the <a target='_blank' rel='noopener' href='https://www.cs.toronto.edu/~kriz/cifar.html'>CIFAR-10 dataset</a> which consists 
	of 60,000 images of ten different objects. This dataset is commonly used in computer vision research.
	</br></br>

	The following image is an example of the predictions made by the network.<br/><br/></p>
	<div style='text-align: center;'>
		<img src='./img/classifier.png' alt='CNN results' class='classification-img'>
	</div><br/><br/><p>
	""",
	"https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Classification")

DL_project3 = media.Project("TV-Scripts Generator",
	"The way to write a script for a TV show is actually to write a script. A pen is useful and typing is also good. Keep "\
	"putting words on the page, but if for some reason you aren't feeling good, you're sick, or you just are stuck, then "\
	"why not try to use a computer capable of writing the script for you?.  This project generates an original piece of "\
	"writing using your existing scripts, therefore the new piece will conserve your own writing style.",
	"https://media.giphy.com/media/l0HU7Ik9NfAnoWq9q/giphy.gif",
	"",
	"""
	This project generates Simpsons TV scripts, specifically for a scene in the Moes tavern, using a recurrent neural network (RNN).
	</br></br>

	To train the network I used a small subset of the <a target='_blank' rel='noopener' href='https://www.kaggle.com/wcukierski/the-simpsons-by-the-data'> 
	Simpsons dataset </a> which contains scripts from 27 seasons. 
	<br/><br/>

	The following image in an example of the network output: 
	<br/><br/></p>

	<div style='text-align: center;'>
		<img src='./img/scripts-script.png' alt='Simpson script' class='scripts-img'>
	</div><br/><br/><p>

	NOTE: For the purpose of this project, it is okay if the TV script does not make much sense since the network was trained on less 
	than a megabyte of text. In order to improve results, we need to use a smaller vocabulary or get more data. Luckily there is more 
	data, but train on it would take too long.
	<br/><br/>
	""",
	"https://github.com/betogaona7/DLNF-projects/blob/master/DLNF-Scripts/dlnd_tv_script_generation.ipynb")

DL_project4 = media.Project("Machine Translation",
	"Language is the backbone of our civilization. Without written records of previous scientific discoveries, we could never "\
	"accomplish great events like traveling to space. We've accomplished a lot in the world where 13 of the most common languages "\
	"are natively spoken by less than 50 percent of the population, so what would the world be like if we could all work together "\
	"without the language barrier?. This project translates sentences from English to French.",
	"https://media.giphy.com/media/l0HU3pdWVTEz8qPCM/giphy.gif",
	"",
	"""
	Take a peek into the realm of neural network machine translation. In this project, I taught a sequence-to-sequence 
	(seq2seq) model how to translate from one language to another training it on a dataset of English to French sentences.
	<br/><br/>

	Recurrent Neural Networks (RNNs) are a powerful class of neural networks that deal with sequential data. They are
	especially suited for language and translation tasks because they can extend to sequences of any length. But more 
	importantly, they share their parameters across different timesteps. So when they do learn a language model, they do it 
	a lot more efficiently than a traditional feedforward network would.<br/><br/>

	The challenge with neural networks is to find the right dataset to feed your model and guide it through the learning 
	process.<br/><br/>

	The seq2seq model can do amazing things. If you have a dataset with questions and answers you can make a 
	Question-Answering model, or if you have a dataset with new articles and their summaries you can make a summarization bot, 
	or like in this project, if you have a dataset with English phrases and French phrases you can make an English to French 
	translator.<br/><br/></p>

	<div style='text-align: center;'>
		<img src='./img/traductor-example.png' alt='English to French sentence' class='translation-img'>
    </div><br/><br/><p>

    Since the dataset I used only has a vocabulary of 227 English words of thousands that you use, you are going to see 
    good results using these words. If you want to create a better translation model, you will need better data. You can train 
    on the <a target='_blank' rel='noopener' href='http://www.statmt.org/wmt10/'>WMT10 French-English corpus dataset</a>. 
    This dataset has more vocabulary and richer in topics discussed, however, this will take you days to train, so make sure 
    you have a GPU and the neural network is performing well on this dataset. <br/><br/>
    """,
    "https://github.com/betogaona7/Deep-Learning/tree/master/DLNF-Translation")

DL_project5 = media.Project("New Faces Generator",
	"Imagine you work for a movie production company, and your job is to design the characters in a movie. You would usually "\
	"draw a bunch of different concepts before arriving at the final design. What if you had a program that could do this for "\
	"you?. This project uses celebrity images to generate new images of faces.",
	"https://media.giphy.com/media/l49JYD8R8W6RtOUBa/giphy.gif",
	"",
	"""
	This project is a deep convolutional generative adversarial network (DCGAN) that generates new face images. The DCGAN was 
	training with the <a target='_blank' rel='noopener' href='http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html'>CelebFaces Attributes 
	dataset </a> (CelebA) that consists of more than 200,000 celebrity images with annotations.
	</br></br>

	Generative adversarial networks are used to generate realistic data. The word adversarial means that we have two networks: 
	a generator and a discriminator, and those networks are competing with each other. The generator wants to minimize the value 
	function, and the discriminator wants to maximize the value function. 
	</br></br>

	We can think about this process as being like a competition between counterfeiters and police. The generator net is like a 
	group of counterfeiters trying to produce fake money and pass it off as real. The police try to catch counterfeiters using 
	fake money but still want to let everyone else spend their real money. Over time the police get better at detecting counterfeit 
	money, and the counterfeiters get better at faking it. Eventually, the counterfeiters are forced to make perfect replicas of 
	real money.
	</br></br>

	The following image is an example of how the generated faces look for this project.<br/><br/></p>

	<div style='text-align: center;'>
		<img src='./img/faces-example.png' alt='Faces'>
	</div><br/><br/><p>

	Note that some faces look like horror movie characters! The network ran for only one epoch so to get state-of-art images you 
	need to increment the number of epochs. It will take around 20 minutes on an average GPU to run each one. 
	</br></br>
	""",
	"https://github.com/betogaona7/DLNF-projects/blob/master/DLNF-Faces/dlnd_face_generation.ipynb")

AI_project1 = media.Project("AI Agent to solve Sudoku puzzles",
	"Surely you have played Sudoku at least once in your life. Sudoku is that puzzle game that comes in magazines, newspapers, "\
	"etc. The goal is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 sub-grids that "\
	"compose the grid contains all of the digits from 1 to 9. Have you ever been stuck trying to solve one?. This a play-game "\
	"agent to solve diagonal sudoku puzzles.",
	"https://media.giphy.com/media/3o751YzOR1rXv8FVTO/giphy.gif",
	"",
	"""
	This project can solve any Sudoku puzzle, and it also has some extensions. The first extension is an implementation of the 
	naked twins technique. The second is a modification to solve diagonal sudokus. 
	<br/><br/>

	The naked twins technique is the following. Consider the following puzzle, and look at the two highlighted boxes, F3 and I3.
	<br/><br/></p>

	<div style='text-align: center;'>
		<img class='sudoku-img' src='./img/naked-twins.png' alt='Naiked twins 1'>
	</div><br/><br/><p>

	As we can see, both belong to the same column, and both permit the values 2 and 3. Now, we do not know which one has a 2 and 
	which one has a 3, but we know one thing for sure - the values 2 and 3 are locked in those two boxes, so no other box in their 
	same unit (the third column) can contain the values 2 or 3.
	</br></br>

	Thus, we go over all the boxes in the same unit and remove the values 2 and 3 from their possible values.
	<br/><br/></p>

	<div style='text-align: center;'>
		<img class='sudoku-img' src='./img/naked-twins-2.png' alt='Naiked twins 2'>
	</div><br/><br/><p>

	As you can see, we've removed the values 2 and 3 from the boxes D3 and E3. This is the naked twins technique. The diagonal 
	sudoku is like the regular sudoku, except that both main diagonals have to have each digit once, just like columns and rows.
	</br></br>

	The following video shows the agent solving an example of diagonal sudoku.<br/><br/></p>

	<div style='text-align: center;'>
		<video controls class='sudoku-vid'>
			<source src='./img/Sudoku.mp4' type='video/mp4'>
		</video>
	</div><br/><br/><p>
	""",
	"https://github.com/betogaona7/AI-projects/tree/master/AIND-Sudoku")

AI_project2 = media.Project("Isolation Game-Playing Agent",
	"Isolation is a two-player game in which the players alternate turns moving a single piece from one cell to another on the "\
	"board. Whenever either player occupies a cell, the cell becomes blocked for the remainder of the game. The first player with "\
	"no remaining legal moves loses, and the opponent is declared the winner. In this version, each player is restricted to L-shaped "\
	"movements on a 7x7 board. This project is an AI agent that beats humans in Isolation game.",
	"https://media.giphy.com/media/3o752fb9nnFM3P7JOo/giphy.gif",
	"",
	"""
	Game playing has long been one of the cornerstones of AI advancements. One of the biggest advancements in recent AI has been in 
	this field through Google s AlphaGo AI. Similarly, one of the seminal events of the 20th century was seeing IBMs Deep Blue defeated 
	Gary Kasparov, a world chess champion in a game of chess.
	<br/><br/>

	In this project, I designed and implemented a game-playing agent to play a game using adversarial search. The agent play Isolation. 
	A two-player game in which the players alternate turns moving a single piece from one cell to another on the board. Whenever either 
	player occupies a cell, that cell becomes blocked for the remainder of the game. The first player with no remaining legal moves loses, 
	and the opponent is declared the winner. Each player is restricted to L-shaped movements (like a knight in chess) on a 7 by 7 board, 
	however, the player can jump blocked or occupied spaces (just like a knight in chess).
	<br/><br/>

	The goal was to program a player that beats its opponent consistently at this game. Additionally, the agent has a fixed time limit 
	each turn to search for the best move and respond. If the time limit expires during a players turn, that player forfeits the match, 
	and the opponent wins.
	<br/><br/>

	I used three different heuristics to perform the adversarial search and compare their performance:<br/>

	<ul type='disk' class='popup-list'>
		<li>
			<p>The basic heuristic - It evaluates how good is the board for the player and how good it is for the opponent, then subtract 
			the opponents score from the players. This heuristics would penalize our computer player with more potential moves which are 
			counterproductive. It continues to take into account boards where the current player can make a larger number of moves and also 
			penalizes boards where the opponent can make a larger number of moves.</p>
		</li>
		<li>
			<p>The lucky heuristic - This heuristic takes into account the number of locations that are still available on the board, however, 
			this number does not reflect the goodness of the board but confirm the next statement: Both, the number of open spaces and the number 
			of moves made are the same for every position for the same depth, thus any heuristic that relies only on these two exactly as 
			effective (minus very slight performance penalty) as a zero score function.</p>
		</li>
		<li>
			<p>The coward heuristic - It was called coward because the goal is to get as far away from the opponent as possible, here is the 
			otherwise of the basic heuristic evaluation function.</p>
		</li>
	</ul><br/><br/><p>

	In conclusion, the best was the basic heuristic because it obtains a better win rate, it is no computationally complex and it evaluates very 
	well how the current board configuration is for our player.<br/><br/></p>

	<div style='text-align: center;'>
		<img src='./img/isolation.gif' alt='Isolation gif' class='isolation-img'>
    </div><br/><br/><p>
    """,
    "https://github.com/betogaona7/AI-projects/tree/master/AIND-Isolation")

AI_project3 = media.Project("Air Cargo Planner",
	"Have you asked yourself how companies like DHL schedule all their shipments?, This project solves a group of problems "\
	"for an Air Cargo transport system using a planning search agent, in which we see how an agent take advantage of the "\
	"structure of a problem to construct a complex plan of action.",
	"https://media.giphy.com/media/l0HUo260gjOsknsY0/giphy.gif",
	"",
	"""
	In this project, I defined a set of air-cargo domain problems in the classical planning domain definition language (PDDL) and 
	implemented two different heuristics for a search algorithm. Then with an implementation of a planning graph ran six different 
	search algorithms selecting the best one and used it to solve successfully the problems finding the most efficient path to route 
	cargo around the world. For example, look the next problem:
	</br></br></p>

	<div style='text-align: center;'>
		<img src='./img/planner-problem.png' alt='Planner problem' class='planner-img'>
	</div><br/><br/><p>

	After defining it in the PDDL, set up the problems for the search of two types: Non-heuristic searches and Heuristic searches. 
	The non-heuristic searches include Breadth-First search (BFS), Depth-First graph search (DFS) and Uniform-Cost search (UCS). Of 
	them, the most efficient was the UCS algorithm.
	</br></br>

	For the heuristic searches, I used the A* algorithm with two different heuristics:</br></p>
	<ul type='disk' class='popup-list'>
		<li>
			<p>Ignore preconditions heuristic - The minimum number of actions that must be carried out from the current state 
			in order to satisfy all of the goal conditions by ignoring the preconditions required for an action to be executed.</p>
		</li>
		<li>
			<p>Level sum heuristic - The sum of level costs of the individual goals (admissible if goals are independent).</p>
		</li>
	</ul></br><p>
	
	A* with the ignore preconditions heuristic was the one that works best. The following image is the answer to the problem 
	posted in the previous image solved by both algorithms (A* and UCS):
	<br/><br/></p>

	<div style='text-align: center;'>
		<img class='planner' src='./img/planner-solution.png' alt='Planner solution'>
	</div><br/><br/><p>

	UCS took 157 seconds to solved it while A* only took 30 seconds. That is one of the great advantages of using heuristics.
	</br></br>
	""",
	"https://github.com/betogaona7/AI-projects/tree/master/AIND-Planning")

AI_project4 = media.Project("American Sign Language Recognizer",
	"According to the World Health Organization (WHO), 360 million people worldwide have disabling hearing loss of which 70 million people "\
	"use sign language as their first language. Now, how many interpreters are there? much less than half, so in this project, I built a "\
	"word recognizer for American Sign Language (ASL) video sequences.",
	"https://media.giphy.com/media/xULW8BRAEkxshqm02Q/giphy.gif",
	"",
	"""
	The overall goal of this project was to build a word recognizer for American Sign Language video sequences, demonstrating
	the power of probabilistic models. In particular, this project employs Hidden Markov Models (HMMs)  that use a 
	preprocessed 
	<a target='_blank' rel='noopener' href='https://www-i6.informatik.rwth-aachen.de/%7Edreuw/database-rwth-boston-104.php'>
	dataset</a> of tracked hand and nose positions extracted from video to identify individual words from test sequences.<br/><br/>

	The next video is an example of how hand locations are tracked:<br/><br/></p>

	<div style='text-align: center;'>
		<video controls>
			<source src='./img/Recognizer.mp4' type='video/mp4'>
		</video>
	</div><br/><br/><p>

	To build the word recognizer for ASL video sequences, I experimented with four feature sets and three model selection criteria 
	methods (that is 12 possible combinations). The best combination was the feature set: features-ground (those are differences 
	between hand and nose locations) with the Selector CV (Log likelihood with Cross-validation folds). It got a word error rate 
	(WER) of 53%. This can be improved by adding techniques like context training, statistical grammar, state typing, segmentally 
	boosted HMMs, and many more that help us to obtain even a lower WER.
	</br></br>
	""",
	"https://github.com/betogaona7/AI-projects/tree/master/AIND-Recognizer")

AI_project5 = media.Project("Facial Key-Points Detector",
	"Predict key-point positions on face images can be the building block in several applications, such as tracking faces in images "\
	"and video, analyzing facial expressions, detecting dysmorphic facial signs for medical diagnosis, performing face recognition, "\
	"etc. This project is a recognition system that takes in any image containing faces and identifies the location of each face and their "\
	"facial key-points.",
	"./gifs/Face.png",
	"",
	"""
	Facial keypoints recognition systems are used in many applications, from facial tracking to emotion recognition. These key points include 
	points around eyes, nose, and mouth for example.
	</br></br>

	In this project, I explored a few of the many computer vision algorithms built into the OpenCV library like Haar 
	feature-base cascade classifier to detect human faces in images. Also, I built and trained a convolutional neural 
	network to recognize patterns in images and learn how to identify key points given sets of label data.
	</br></br>

	The following figure shows the model s predicted key points on a subset of the testing images.<br/><br/></p>

	<div style='text-align: center;'>
		<img class='keypoints-img' src='./img/cnnkeypoints.png' alt='CNNs output example'>
	</div><br/><br/><p>

	At the end, I combined all to implement the facial key points recognition system, that is:</br></p>
	<ul type='disk' class='popup-list'>
		<li><p> Accept a color image. </p></li>
		<li><p> Convert the image to grayscale. </p></li>
		<li><p> Detect and crop the face(s) contained in the image. </p></li>
		<li><p> Locate the facial key points in the cropped image. </p></li>
		<li><p> Overlay the facial key points in the original (color, uncropped) image.</li>
	</ul></br><p>

	As a result, this system takes in any image containing faces and identifies the location of each face and their 
	facial key-points.
	</br></br>

	The following image is an example of the final result. </br></br></p>

	<div style='text-align: center;'>
		<img src='./img/facialrecognition.png' alt='Facial recognition result' class='facialrecognition-img'>
    </div><br/><br/><p>
	""",
	"https://github.com/betogaona7/AIND-projects/blob/master/AIND-CV-FacialKeypointDetection/CV_project.ipynb")

AI_project6 = media.Project("EN-FR translator",
	"Language is the backbone of our civilization. Without written records of previous scientific discoveries, we could never "\
	"accomplish great events like traveling to space. We've accomplished a lot in the world where 13 of the most common languages "\
	"are natively spoken by less than 50 percent of the population, so what would the world be like if we could all work together "\
	"without the language barrier?. This project translates from English to French.",
	"https://media.giphy.com/media/l0HU3pdWVTEz8qPCM/giphy.gif",
	"",
	"""
	Recurrent Neural Networks (RNNs) are a powerful class of neural networks that deal with sequential data. They are especially 
	suited for language and translation tasks because they can extend to sequences of any length. But more importantly, they share 
	their parameters across different timesteps. So when they do learn a language model, they do it a lot more efficiently than a 
	traditional feedforward network would.
	</br></br>

	To built the EN-FR translator, I used a small dataset which contains English sentences with their French translations to train a 
	deep learning model.
	</br></br>

	For that, I converted the text into sequences of integers tokenizing words into ids and adding padding to make all the sequences 
	the same length. 
	</br></br>

	Then experimented and compared the performance of four different neural networks architectures:</br></p>

	<ul type='disk' class='popup-list'>
		<li><p> Simple RNN. </p></li>
		<li><p> RNN with Embedding. </p></li>
		<li><p> Bidirectional RNN. </p></li>
		<li><p> Encoder-Decoder RNN. </p></li>
	</ul></br><p>

	To design a deeper architecture, a bidirectional RNN with embedding, that outperforms all the last models. 
	</br></br>

	The following image shows an example of the translator output where each sample contains two sentences: the first one is the correct 
	translation and the second is the translation generated for the model. The first sample translates: <i> He saw an old yellow truck. </i> And 
	the second one translates: <i> new jersey is sometimes quiet during autumn , and it is snowy in april. </i>
	</br></br></p>

	<div style='text-align: center;'>
		<img class='translator-result-img' src='./img/translatorresults.png' alt='RNNs output example'>
	</div><br/><br/><p>

	NOTE: since the dataset I used only has a vocabulary of 227 English words of thousands that you use, you are going to see good results using 
	these words. If you want to create a better translation model, you will need better data. You can train it on the 
	<a target='_blank' rel='noopener' href='http://www.statmt.org/wmt10/'>WMT10 French-English corpus dataset</a>. This dataset has more 
	vocabulary and richer in topics discussed, however, this will take you days to train, so make sure you have a GPU.
	<br/><br/>
	""",
	"https://github.com/betogaona7/AIND-projects/blob/master/AIND-NLP-MachineTranslation/machine_translation.ipynb")

AI_project7 = media.Project("DNN Speech Recognizer",
	"A voice user interface is a speech platform that enables humans to communicate with machines by voice, and there are a lot of "\
	"applications, for example a text transcriber, which is three times faster than typing. This project converts audio sound waves "\
	"into language text completing a part of end-to-end automatic speech recognition (ASR) pipeline.",
	"./gifs/Speech.png",
	"",
	"""
	This project is an acoustic model that converts audio sound waves into language text. The raw audio is converted to a feature 
	representation as a preprocessing step. 
	</br></br>

	There are two audio representations used in this project: a normalized spectrogram which speeds the convergence of the network 
	and the normalized Mel-Frequency Cepstral Coefficients(MFFCs) that is a more lower-dimensional audio representation that the 
	spectrogram.
	</br></br>

	Using a small subset of the <a target='_blank' rel='noopener' href='http://www.danielpovey.com/files/2015_icassp_librispeech.pdf'>
	LibreSpeech</a> dataset, which contains a large corpus of English-read speech, I experimented with five 
	different model architectures and evaluated their performance: 
	</br></br></p>

	<ul type='disk' class='popup-list'>
		<li><p> Model 0: A simple RNN. </p></li>
		<li><p> Model 1: RNN + TimeDistributed Dense. </p></li>
		<li><p> Model 2: CNN + RNN + Timeistributed Dense. </p></li>
		<li><p> Model 3: Deeper RNN + TimeDistributed Dense. </p></li>
		<li><p> Model 4: Bidirectional RNN + TimeDistributed Dense.</li>
	</ul></br>

	<div style='text-align: center;'>
		<img src='./img/acousticmodelsperfomance.png' alt='Acoustic models performance' class='aco-performance-img'>
    </div><br/><br/>

    <div style='text-align: center;'>
		<img src='./img/acousticmodelstable.png' alt='Acoustic models comparission' class='aco-comparission-img'>
    </div><br/><br/><p>

    The model 4 was the best of the five for this acoustic modeling task.  After that, I used what I learned to draft my architecture:
    </br></br></p>
    <ul class='popup-list'>
    	<li><p> Final Model: CNN + Dropout + RNN + TimeDistributed dense. </p></li>
    </ul><p>

    Since spectrograms or MFFCs features are visual representations of speech, a CNN is perfect to find their patterns. The dropout 
    helps with the overfitting problem and the RNN** tracks series of data through memory, and temporary memory is an important 
    characteristic for training and decoding speech.
    </br></br>

    ** Bidirectional RNN work better but add complexity, therefore, double the training time, so in this case, I sacrificed a little 
    more precision for less time of training. 
    </br></br>

    Compared with model 4, the final architecture reached 19% less validation loss in only one-third of the time. The following image 
    shows an output example of the final model.
    </br></br></p>

    <div style='text-align: center;'>
		<img src='./img/acousticmodeloutput.png' alt='Acoustic model output example' class='aco-outexample-img'>
    </div><br/><br/><p>

    NOTE: This can be improved by download more data and train bigger, deeper models. But beware - the model will likely take a long 
    while to train (days, even weeks on a single GPU).
    </br></br>
	""",
	"https://github.com/betogaona7/AIND-projects/blob/master/AIND-VUI-SpeechRecognition/vui_notebook.ipynb")

OWN_project1 = media.Project("Mariya",
	"The Wixaricas, an indigenous Mexican community, face a communication problem that obliges their new generations to migrate to "\
	"the big cities and to confront with the language problem which threatens the extinction of their native language. Mariya project "\
	"intends to put an end to their communication barrier through a translator device and help them to preserve their culture and to "\
	"rescue their stories and knowledge.",
	"./gifs/Mariya.png",
	"https://player.vimeo.com/video/195152250",
	"""
	</p><div style='text-align: center;'>
		<video controls poster='./img/huicholdos.png'>
			<source src='./img/Mariya.mp4' type='video/mp4'>
		</video>
	</div><br/><br/><p>

	Have you ever seen a piece of Huichol art?  Did you know that each piece of Huichol art tells a story?. Those 
	stories create an identity for the Wixarica, erroneously known as Huichol, community. Through their tales, which 
	have been passed from generation to generation, they create a heritage to encourage new generations to follow in 
	the footsteps of their ancestors.
	<br/><br/>

	Nowadays, the Wixarica community is facing a migration problem. They are located in the highest part of the Sierra 
	Madre Occidental where communication and access to new technologies are almost impossible. This forces new 
	generations to migrate to the big cities confronting the language problem that threatens the extinction of their 
	native language.
	<br/><br/>

	Mariya project aims at opening a communication portal between the Wixaricas and the rest of the world through 
	a translator device. It demonstrates that technology is not fought with ancestral customs of a town giving the 
	floor to those who deserve to be heard and rescuing their stories and knowledge which they consider sacred.
	<br/> <br/>

	Fall in love with the Wixarika culture with the documentary: 
	<a target='_blank' rel='noopener' href='https://huicholesfilm.com/en/'>
	Huicholes the last peyote guardians</a>.
	<br/>Learn more about the Mariya project by visiting the 
	<a target='_blank' rel='noopener' href='https://proyectomariya.github.io/'> official website</a>.<br/><br/>
	""",
	"https://github.com/proyectomariya/translate/blob/master/translate.py")

#projectslist = [OWN_project1, AI_project5, AI_project6,	AI_project7, DL_project1, AI_project4, AI_project3, DL_project3, DL_project5, AI_project2, AI_project1, DL_project2]
projectslist = [OWN_project1, AI_project5, AI_project6,	AI_project7, AI_project4, AI_project3, AI_project2, AI_project1, DL_project5, DL_project3, DL_project2, DL_project1]
projects.open_project_page(projectslist)

