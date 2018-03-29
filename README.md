## LyrifyBot

We wrote a chatbot that is capable of recognizing music authors in natural language and returning sentences based on the lyrics from these artists. Essentially, this way the bot can reply using the style of the lyrics of certain artists, capsulating a lot of their speech pattern and vocabulary. 

The goal of the bot was to be able to return answers based on the vocabulary of the artists as well as make contextual sense. However, this may have been a little overzealous for this homework assignment and we downscaled it a little bit to what it is now; a bot that returns sentences based on the lyrics of artists. The bot is also capable of a little bit of chitchat, and all in all usable. 

The bot can be used by mentioning an artist in your message. If one is mentioned, the bot also looks whether a number is mentioned. The response then will be a sentence based on the lyrics of the artist with, if given, a maximum number of characters of the number specified in your message.

The approach taken for this project was the "bottoms-up" method, where we initially looked for a good dataset related to the direction we wanted to go. The specific problem that would be solved was based on the capacities that were allowed by the data. 
The [dataset](https://www.kaggle.com/dboshardy/ma-ma-markov-chain-ruler-of-the-funny-lyrics-game/data) we found was scraped from lyricsfreak.com by a kaggle user. The dataset contains the artist name, song name and lyrics from 57650 songs. This was deemed quite sufficient for our purpose. 

Our problem was, among others, well suited for Markov chains. Using the well known [Markovify](https://github.com/jsvine/markovify) library, we implemented the answering structure needed for these answers. We have implemented the capacity to respond in the style of a specific artist, but it is also possible to combine styles and name multiple artists. 

To give an indication of the possible interactions, see the images below. From top to bottom, they will visualize a possible conversation between a user and the bot. 
![greeting](/images/Capture.PNG)

After some explaining, lets get to the first query! As is clear, this one has a maximum length.
![start_interaction](/images/Capture1.PNG)

A different query, this time without a maximum length. 
![start_interaction](/images/Capture2.PNG)

Now lets try a combined sentence!
![start_interaction](/images/Capture3.PNG)

And lastly, the end of a conversation. 
![start_interaction](/images/Capture4.PNG)

