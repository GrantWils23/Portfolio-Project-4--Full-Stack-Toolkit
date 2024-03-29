![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<h1>Portfolio_Project_4 --- FullStack_Toolkit</h1>
<h1>BeBeauty</h1>
<p>The Idea for this website came from a friend who runs a business as a mobile beautician and requested a website that which she can take bookings from clients and has a way to manage her work diary. The beautician works remotely and therefore her business is a one-person operation and finds it hard to manage her work accordingly when she has so much going on, so the idea of the website is to cut down her interactions on the phone with clients as she has to commute via car and train and is sometimes impossible for her to make appointments in her diary when she is either commuting or in the middle of a session. This app is aimed at expanding her reach of clients and all the while giving them more piece of mind that they can make bookings and it will be recorded and saved...</p>

click here to go to the deployed website: <a href="https://bebeauty-app.herokuapp.com/" target="_blank"><b><i>"BeBeauty"</i></b></a>
<br><br>

![image](https://user-images.githubusercontent.com/72948843/181935137-008ff294-97f7-412c-96a5-cb3f4b4dd023.png)

![image](https://user-images.githubusercontent.com/72948843/181935492-f4929234-fadd-45a4-b88c-786a809978d0.png)

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Project Management](<#project-management>)
    * [Data Model](<#data-model>)
    * [Wireframes](<#wireframes>)
    * [Site Structure](<#site-structure>)
* [**Design Stylings**](<#design-stylings>)
    * [ColourScheme](<#colour-scheme>)
    * [Fonts](<#fonts>)
* [**Features**](<#features>)
    * [Existing Features](<#existing-features>)
    * [Input Validation and Checking](<#input-validation-and-checking>)
    * [Future Features](<#future-features>)
* [**Testing**](<#testing>)
* [**Technologies Used**](<#technologies-used>)
* [**Libraries**](<#libraries>)
* [**Deployment**](<#deployment>)
    * [Deployment of the project](<#deployment-of-the-project>)
    * [Cloning of the project](<#cloning-of-the-project>)
    * [Setting the email service](<#setting-the-email-service>)
* [**Credits**](<#credits>)
* [**Acknowledgements**](<#acknowledgements>)


# User Experience UX

## User Stories
Provide a user stories table here or list of the general user stories

[Back to Top](<#contents>)
<br>

## Wire Frames
The Wireframes for this project started off as a base idea with some users feedback from some of my friends who would use a service and they gave me feedback as time went on. These basic templates were the foundation of which the website style is built on but with the help of real user feedback I implemented it along the way.
 
[Back to Top](<#contents>)
<br>
 
## User Stories
Provide a user stories table here or list of the general user stories
<ul>
    <li>As a Site User I can Navigate to the Gallery to see previous work so that I can make an informed decision on whether I like the beautician's work or not.</li>
    <li>As a Site User I can browse the front page so that I can select different parts of the website I wish to view.</li>
    <li>As Site Admin I can Create a new booking on behalf of a guest or registered user manually so that a booking is stored on the database.</li>
    <li>As Site Admin I can Read the all the bookings stored on the database so that i can manage and plan my day and workload.</li>
    <li>As Site Admin I can Edit a booking on behalf of a guest or registered user manually so that the edited booking is stored on the database.</li>
    <li>As Site Admin I can Delete a new booking on behalf of a guest or a registered user manually so that the booking is removed from the database.</li>
    <li>As a Site User I can make an appointment with the beautician so that I will have a make-up session on the date I Choose.</li>
    <li>As a Site User I can edit my bookings so that they change to a better time/date that suits me.</li>
    <li>As a Site User I can cancel a booking so that I no longer have to go to the appointment that is not required.</li>
    <li>As a Site User I get confirmation upon successfully creating a new booking.</li>
    <li>As a Site User I get confirmation of my booking being edited was successful, and deletion of appointments.</li>
    <li>As a Site User I get confirmation that when I request my booking to be cancelled, it was successful.</li>
    <li>As a Site User I can Register an Account so that I can create and view all my bookings.</li>
    <li>As a Admin/User I can receive emails regarding bookings made, alter and cancel so that I can manage all my bookings.</li>
    <li>As a User I can contact the company with any queries i may have so that my concerns are answered.</li>
</ul>
<br>

[Back to Top](<#contents>)
<br>

## Project Management
To work along with the user stories that i created to help build the site, I used GitHubs's Project Board to manage my workflow. The Kanban style work board is very useful when trying to implement a working Agile environment. This tool helped me break down the importance of time management and helped me track my progress. It's a super powerful tool, with the abiltity to add small notes and labels to items within the project board.
<br>

![image](https://user-images.githubusercontent.com/72948843/183261980-26c2a44d-ed37-44e4-aed5-be0ec2ccffe0.png)
<br>

[Back to Top](<#contents>)
<br>

## Data Model
Here below you can find the Data schema used to create the data model. This was useful in helping me understand the flow and direction on how to create the app models, views and templates. A well working data schema is important to the database be established properly for the website to work correctly.
 
![image](https://user-images.githubusercontent.com/72948843/180508284-61cee041-2d54-41ae-b696-d54960757d1f.png)

<br>

[Back to Top](<#contents>)

## Wireframes
The Wireframes for this project started off as a base idea with some users feedback from some of my friends who would use a service and they gave me feedback as time went on. These basic templates were the foundation of which the website style is built on but with the help of real user feedback I implemented it along the way.

![image](https://user-images.githubusercontent.com/72948843/178985692-836737f5-6fee-42d9-b257-758808ee361f.png)

![image](https://user-images.githubusercontent.com/72948843/178987414-38e29485-f3cc-46f1-83a4-e5620159515e.png)

![image](https://user-images.githubusercontent.com/72948843/178990844-55a30a73-663b-49b9-acab-78be7bf0985b.png)

![image](https://user-images.githubusercontent.com/72948843/178993564-a87a437c-48f6-40b9-81e5-d1ef34e2159e.png)

![image](https://user-images.githubusercontent.com/72948843/178994130-61fc36a3-b3ec-4cd9-9969-915eb5eb0425.png)

<br>

[Back to Top](<#contents>)
<br>

## Site Structure
The site structure is extremely important to the clients who will wish to book an appointment with BeBeauty. It is imperative that the site is user friendly and easy to access, read, and find the pages you want to with the least hassle. The site structure will consist of a navigation menu bar that will be present at the top of all pages as well as a footer with the appropriate social links. The body of the pages will be broken down into the following...
<ul>
    <li>Home Page</li>
    <li>Services</li>
    <li>Prices</li>
    <li>Gallery</li>
    <li>Contact</li>
    <li>Sign Up</li>
    <li>Sign In</li>
    <li>Sign Out</li>
    <li>My Bookings</li>
    <li>Create Booking</li>
    <li>Booking Details</li>
    <li>Edit Booking</li>
    <li>Cancel Booking</li>
    <li>Delete Bookig</li>
    <li>Admin-Planner</li>
    <li>Admin Add Booking</li>
    <li>Admin Edit Booking</li>
    <li>Admin Cancel Booking</li>
    <li>Admin Delete Booking</li>
</ul>

The Desktop version of the site is very spacious but when the user drops down to a smaller aspect ratio the content will be forced to occupy a majority of the screen not to waste the restricted space that is left on the display. So any Wireframes above that take up larger areas with content and spacing will be forced to a column that occupies the screen so it displays all on one screen with no side to side juddering. This will greatly improve the UX as it will be easier to use on smaller devices, just as it would be on a desktop or larger screen device.

[Back to Top](<#contents>)
<br>

# Design Stylings

## Colour Scheme
the colour scheme chosen for this website is sutble and chicque, requested by the client that it will have light tones to exert a professional look that is not overpowering to the views and that it is to be inviting to anyone who visits the site.
the colour scheme chosen for this website is subtle and  chic, requested by the client that it will have light tones to exert a professional look that is not overpowering to the views and that it is to be inviting to anyone who visits the site.
-	The blue tone colour settled upon is aliceblue which is a nice colour that gives some personality to website other than a standard white background (#efffff).
-	The pink tone colour settled upon is mistyrose which is a beautiful light pink (#ffe4e1) that really compliments the background colour.
-	The pink tones also come with some shadowing to give a bit more flair and dynamics to the buttons and icons. the text shadow to the media buttons contains a darker pink colour (#ffc0cb).
- Functional buttons within the booking pages hold a simple colour scheme of:
    * Booking Buttons - Pink(#ffe4e1)
    * Completed Buttons - Green(#b3ecb3) 
    * Today Buttons - Yellow(#f9f092)
    * Cancel/Delete Buttons - Red(#f08080)
    * Edit Buttons - Blue(#add8e6)
    * Null Buttons - Grey(#acabab). This scheme is designed to draw attention appropriately with the necessary information regarding a booking.


![image](https://user-images.githubusercontent.com/72948843/178701361-701495cf-f505-44f6-83e2-bd32ac33fa17.png)
<br>

[Back to Top](<#contents>)
<br>

## Fonts

The fonts applied are important to the websites appeal. The main font for the website's title was requested by the client to be eye-catching and refined, but at the same time be strong and elegant. The font settled on were "Playfair Display" and it really ticks all the boxes.

![image](https://user-images.githubusercontent.com/72948843/178712500-832da105-1ba9-4ab4-b24a-2147f79d05f4.png)

The second font for the general font for the website which was settled on which complements the title font was "Zilla Slab". It works well as it doesn't draw away from the attention of the main font and is easy to read but still is attractive to the users.
 
![image](https://user-images.githubusercontent.com/72948843/178712706-aff22d38-4992-4116-b90d-98a6b7cb19d0.png)


[Back to Top](<#contents>)
<br>

# Features

## Existing Features
* [Navigation Menu](<#navigation-menu>)
* [Sign In](<#sign-in>)
* [Sign Up](<#sign-up>)
* [Sign Out](<#sign-out>)
* [services Page](<#services-page>)
* [Prices Page](<#prices-page>)
* [Gallery](<#gallery>)
* [Contact](<#contact>)
* [The Booking Form](<#the-booking-form>)
* [My Bookings](<#my-bookings>)
* [Booking Details](<#booking-details>)
* [Cancel and Delete Bookings](<#cancel-and-delete-bookings>)
* [Footer](<#footer>)
* [Pop-up Messages](<#pop-up-messages>)


### Navigation Menu
-	The nav menu is set at the top of all the pages. It is fully responsive and converts to a small dropdown menu on smaller screen ratios for a better UX. The nav contains links to all the pages of the site to enable quick searching through the website.
-	The logo is clickable with a link back to the home page for enhanced UX.
-	The bookings tab will only appear if the user is authenticated and logged in otherwise there is no bookings to view within the nav menu which makes it clearer for new customers that you need to sign up to book appointments


<i>Not Signed in</i>

![image](https://user-images.githubusercontent.com/72948843/178716276-c5cf98f9-fec0-4922-a76b-d8c35296ca15.png)

<i>User signed in</i>

![image](https://user-images.githubusercontent.com/72948843/180424025-1958c6c7-6a10-485f-a374-4631ed7ea667.png)


<i>Admin signed in</i>

![image](https://user-images.githubusercontent.com/72948843/180423660-8c95fe49-44fd-43f5-b423-c3f967ede232.png)


<i>Dropdown menu - smaller aspect ratio devices</i>

![image](https://user-images.githubusercontent.com/72948843/178731371-400bd99a-031d-4a93-a63f-12136f2359a5.png)

[Back to Existing Features](<#existing-features>)
<br>

### Sign In
- The Sign In page has a title in large letters.
- The sign in form has the required fields: Username and Password.
- There is a 'Remember Me' box located beneath the username and password fields, if a user wishes to hold their log in data.
- There is a clearly visible pink 'Sign In' button that submits the form for the user to sign in and redirects the user to the home page. 

![image](https://user-images.githubusercontent.com/72948843/183263239-7b719076-42c6-4a8f-9fb2-ad27238b9a85.png)

[Back to Existing Features](<#existing-features>)
<br>

### Sign Up
- The sign Up page has a title in large letters.
- In the form to sign up to the website, there are the fields: Username, Email, Password and Password(again) input boxes.
- There is a clearly visible pink 'Sign Up' button that submits the form for the user to sign Up and redirects the user to the home page. 

![image](https://user-images.githubusercontent.com/72948843/183263408-72fa0bec-bd85-41dd-8e5b-518699bceaa5.png)

[Back to Existing Features](<#existing-features>)
<br>

### Sign Out
- The Sign Out page has a title in large letters.
- a centered box contains a message asking the user if they are sure they want to log out?
- There is a clearly visible pink 'Sign Out' button that signs out the user and redirects the user to the home page. 

![image](https://user-images.githubusercontent.com/72948843/183263434-aafbc67c-d265-4162-8ff5-f1757f3fcbd8.png)

[Back to Existing Features](<#existing-features>)
<br>

### Services Page
The services page is designed to give the users a brief insight into the services of what the company offers its clients with a description of the beautician’s experience and really is where you get a feel for the company and the professional nature of it. The page is designed to be eye-catching and give the user a well-rounded experience as they view what company has to offer.
 
![image](https://user-images.githubusercontent.com/72948843/178738891-d482c632-cea1-486a-b77f-d7272512f8e7.png)

[Back to Existing Features](<#existing-features>)
<br>

### Prices Page
The prices page gives and accurate breakdown of the services that BeBeauty has to offer, as well as the description and prices and approximate time it takes each session. It is displayed in a list format to give users a clear presentation that is navigate to the service they are most interested in. It uses a modal to display the larger information of each booking. The modals give the user a real user friendly feel as it is free flowing the colour scheme matches the rest of the websites design giving a very pleasant UX.

![image](https://user-images.githubusercontent.com/72948843/178738621-9bece993-1377-42d2-b84e-f27a04017072.png)

![image](https://user-images.githubusercontent.com/72948843/178738736-a1e20a78-e6fc-4e46-bd85-80b3f0c89727.png)

[Back to Existing Features](<#existing-features>)
<br>

### Gallery
The gallery is a small sneak peak of just some of the work that BeBeauty has done for some its clients. The current idea is to have a small sample of photos with which the users can see now. If the users want to view more, they are encouraged to check them out on the social media links located below for more day-to-day photos if you follow them on the likes of Instagram or Facebook. This will likely change, and the owner may wish that they have a more robust website with a larger gallery later.

![image](https://user-images.githubusercontent.com/72948843/178739016-b4d4c666-d7c9-44ab-b602-a63050b91e5c.png)

[Back to Existing Features](<#existing-features>)
<br>

### Contact
The contact page is small and consists of the T&C's of the company's policy and how they operate. It is a clean format that clearly labels all important details regarding any bookings. 

![image](https://user-images.githubusercontent.com/72948843/178741286-6607523f-77b7-4833-8500-b4fe8820ed3e.png)

[Back to Existing Features](<#existing-features>)
<br>

### The Booking Form
The booking form is a simple and easy to use, once signed in it knows you are a valid user and so it generates the user and email name already for submission.

![image](https://user-images.githubusercontent.com/72948843/178740493-0c2a52f6-af0e-49ca-9dce-0b9a7b31c1dd.png)

[Back to Existing Features](<#existing-features>)
<br>

### My Bookings
The bookings page is a paginated page that displays a max of 6 appointments on any one page before having to cycle through to view more previous bookings. Its list view is very easy and clear to read and is set up according to the booking reference. The page displays the most significant information within the list view and has a link to view the booking attached to it. to the right side is the bookings edit and cancel buttons that give the user the ability to edit and cancel bookings or just to view old or completed bookings.

![image](https://user-images.githubusercontent.com/72948843/178739501-9bc45d9c-aaed-409b-ac30-13405a2dfdf2.png)

[Back to Existing Features](<#existing-features>)
<br>

### Booking Details
The booking page holds all relevant details required regarding the booking. Located at the bottom of each booking is again buttons to edit and cancel the booking giving the user more than one way just to alter a booking, which prevents having to scroll through multiple pages just to alter it and giving the user a warmer UX.

![image](https://user-images.githubusercontent.com/72948843/178742207-3c9c101e-bbb9-48ba-b6be-fa482c878ae5.png)

[Back to Existing Features](<#existing-features>)
<br>

### Cancel and Delete Bookings
This Page is a warning page for the user, it alerts them to the actions they plan on taking. By diverting to a new page, it gives the user a warning in clue of a visible prompt that with the request they plan to make will alter the booking in some way, this gives the user a greater UX when it comes to making sure they didn't cancel the booking by accident.

![image](https://user-images.githubusercontent.com/72948843/178741783-e1991d20-abf3-4c8c-9072-ca5c367ee852.png)

[Back to Existing Features](<#existing-features>)
<br>

### Footer
 The Footer is lightweight and is very minimalistic, this gives greater UX to the rest of the page as the footer displays social media links which is there for users who want to view more about the company outside of the dedicated website. The links are large and blend in with the rest of the page to show there is some significance in clicking the links. The social links would be directly linked to the businesses pages once the website is set for production.

![image](https://user-images.githubusercontent.com/72948843/178743421-51723903-10ab-450b-8558-21e869f35146.png)

[Back to Existing Features](<#existing-features>)
<br>

### Pop-up messages
The pop-up messages are integrated into the websites UX to provide the user with some useful feedback information. The messages will display on the success of a given task like signing in or upon a completion of a given task, or in the event of something failing, like the appointment booking is not possible, it will throw and error to the user in a message box. below are some examples...

![image](https://user-images.githubusercontent.com/72948843/178992505-afc8e9df-c791-4379-84a1-7a1edc6c4906.png)


![image](https://user-images.githubusercontent.com/72948843/178721734-56da133c-8ff3-4175-8040-db75e741501f.png)
<br>

[Back to Existing Features](<#existing-features>)
<br>

<hr>

[Back to Top](<#contents>)
<br>

## Input Validation and checking
Validation of the form is implemented by checking before the document is submitted is valid to submit. This is achieved by multiple methods:
<ul>
    <li>TTo validate the phone number being entered into the form, django-phonenumber-field was used. It checks the input to see if it is a valid phone number and returns an error message if it is not valid upon submission.</li>
    <li>To validate the date of which a booking can be made, within the form.py is code to check that the date of which the form is greater than the date the booking is being made. If the booking is in today or before, the form is not valid and is returned to be resubmitted.</li>
</ul>

![image](https://user-images.githubusercontent.com/72948843/178716912-c029e08e-f0ac-465c-b7a8-6b1ff8a945ff.png)

<ul>
    <li>Validation of the Bookings that cannot coexist was implemented by making a constraint within the database and when such appointment already exists with the parameters of ‘appointment_date’ and ‘appointment_slot’ are met, then the code throws an error and addresses the user to pick another day or time for the appointment. (This was a bug I solved)</li>
</ul>

![image](https://user-images.githubusercontent.com/72948843/178721734-56da133c-8ff3-4175-8040-db75e741501f.png)

[Back to Top](<#contents>)

<br>

## Future Features

Features left to implement:
This can be a list of unfinished or future new user stories on how to improve the website.
<li>As the website grows, a larger gallery which would host more pictures would be advantageous.</li>
<li>The ability to like photos in the gallery and upvote them would give the users a more integral feel and a feeling that their opinion matters</li>
<br>

[Back to Top](<#contents>)
<br>

# Testing

<p>To find out more about the tests related to the project. please follow this <a href="https://github.com/GrantWils23/Portfolio-Project-4--Full-Stack-Toolkit/blob/main/tests/TESTS.md">link</a> to the testing page.</p>

[Back to Top](<#contents>)
<br>

## Technologies Used

<li><a href="https://github.com/" target="_blank">GitHub</a> -The site was used to edit and host the website.</li>
<li><a href="https://gitpod.io/projects" target="_blank">GitPod</a> - Used in the deployment and creating the website.</li>
<li><a href="https://git-scm.com/" target="_blank">GitBash</a> - Used for committing and pushing files to github in the terminal through version control. GitBash - Terminal used to push changes to the GitHub repository.</li>
<li><a href="https://www.python.org/" target="_blank">Python</a> - This was used in the production to get the game running as it is required for the app to run.</li>
<li><a href="https://www.djangoproject.com/" target="_blank">Django</a> - The Django web Framework was used to create the app and maintain it.</li>
<li><a href="https://psycopg.com" target="_blank">Psycopg</a> - The database with which the app runs are PostrgeSQL.</li>
<li><a href="http://pep8online.com/" target="_blank">pep8online</a> - This site was used to validate the python code to check for any errors within my writing.</li>
<li><a href="https://www.heroku.com/" target="_blank">Heroku</a> - This was used to deploy the website online for users to see and active site.</li>
<li><a href="https://pypi.org/project/django-phonenumber-field/" target="_blank">Django-phonenumber-field</a> -Is a django module used for validating a phonenumber that is to be stored into the database.</li>
<li><a href="https://django-allauth.readthedocs.io/en/latest/" target="_blank">Django-allauth</a> - Is an authentication app that is used to check validity of the users accessing the website.</li>
<li><a href="https://django-crispy-forms.readthedocs.io/en/latest/" target="_blank">Django-crispy-forms</a> - Is a form generator helper that enables quick and tidy forms to be made with minimal input on the front end.</li>
<li><a href="https://fontawesome.com/" target="_blank">fontawesome</a> - Is used to get the icons at the bottom of the page for the social media resources.</li>
<li><a href="https://favicon.io/" target="_blank">Favicon</a> - was used to design the Favicon for display in the browser tab</li>
<li><a href="https://getbootstrap.com/" target="_blank"> Bootstrap </a> - Bootstrap was used in this project to help create the website with fast and easy web designs, from drop in code for modals, nav bars and how the viewports react.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"> CSS </a> - Aside from some basic stylings inherited from bootstrap, CSS was used to customise the website to a tailored fit. The design schema was heavily influenced by the theme and colours requested and the wireframes used at the beginning stage of development. CSS gave the ability to create a beautiful website exactly as the client requested.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank"> HTML </a> - HTML used as the language to render the text in the front-end.</li>
<li><a href="https://www.pexels.com/" target="_blank"> Pexels </a> - An online stock of photos that are royalty free to use.</li>
<li><a href="https://www.dreamstime.com/" target="_blank"> Dreamstime </a> - An online stock of photos that are royalty free to use.</li>
<li><a href="https://docs.djangoproject.com/en/4.0/topics/email/" target="_blank"> Django Email </a> -  Django Email is a very useful and powerful tool that allowed the clients to receive emails regarding their booking. It is a really useful tool that provides real time functionality with great results.</li>
<li><a href="https://compressor.io/" target="_blank"> Compressor </a> -An online compressing tool, great for compressing stock images down to a user friendly size, and it is completely free to use.</li>
<li><a href="http://pep8online.com/" target="_blank"> PEP8 Validator </a> - An online website used to validate my Python code</li>
<li><a href="https://jshint.com/" target="_blank"> JSHint Valdiator </a> - An online website used to validate my JavaScript code</li>
<li><a href="https://validator.w3.org/nu/" target="_blank"> HTML Validator </a> - An online website used to validate my HTML code.</li>
<li><a href="https://jigsaw.w3.org/css-validator/" target="_blank"> CSS Validator </a> - An online website used to validate my CSS code.</li>
<li><a href="https://developer.chrome.com/docs/devtools/" target="_blank"> Google Chrome DevTools </a> - An online resource that lays within Google Chrome used to debug the website during development.</li>
<li><a href="https://drawsql.app/" target="_blank"> DrawSQL </a> - An online app used to create the database schema.</li>
<li><a href="https://color.a11y.com/" target="_blank">A11y</a> - An online accessibility validator that checks the colour of the background against the text.</li>

<br>

[Back to Top](<#contents>)
<br>

## Libraries

<p>The libraries used in this project are located in the requirements.txt file and were set up in the virtual environment to get the project working. Below is the list of libraries used to run the website:</p>

<ul>
    <li><a href="https://pypi.org/project/asgiref/" target="_blank">asgiref</a> -  Reference ASGI adapters and channel layers.</li>
    <li><a href="https://pypi.org/project/backports.zoneinfo/" target="_blank">backport.zoneinfo</a> - The module used to implement the IANA time zone database in the python standard libary.</li>
    <li><a href="https://pypi.org/project/click8/" target="_blank">click</a> - A python package to help write command line interfaces with as little code as necessary.</li>
    <li><a href="https://pypi.org/project/coverage/" target="_blank">coverage</a> -  A python package that helps determine test coverage.</li>
    <li><a href="https://pypi.org/project/dj-database-url/" target="_blank">dj-database-url</a> - This utility package allows the user to utilize the "DATABASE_URL" environmental variable to configure the Django App.</li>
    <li><a href="https://pypi.org/project/dj3-cloudinary-storage/" target="_blank">dj3-cloudinary-storage</a> -  This package allows django to facilitate integration with Cloudinary by implementing Django Storage API.</li>
    <li><a href="https://pypi.org/project/Django/" target="_blank">Django</a> - A high-level Python web framework that encourages rapid development and clean, pragmatic design.</li>
    <li><a href="https://pypi.org/project/django-allauth/" target="_blank">django-allauth</a> - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.</li>
    <li><a href="https://pypi.org/project/django-cloudinary-storage/" target="_blank">django-cloudinary-storage</a> -Django package that provides Cloudinary storages for both media and static files as well as management commands for removing unnecessary files.</li>
    <li><a href="https://pypi.org/project/django-crispy-forms/" target="_blank">django-crispy-forms</a> -Build programmatic reusable layouts out of components, having full control of the rendered HTML without writing HTML in templates.</li>
    <li><a href="https://pypi.org/project/django-filter/" target="_blank">django-filter</a> - Django-filter is a reusable Django application for allowing users to filter querysets dynamically.</li>
    <li><a href="https://pypi.org/project/django-phonenumber-field/" target="_blank">django-phonenumber-field</a> - A Django library which interfaces with python-phonenumbers to validate, pretty print and convert phone numbers.</li>
    <li><a href="https://pypi.org/project/docstring-parser/" target="_blank">docstring-parser</a> - Parse Python docstrings in rest, Google and Numpydoc format.</li>
    <li><a href="https://pypi.org/project/gunicorn/" target="_blank">gunicorn</a> - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX.</li>
    <li><a href="https://pypi.org/project/iniconfig/" target="_blank">iniconfig</a> - Iniconfig is a small and simple INI-file parser module having a unique set of features.</li>
    <li><a href="https://pypi.org/project/oauthlib/" target="_blank">oauthlib</a> - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic.</li>
    <li><a href="https://pypi.org/project/phonenumbers/" target="_blank">phonenumbers</a> - Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.</li>
    <li><a href="https://pypi.org/project/pluggy/" target="_blank">pluggy</a> - Plugin and hook calling mechanisms for python.</li>
    <li><a href="https://pypi.org/project/psycopg/" target="_blank">psycopg2</a> - PostgreSQL database adapter for Python.</li>
    <li><a href="https://pypi.org/project/py3/" target="_blank">py</a> - This is a dummy package.</li>
    <li><a href="https://pypi.org/project/PyJWT/" target="_blank">pyJWT</a> - JSON Web Token implementation in Python.</li>
    <li><a href="https://pypi.org/project/pylint-django/" target="_blank">pylint-django</a> - A Pylint plugin to help Pylint understand the Django web framework.</li>
    <li><a href="https://pypi.org/project/pylint-plugin-utils/" target="_blank">pylint_plugin-utils</a> - Utilities and helpers for writing Pylint plugins.</li>
    <li><a href="https://pypi.org/project/pytest/" target="_blank">pytest</a> - A simple, powerful testing package in python.</li>
    <li><a href="https://pypi.org/project/python-openid3/" target="_blank">python3-openid</a> - OpenID support for servers and consumers. Python 3 support fork.</li>
    <li><a href="https://pypi.org/project/pytz/" target="_blank">pytz</a> - World timezone definitions, modern and historical.</li>
    <li><a href="https://pypi.org/project/requests-oauthlib/" target="_blank">request-oauthlib</a> - OAuthlib authentication support for Requests.</li>
    <li><a href="https://pypi.org/project/sqlparse/" target="_blank">sqlparse</a> - A non-validating SQL parser.</li>
</ul>

<br>

[Back to Top](<#contents>)
<br>

# Deployment

## Deployment of the project

### Deployment to Heroku
<p>To deploy the site is a labour intensive process. follow the steps below for a stress free deployment:</p>

First and foremost, if you are not a user of Heroku, sign up to its services, once you are logged in, in the top right corner there is a button "New". Click on the button and then click on "create new app".

![image](https://user-images.githubusercontent.com/72948843/182254035-7a6d430b-10bb-4adb-acda-fe21e2a2cd8e.png)
 
Once the page loads, it asks you to put in an app name and your preferred region. I choose Europe as it is my current region.
 
![image](https://user-images.githubusercontent.com/72948843/182254260-b3818089-7b60-4702-9ff3-4ef25acfc727.png)

Once inside the generated app, click on "resources" and then search for 'Heroku Postgres'. Attach this to your project. You must submit the order form. once added it will appear attached as a permanent to 'Add-ons' column.


![image](https://user-images.githubusercontent.com/72948843/182254632-aa6ba5ac-802f-469b-b5b2-c9ff98798b52.png)

If you click on the Heroku Postgres link, it will redirect you to a new page with the information about your Heroku Postgres Database with all the credentials. Click on 'Settings' and then click 'View Credentials' and it will show you your database credentials. below is the image of my credentials.
 
![image](https://user-images.githubusercontent.com/72948843/182255490-5e325002-cf77-45b0-893d-e491ba0f09ab.png)

From the credentials you will want to look at the URI. We will copy this over and add this into our Config Vars:

Return back to the Heroku app page and click on 'settings'. Once inside settings, scroll down to the project settings and click 'Reveal Config Vars'. Add the following config vars to the project:
<br>

NOTE: Before deployment we will need to remove the ```DISABLE_COLLECTSTATIC = 1``` var. This is currently in place for the development stage. When you delpoy the app make sure you remove this.
<br>

![image](https://user-images.githubusercontent.com/72948843/182256504-079ad16f-cffc-4494-9bae-7d95a85d8f95.png)
 
Now go back to VSCode and create a new file called <b><i>env.py</i></b> if it has not already been created. <b>Make sure you add it to your '.gitignore' file</b>. copy the code below. This is nothing new, its just the same config vars from the heroku app and we need them inside our env.py file. make sure to add <b>your</b> config var values inside.

![image](https://user-images.githubusercontent.com/72948843/182257529-09ce9e5d-9ba7-410c-a745-25c86e6506aa.png)

Inside settings.py, search for the line that says "from pathlib import Path" and then insert the code below:

![image](https://user-images.githubusercontent.com/72948843/182257894-26c2518f-2fbf-401a-b26c-6a845945ecf0.png)

Replace the default random security key that Django provides you with your SECRET_KEY variable that you created in your env.py file.

![image](https://user-images.githubusercontent.com/72948843/182258087-fd940b53-a297-49fa-8445-dcd45aba6892.png)

Set <b>DEBUG = 'DEVELOPMENT' in os.environ</b> This allows you to have Debug set to True when developing locally. However DEBUG will be set to False when deployed to Heroku.

![image](https://user-images.githubusercontent.com/72948843/182258392-dcce5dac-62ea-48fc-a9d0-35e9b5a7d956.png)

Whilst working in development, we want to keep the PostgreSQL for deployment. So, running the code below allows us to have two databases. SQLite for local development and the PostgreSQL database for the deployed application.

![image](https://user-images.githubusercontent.com/72948843/182259041-4743cadc-e401-44ab-a440-4d64c40305b3.png)

Next we need to add cloudinary application to the INSTALL_APPS in settings.py: <b>The order of the  apps in this list is important, copy as below.</b>

![image](https://user-images.githubusercontent.com/72948843/182259381-0c8589cd-e570-4679-982d-b6c7dfef087f.png) 
 
Then we need to go to STATIC_URL = '/static/' in the settings file and copy the code below... this tells django to use Cloudinary to store media and static files
 

![image](https://user-images.githubusercontent.com/72948843/182259693-72cd2070-895d-4473-8576-26819495480c.png)

After that we can add the code for the Templates into the settings.py copy the code below:

![image](https://user-images.githubusercontent.com/72948843/182259902-c01aef57-3de8-4d13-a3e2-0fed1f491249.png)

Next add your allowed hosts to ALLOWED_HOSTS. You will need to add ```'127.0.0.1'``` to your local host list to allow you to open it locally, as well as ```'localhost'``` and ```'bebeauty-deployment-process.herokuapp.com'```

![image](https://user-images.githubusercontent.com/72948843/182463546-97ee9b7e-072b-41ac-bbc4-81557fe9dd5f.png)

Now inside the top level directory we need to two new folders and one new file:

#### STATIC
<li>Add a static file that will hold your images, and css folders and anything else. i.e. js files and/or favicons.</li>

<br>

#### TEMPLATES
<li>Next add the templates folder where the project will keep all the HTML files that will will be used to build the webiste.</li>

<br>

#### PROCFILE
Once those files are completed, we need to add a Procfile for the website to work. So again, from the top level directory, we need to add a Procfile and within the file write the command... ``` web: gunicorn 'APP_NAME'.wsgi ``` within the file. This allows the file to run your in Heroku.

(My Example from BeBeauty)
![image](https://user-images.githubusercontent.com/72948843/182356833-bbfa158f-942b-4538-b78c-0b72edfcc6a1.png)


If you are unsure what your app name is, you can find it and the resources page of your heroku app page, just look at the exmaple below if you are not sure...

![image](https://user-images.githubusercontent.com/72948843/182356444-15549040-be85-465d-bb7d-da5616823a00.png)

Once completed, make sure you save all the files and then type the following lines:

* ```git add .```
* ```git commit -m "deployment commit"```
* ```git push```
<br>
Then the final step is to deploy your application, if you wish to deploy using the Heroku CLI follow the lines of code below:

* ```heroku login```
* ```heroku git:remote -a APP_NAME```
* ```git push heroku main```
<br>
Alternatively, if you wish to do it from within the Heroku website and through github, follow the steps below:

1) Within your Heroku app, click on the deploy tag.
2) On the deployment section in the middle, select GitHub.
3) Once you log in to github through Heroku, you should get a search menu appear.
4) Search for the repository within your Github account for the app you will create and then hit the "Connect" button.
<br>
![image](https://user-images.githubusercontent.com/72948843/182438506-65c4d13a-29dd-492c-a710-452fa1fe8110.png)

5) Once connected, you will be presented with two methods to deploy the website, Automatic and Manual Deployment. Choose whichever one is more conventient for you.
<br>
![image](https://user-images.githubusercontent.com/72948843/182439770-36dba819-d629-477a-a8f0-dd1a61eeb2c0.png)

[Back to Top](<#contents>)

(Side Note: When the app is deployed, Debug has to be set to False! this is for security reasons as it can expose sensative data.)
<br>

### Cloning and setting up of this project
<hr>



<p>To create a local clone of the project, follow the steps below:</p>

* In the GitHub repository, under the repository name there is a code tab., click on the 'code' tab. and select either HTTPS or CSS link to copy the code. I will use HTTPS:
![image](https://user-images.githubusercontent.com/72948843/182441657-b4116d59-ee58-4a4d-9826-2119bd34d7a8.png)
* In the clone tab, click the HTTPS tab. Within this section, click on the clipboard icon and copy the URL supplied for the repository.

* Once the link has been copied, open an IDE (Command Prompt) of your choosing, navigate to where you wish to store the project and run the following terminal commands:

1. ```"git clone HTTPS or SSH link``` - This will clone the project to your computer
2. ```cd name of project``` - This will cd (change directoy) into your project
3. ```code .``` - This will launch your project in VSCode
<br>
![image](https://user-images.githubusercontent.com/72948843/182444495-9a5f9b21-e7e2-4a99-b055-937a7232470e.png)

Now you need to setup and initialize a virtual environment for the project. follow the steps below to setup a virtual environment if you haven't done so before.

```$ pip install virtualenv```
<br>
(Step.1) Test your installation was successful:

```$ python3 -m virtualenv -- version```
<br>
(Step.2) Then create the virtual environment using virtualenv

```$ python3 -m virtualenv myenv```
<br>

![image](https://user-images.githubusercontent.com/72948843/182444824-9bafb75a-cae4-4cef-b00b-d22d9a619336.png)
<br>
(Step.3) After creating the virtual environment, you need to activate it. <b><i>We need to activate the virtual environment every time you will work on the project!</i></b>. This can be achieved by using the following command:
<br>

* ``` $ source virtualenv_name/bin/activate ``` - [For Mac] 
* ``` $ source virtualenv_name/Scripts/activate ``` - [For Windows]  (as in my example below):

!![image](https://user-images.githubusercontent.com/72948843/182445439-bca1e977-081b-46ea-85c3-312b04543870.png))

<b>Don't forget to addd the env to your .gitignore file</b> if added correctly the file and its content's font shall be shaded a darker grey.

![image](https://user-images.githubusercontent.com/72948843/182445548-45a57c2b-d86a-491e-bd25-3b03f93d0892.png)

Once you are in the virtual environment, the terminal will have it appear in brackets next to the command line as in the image below:

![image](https://user-images.githubusercontent.com/72948843/182445662-f576728c-a54e-48de-92a3-98439108785b.png)

NOTE: To deactivate the virtual environment just type ```deactivate``` into the terminal (like in the image below).

![image](https://user-images.githubusercontent.com/72948843/182445800-b322a679-751f-4ad3-af36-416b91451d23.png)
<br>
<hr>
Now within the virtual environment, we now need to install the project requirements to run the project. in the virtual environment terminal, type in the following command:

```pip3 install -r requirements.txt```

What this will do is download all the app's dependencies stated in the requirements.txt file which will get the project to work.

![image](https://user-images.githubusercontent.com/72948843/182447722-1b86059c-319a-4ef1-9db5-7900de0b4374.png)

With that now complete, We now need to create our env.py file, which tells the app what variables to use. These variables are usually hidden for security reasons as they contain sensative data that we don't want leaked and can be dangerous if shared publicly they can be vulnerable to attacks. So what we must do is first create the env.py file and immediately add it to our .gitignore file.

Any variables you declared in your settings.py file must be added to this file. (Apart from ["DEVELOPMENT"]) to your config vars when you deploy in Heroku.

![image](https://user-images.githubusercontent.com/72948843/182455915-2e6da191-999a-4ffd-8fe4-0494d232e6a0.png)

Now when we run the command ```python3 manage.py runserver``` if the terminal will respond with unapplied migrations which is to be expected as we haven't made any migrations into the database. If this is the case, run the migrations command in the terminal... ```python3 manage.py migrate```.

Once it has finished applying the migrations, you will need to run the command ```python3 manage.py runserver```

![image](https://user-images.githubusercontent.com/72948843/182458479-9d27b5ac-542c-40e4-a11e-2ed937375e73.png)

This will now launch the project locally, successfully and ready for development.

The test files that exist in the project can be run with the simple command ```python3 manage.py test```. 

If you wish to test a particular app you can run the command ```python3 manage.py test "APP_NAME"```

(for example, the specific APP_NAME's from BeBeauty are 'booking' or 'treatment')

This command will only work if you use your local database within the deployment. if for any reason you run this command using the Heroku database, the test will fail. please refer to the <a href="https://github.com/GrantWils23/Portfolio-Project-4--Full-Stack-Toolkit/blob/main/tests/TESTS.md">testing</a> file to see how the tests perform.

This project has installed inside it a python package called [*Coverage*]. This app is useful as it gives you comprehensive reports on how much of your project has been tested. To get a coverage report, run the following command in the terminal: ```coverage report``` and this will output a tabled list of the results from the report. The report gives you an idea of what areas perhaps require more testing and gives you a score on how your tests perform.

<br>

### Setting the email service

There is one part of the project that hasn't been explained in the above. I have set up the app to send emails and to do this I created at the bottom of settings.py. What we have here are two two config vars that we need to add to your env.py file. The ```['EMAIL_HOST_USER']``` and ```['EMAIL_HOST_PASSWORD']```. 

![image](https://user-images.githubusercontent.com/72948843/182680072-b77a00e2-2c0b-4c93-a2bf-1a7f24f56a12.png)

 I found a really useful tutorial by "Toumi Abderrahmane" on how to set up googlemail sync up to send emails with django in deployment. please click on this link below.

<a href="https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab" target="_blank">how to send email with django and gmail</a>
<br>

Within the env.py file, at the bottom two lines, you have to insert you email address and password, just look below:

![image](https://user-images.githubusercontent.com/72948843/182467606-e6d25616-caf0-4b54-8bcf-abf559771028.png)

Now with this done, you can now send emails in development and deployment.
 (Note there is a code at the bottom of the Development Django Email Settings, run this in the command line to check your emails send.)

[Back to Top](<#contents>)

## Credits

<p>Building the website was a very hard process but very rewarding. I would like to mention below some credits to my project:</p>
<ul>
    <li>I used Bootstrap a lot when building this website. I mentioned a link to the website in the above technologies used section.</li>
    <li>Django documentation was used a lot during the build of the website to make sense of how to build the MVT. The documention is very thorough and explains a lot of things clearly. When I had a problem, I could read their docs with a large degree of success</li>
    <li>I also used <a href="https://stackoverflow.com/" target="_blank">Stacker Overflow</a> to help me when I had problems as there was a lot of times people had the same problems as I and I could lean on some of these questions for help.</li>
</ul>
<br>

[Back to Top](<#contents>)

## Acknowledgements

<p>This project is my 4th Portfolio Project, as part of <a href="https://codeinstitute.net/" target="_blank">Code Institute's</a> Full Stack Software Developer (e-Commerce) Diploma.</p> A Big thank you to Precious Ijege (my mentor) for his help and expertise pushing me to right better code. Another thank you to the Slack community as well and Daniel_C_5p_lead (Daniel Callaghan) for his help as he always found the time to reply anytime I had a problem, he always tried to help. Also thank you to the tutors at Code Institute Alex and Oisin who helped me when I lost my way. There experience and help really got my through the tough patches.
<br>
<br>
Grant Wilsmore, 2022
<br>
<br>

[Back to Top](<#contents>)