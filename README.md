![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<h1>Portfolio_Project_4 --- FullStack_Toolkit</h1>
<h1>......</h1>
<p>breif description of the website and what it is about.... 
The aim of the website is to.....</p>

click here to go to the deployed website: <a href="#" target="_blank">"WEBSITE</a>
<br><br>

![image](...)

# Contents

* [**User Experience UX**](<#User-Experience>)
    * [User Stories](<#User-Stories>)
    * [Wireframes](<#Wireframes>)
    * [Site Structure](<#Site-Structure>)
* [**Design Stylings**](<#Design-Stylings>)
    * [ColourScheme](<#Colour-Scheme>)
    * [Fonts](<#Fonts>)
* [**Features**](<#Features>)
    * [Existing Features](<#Existing-Features>)
    * [Future Features](<#Future-features>)
* [**Data Model**](<#Data-Model>)
* [**Testing**](<#testing>)
    * [Bugs](<#bugs>)
    * [Solved Bugs](<#solved-bugs>)
    * [Validation Testing](<#validation-testing>)
* [**Technologies Used**](<#technologies-used>)
* [**Deployment**](<#deployment>)
    * [Deployment of the project](<#deployment-of-the-project>)
    * [Cloning of the project](<#cloning-of-the-project>)
* [**Credits**](<#Credits>)
* [**Acknowledgements**](<#acknowledgements>)


# User Experience UX
<hr>

## Colour Scheme
the colour scheme chosen for this website is sutble and chicque, requested by the client that it will have light tones to exert a professional look that is not overpowering to the views and that it is to be inviting to anyone who visits the site.
  - The blue tone colour settled upon is aliceblue which is a nice colour that gives some personaliry to website other than a standard white background.
  - The pink tone colour settled upon is mistyrose which is a beautiful light pink that really compliments the background colour.
  - The pink tones also come with some shadowing to give a bit more flair and dynamics to the buttons and icons.

[Back to Top](<#contents>)
<br>

## Fonts
The fonts applied are really important to the websites appeal. The main font for the website's title was requested by the client to be eye-catching and refined, but at the sametime be strong and elegant. The font settled up was "Playfair Display" an it really ticks all the boxes.

The second font for the general font for the website which was settled on which complements the title font was "Zilla Slab". It works well as it doesn't draw away from the attention of the main font and is easy to read but still is attractive to the users. 

[Back to Top](<#contents>)
<br>

# Design Stylings
<hr>

## User Stories
Provide a user stories table here or list of the general user stories

[Back to Top](<#contents>)
<br>

## Wire Frames
Provide some images of wireframe models for the website display and a brief description

[Back to Top](<#contents>)
<br>

# Features
<hr>

## Existing Features

feature 1:

![image]("link")

feature 2:

![image]("link")


<ul>
    <li>...</li>
    <li>...</li>
    <li>...</li>
</ul>

![image]()

<ul>
    <li>...</li>
</ul>

<li>Input Validation and checking</li>
<ul>
    <li>...</li>
</ul>

![image]()

<li>...</li>
<ul>
    <li>...</li>
    <li>...</li>
</ul>

<li>...</li>
<br>
    
[Back to Top](<#contents>)

## Data Model

Here you can find the logical flow chart that I made to help me create the data model... <a href="link" target="_blank">link tag</a>. This was really useful in helping me understand the flow and direction on how to create the app and models, views and templates... etc... something along these lines
<br>

[Back to Top](<#contents>)

### Features left to implement

This can be a list of unfinished or future new user stories on how to improve the website
<li>...</li>

<br>

[Back to Top](<#contents>)
<br>

# Testing

To test my project, I have manually tested the project by doing the following:
<ul>
    <li>
        Testing the programs code in <a href="http://pep8online.com/" target="_blank">pep8online</a> and confirmed that there were no errors with the code.
    </li>
    <li>
        Tested the validations to prove the program is working correctly by entering invalid inputs and checking that all error types are accounted for (outside size of board parameters, same input cannot be inputted twice and strings are not excepted).
    </li>
    <li>
        Tested in the local terminal and the Code institute Heroku Terminal.
    </li>
</ul>

![image]()

[Back to Top](<#contents>)
<br>

## Bugs

### Solved Bugs

<ul>
    <li>I created a validation for checking if the guess made ca be found in the guesses but I didnt pass this validation into the code for the computers turn. This showed up that the
    computer was hitting targets it has already shot and missed. resulting in an unbalanced and unfair game experience wereby the user can have a greater chance at winning then the computer.</li>
</ul>

[Back to Top](<#contents>)
<br>

### Unsolved Bugs

<p>There are no unfixed bugs found on the project.</p>
<br>

[Back to Top](<#contents>)
<br>

## Technologies Used

<li><a href="https://github.com/" target="_blank">GitHub</a> - The site was used to edit and host the website.</li>
<li><a href="https://gitpod.io/projects" target="_blank">GitPod</a> - Used in the deployment and creating the website.</li>
<li><a href="https://www.python.org/" target="_blank">Python</a> - This was used in the production to get the game running as it is required for the app to run.</li>
<li><a href="https://nodejs.org/en/" target="_blank">Node.js</a> - This was used in the production to get the game running as it is required for app to run.</li>
<li><a href="http://pep8online.com/" target="_blank">pep8online</a> - This site was used to validate the python code to check for any errors within my writing.</li>
<li><a href="https://www.heroku.com/" target="_blank">Heroku</a> - This was used to deploy the game in a mock terminal that allows anyone to play the game online.</li>
<li><a href="https://docs.python.org/3/library/random.html" target="_blank">Python Libary Random</a> - This was used to generate random numbers within the games code for deployment of the ships or the computers random guesses.</li>

LIST A BUNCH OF NEW TECHNOLOGIES AND PYTHON PACKAGES USED... DJANGO AND etc...

<br>

[Back to Top](<#contents>)
<br>

## Deployment

### Deployment of the project

<p> I deployed this site using Heroku which is a container based cloud platform where you can deploy, manage and scale applications. To deploy this project I used the following steps in Heroku:</p>
<li>Fork or clone a copy of this repository.</li>
<li>Log in or create an account in heroku.</li>

![image]("")

<li>click on the button in the right corner to create a new app.</li>

![image]()

<li>inside the app page, go to setting page (underlined in green) and set the buildpacks to "Python" and "Nodejs" in that order (like in the picture below).</li>

![image]()

<li>Link the heroku app to the repository.</li>
<li>Go back to the deploy page (underlined in yellow) and you can either choose to manually deploy the site or automatically.</li>
<li>Once it has deployed, it may take a fww minutes to load and you can play the game.</li>

<br>
<p>The link to the site can be found here - <a href=" link here " target="_blank">LINK HERE!!!!</a></p>

<br>

!!!! REMOVE DEBUG FROM TRUE TO FALSE BEFORE SUBMISSION !!!

[Back to Top](<#contents>)

<br>

### Cloning of the Project
<hr>
<p>To create a local clone of the project, follow the steps below:</p>
<ol>
    <li>In the GitHub repository, under the repository name there is a code tab., click on the <b>code</b> tab.</li>
    <li>In the clone tab, click the HTTPS tab. Within this section, click on the clipboard icon and copy the URL supplied for the repository.</li>
    <li>Open an IDE of your choosing and run Git Bash.</li>
    <li>Change the current working directory to the location of which you wish to place the cloned repository.</li>
    <li>In the terminal, write <b>Git Clone</b> and then paste in the URL supplied via GitHub from step 2.</li>
    <li>Press enter and your new cloned repository will be created within the desired location.</li>
</ol>
<br>

[Back to Top](<#contents>)

## Credits

<p>I would like to say a small thanks to the Code institute for the first bit of help on how to setup the game and create objects models that have real value and functionality from their introduction video as it gave a good starting point on how to logically approach designing the game.</p>
<br>

[Back to Top](<#contents>)

## Acknowledgements

<p>This project is my 4t Portfolio Project for the Full Stack Software Developer (e-Commerce) Diploma course provided by the <a href="https://codeinstitute.net/" target="_blank">Code Institute</a>. </p>

[Back to Top](<#contents>)