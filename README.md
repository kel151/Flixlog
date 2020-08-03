<h1>OurAnimeVault</h1>
<p>Have you ever tried to remember the name of that really good anime you watched ages ago? Have you ever tried to remember what your intial thoughts on it were or all of the reasons why you liked (or disliked) it? If you're anything like me, then the answer to both of these questions is yes. That's where OurAnimeVault comes in.</p>
<p>Think of it as a very niche and collective film critiquing app for personal use. You watch an anime that you like or dislike that you might want to remember for the purposes of recommending it or rewatching it later, simply make an entry, and there you go. Your intial thoughts and feelings are recorded for reference later.<p>

<h2>Content:</h2>
<ul>
  <li>UX 👍
    <ul>
      <li>Project Goals</li>
      <li>Target Audeience Goals</li>
      <li>Site Owner Goals</li>
      <li>User Stories</li>
      <li>User Requirements and Expectations</li>
    </ul>
  </li>
  <li>Design Choices 🎨
    <ul>
      <li>Fonts</li>
      <li>Colours</li>
      <li>Styling</li>
      <li>Images</li>
      <li>Backgrounds</li>
    </ul>
  </li>
  <li>Planning ✏️</li>
  <li>Wireframes 🔧
    <ul>
      <li>Website Layout</li>
      <li>Account Creation Flowchart</li>
      <li>Database Design</li>
    </ul>
  </li>
  <li>Features 🎡
    <ul>
      <li>Features that have been developed</li>
      <li>Features that will be implemented in the future</li>
    </ul>
  </li>
  <li>Technologies Used 👨‍💻</li>
  <li>Planning + Testing ✏️ 🔌</li>
  <li>Bugs 🐞</li>
  <li>Deployment 🚀
    <ul>
      <li>Deploying to Heroku</li>
      <li>Locally run this project</li>
    </ul>
  </li>
  <li>Credits 💳</li>
  <li>Disclaimer 📝</li>
</ul>

<h2>User Experience 👍</h2>
<h3>Project Goals:</h3>
<p>The goal of this project is to provide users with a online repository in which they can record their opinions of the anime titles they've seen, rating them and providing their intial thoughts. This project will serve as a collective film critiquing service for personal use that caters to a very specific genre and demographic.</p>

<h3>Target Audience Goals:</h3>
<ul>
<li>To be able to record anime titles in one place.</li>
<li>To be able to record my intial thoughts, feelings, opinion on each title.</li>
<li>To be able to rate each title.</li>
</ul>

<h3>Site Owner Goals:</h3>
<ul>
<li>Generate further interest in anime/Japanese animation</li>
<li>Encourage curiosity about the viewing habits and perspectives of others.</li>
<li>Encourage critical thinking about the anime titles that we watch, and provoke deeper exoloration of their themes, ideas, etc.</li>
<li>Collect user information for the purposes of site analytics and gaining insights into how the general public receives certain titles.</li>
</ul>

<h3>User Stories:</h3>
<ul>
<li>As a user, I expect log in to be quick and easy.</li>
<li>As a user, I expect to navigation of the site to be intuitive and require as few clicks as possible.</li>
<li>As a user, I expect to maaking an entry to be quick and simple.</li>
<li>As a user, I expect my entries to be stored in such a way that makes them easy to view and access.</li>
</ul>

<h3>User Requirements and Expectations:</h3>
<h4>Requirements:</h4>
<ul>
<li>Interact with a visually appealing website.</li>
<li>Navigate the website with ease & with fast load times.</li>
<li>Make entries in an quick and uncomplicated way.</li>
<li>Find previous entries easily and see them clearly displayed.</li>
</ul>

<h4>Expectations:</h4>
<ul>
<li>The users can interact with the elements visible on the page.</li>
<li>The website loads with sufficient speed.</li>
<li>The content on the website renders correctly on desktop, mobile and tablet.</li>
<li>The user feels satisfied with the experience.</li>
</ul>

<h2>Design Choices</h2>
<p>It was important for me to create a project aesthetic that suited the theme of Japanese anime. In light of this, I opted for a unifying background image that contained some popular Japanese titles. This was then framed by a dark footer and navbar, which the social media handles of the footer being pink, because when most people think of anime, they often think of either soft pastels like pink. I also opted for the accordians to be of a similar black to the footer and navbar, to provide more of a sense of cohesion. All in all, I feel all of these elements blended together in a way that appeared cohesive and seamless as well facilitated a positive user experience.</p>

<h3>Fonts:</h3>

<h3>Colours:</h3>
<p>I carefully considered which colours I wanted to use because I knew I wanted to mix some genre-defining pastels with some darker elements, but I also needed to ensure that the colour combinations complimeted the background image as well as each other while not overpowering one another or competing for the user's attention in jarring or dissonant way. So, after careful deliberation, I decided to use <a href="https://coolors.co/">coolers</a>, which is a colour scheme generator. It helped to experiment with dfferent palette and eventually decide on a group of colours that I think were attractive and appropriate for the project. The chosen colours are:

