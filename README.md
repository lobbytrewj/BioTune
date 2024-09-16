# EcoSub
 
# Inspiration
While many believe that happiness is derived from wealth, achievements, or relationships, one aspect that's often overlooked but can contribute the most to happiness is the weather. BioTune hopes to address this need by combining aspects that people are cognizant of -- stress levels, health, and sleep -- and underlying subconscious effects from the weather -- sunshine, temperature, wind speed, humidity, etc. -- to optimize user emotional well-being.

# What it does
BioTune asks the user 4 questions when developing a curated playlist to reflect their moods. The first question relates to their zip code. BioTune takes in the zip code and converts it into latitude and longitude coordinates to retrieve weather data. After this, the user enters 3 fields of the amount of sleep they got, their physical health, and current stress level. BioTune takes in these inputs and generates a custom MoodScore which then informs the model on what type of music playlist should be created (which includes 25 songs). For example, on a sunny day when the user feels great, BioTune will recommend a playlist of high-energy and upbeat music. However, on the same sunny day, if the user feels overly stressed, BioTune will recommend music to decrease stress and relax users throughout the day.

# How we built it
Weather data was retrieved from the Spire API which gave a comprehensive list of weather data given a certain zip code. Parameters relating to the effect on mood given each variable from weather data was retrieved from a 517-day-long study with 75 participants that trained a regression model to determine the relative effects of weather on mood (see Weather and Individual Happiness by Yoshiro Tsutsui). The same study included the 3 questions that BioTune asks its users. All of this data is then run through a model trained on the same parameters found in the research paper to accurately determine the mood of a user to generate a playlist for. The playlist was created with the Spotipy API which generated a link for users to click on after the custom playlist was created. 4 different emotional types of music were created with the playlists: hype, high energy, relaxation, and depression. Each playlist contains a list of over 10,000 songs, and from that list, 25 are randomly selected for the user to listen to.

# How to run BioTune
1. Run this message git clone https://github.com/lobbytrewj/EcoSub

2. Change your local directory to the Spotify folder within the repository, assuming that you have all dependencies and libraries installed, use npm start to open a local host of the website.

3. Once prompted to the website, you're met with the basic UI for the application. This includes a place to enter your city's zip code and three supporting questions to get a better understanding of the user's mood and current state.

4. Using GeoCoder through the ZipCodes API allowed us to retrieve the latitude and longitude of a certain zip code. Using this we were able to get access to Spire's API to retrieve weather data and based on this make an algorithm to determine user mood.

5. Then after gaining the overall mood of our user, we processed the mood and accordingly matched it to a type of music style. This then is sent to our song selection algorithm which created a unique set of songs and transfers them to the user's Spotify account.

# Challenges we ran into
Our team pivoted to this project extremely late: we had spent roughly 6 hours working on EcoScore, a product that rated products on their carbon footprint and sustainability, but we ran into problems finding a database of green-certified products and creating a recommendation system. Hence, we were on a tight schedule when creating BioTune. Creating the backend of BioTune was quite simple, but as it was the first time for all of us to create the frontend of a program, we ran into a lot of trouble fine-tuning it.

# Accomplishments that we're proud of
We're proud of all the progress we've made -- especially with this being our first hackathon. While there were many ups-and-downs, we were able to persevere through all of them to be confident to say that we did our best. We were particularly proud of creating a BioMood score which had been scientifically backed by a research study and catered to a need that has never been met.

# What we learned
We learned a lot about teamwork, specifically about the sunk-cost fallacy. We had already spent a lot of time on EcoScore and we felt like pivoting was the right idea, but it was too late and we may as well continue working on EcoScore. However, we ultimately just didn't care about failure and were able to create something exponentially better than we would have done if we hadn't embraced a fear of failure.

# What's next for BioTune
We hope to add additional playlists that we can recommend to users and hopefully transition users from one emotional state to another (say if they're very focused on work right now, but want to be happy, we can transition from a "study playlist" to an "energetic playlist"). This could be done by syncing with Notion or Google Calendar.

# Built With
flask
javascript
pandas
python
spire
spotify