<ul>
<li>![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `#f03c15`</li>
<li>485665</li>
<li>8e7c93</li>
<li>d0a5c0</li>
<li>f6c0d0</li>
</ul>

<h3>Images:</h3>
<p>The background landing page/log in page is a flex panel gallery, with each panel oscillating between a solid colour and anime image.</p>

<h3>Background Images:</h3>

<h2>Wireframes/Flowcharts</h2>
<p>I used <a href="https://balsamiq.com/">balsamiq</a> to develop the wireframes for this project. I chose balsamiq because their process for creating wireframes is quick, simple, and intuitive. Having the wireframes developed before commencing the project made development much easier and more straightforward. It provided a basic blueprint that I could follow which made the endeavor faster and more manageable.

The wireframes can be found <a href="https://github.com/kel151/Flixlog/tree/master/wireframes">here</a>.</p>

<h3>Account Creation Flowchart:</h3>
<p>Despite the account creation and log in process seeming rather simple, I still opted to create a very basic flowchart for it for the purposes of visualizing the user's journey. It can be found <a href="https://github.com/kel151/Flixlog/tree/master/fl%20wireframes/flowcharts">here.</a></p>

<h3>Database Design:</h3>
<p>I used NoSQL features from MongoDB in order to be able to map out the collection below.</p>

<h3>Data Storage Types:</h3>
<p>The types of data that are stored in the MongoDB database:</p>
<ul>
<li>String</li>
<li>Number</li>
</ul>

Entry Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Title|title|String
Category|category|String
Rating|rating|Number
Comments|comments|String

View the schema templates for the database collections <a href="https://github.com/kel151/OurAnimeVault/blob/master/data/schemas.json">here.</a>

<h2>Features</h2>

<h3>Features that have been developed:</h3>

<h3>Features that will be developed in the future:</h3>

<h2>Technologies Used 👨‍💻</h2>

<h4>Languages:</h4>

<h4>Tools & Libraries:</h4>

<h2>Planning + Testing</h2>

<h4>Planning:</h4>

<h4>Testing:</h4>

<h2>Bugs</h2>

<h4>Bugs During Development</h4>

<h2>Deployment</h2>
<p>OurAnimeVault was developed on Gitpod, using git and Github to host.</p>

<h3>Cloning OurAnimeVault from Github:</h3>

<p>You will need to install the following:</p>

<ul>
<li><a href="https://pip.pypa.io/en/stable/installing/">PIP</a></li>
<li><a href="https://www.python.org/">Python</a></li>
<li><a href="https://git-scm.com/">Git</a></li>
</ul>

<p>You will also need a <a href="https://www.mongodb.com/">MongoDB</a> account for the databsae.<p>

<em>WARNING: You may need to follow a different guide based on the OS you are using, read more <a href="https://python.readthedocs.io/en/latest/library/venv.html">here.</a></em>

* 1: <strong>Clone</strong> the OurAnimeVault repository by either downloading from <a href="https://github.com/kel151/OurAnimeVault"> here</a>, or if you have Git installed typing the following command into your terminal.
```bash
git clone https://github.com/kel151/OurAnimeVault
```
* 2: <strong>Navigate</strong> to this folder in your terminal.
* 3: <strong>Enter</strong> the following command into your terminal.
```bash
python3 -m .venv venv
```
* 4: <strong>Initilaize</strong> the environment by using the following command.
```bash
.venv\bin\activate 
```
* 5: <strong>Install</strong> the relevant requirements & dependancies from the requirements.txt file.
```bash
pip3 -r requirements.txt
```
* 6: In your IDE now <strong>create</strong> a file where you can store your SECRET_KEY and your MONGO_URI, follow the schema structure located in data/schemas to properly setup the Mongo Collections.
<em>NOTE: I developed this website on Visual Studio Code and used the following settings.json file, delete and replace with your values.</em>
```json
{
    "python.pythonPath": "env/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintArgs": ["--load-plugins=pylint_flask"],
    "files.autoSave": "onFocusChange",
    "files.useExperimentalFileWatcher": true,
    "terminal.integrated.env.osx": {
      "SECRET_KEY": "<your_secret_key>",
      "DEV": "1",
      "FLASK_DEBUG": "1",
      "MONGO_URI": "<your_mongo_uri>"
    }      
}
```
* 7: Run the application using 
```bash
flask run 
```
or 
```bash
Python3 app.py
```
<h3>Deploying OurAnimeVault to Heroku:</h3>

* 1: <strong>Create</strong> a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```
* 2: <strong>Create</strong> a Procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
* 3: <strong>Push</strong> these newly created files to your repository.
* 4: <strong>Create</strong> a new app for this project on the Heroku Dashboard.
* 5: <strong>Select</strong> your <strong>deployment</strong> method by clicking on the <strong>deployment</strong> method button and select GitHub.
* 6: On the dashboard, <strong>set</strong> the following config variables:

**Key**|**Value**
:-----:|:-----:
IP|0.0.0.0
PORT|8080
MONGO\_URI|mongodb+srv://<username>:<password>@<cluster\_name>-qtxun.mongodb.net/<database\_name>?retryWrites=true&w=majority
SECRET\_KEY|"your\_secret\_key"
* 7: Click the deploy button on the Heroku dashboard.
* 8: The site has been deployed the Heroku.


<h2>Credits</h2>

<h2>Disclaimer</h2>
<p>The contents of this website are for educational purposes only.</p>
