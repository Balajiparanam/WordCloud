# WordCloud(optional project)
## Project Overview
### Wordcloud is a visual representation of text data.
![final_output](https://user-images.githubusercontent.com/45941424/91551732-4b644100-e948-11ea-99a6-e65fcdd5af65.png)
### 5 is made of Noun's and G is made of Verb's

Created two wordcloud's one of Noun and the other one of Verb with the text extracted from scraping of IDRBT website. Scrapped 5 pages of IDRBT website in order to fill the image with word's. 

## Modules to be installed
1. Requests(Used to make a request to a web page , we are using get request to idrbt url)
```python
pip install requests
```
2. BeautifulSoup(For parsing the content we got after making the request)
```python
pip install bs4
```
3. TextBlob(Used for processing textual data. It has an API which is can be used for tagging parts of speech)
```python
pip install textblob
```
4. Numpy(To get the array or a matrix, or square pixels arranged in columns and rows)
```python
pip install numpy
```
5. Pillow(Python imaging library which adds support for opening, manipulting, and saving images)
```python
pip install pillow
```
6. Matplotlib(Plotting library )
```python
pip install matplotlib
```
Import the modules
**warnings module**
I had imported warning module as my requests are unable to verify SSL certificate of IDRBT website because of which when i send a request to the website it throws me an error. In order to avoid this i turned off the verification by using parameter (verify = False). There are even other safer way's to do this i don't recommend anyone to do this if there are into production. As i turned off the verification python gives me the warning to turn on the verification in order to dodge those warning's i had imported warnings module and ignored them.
## Text Extraction
After importing all the modules, i had taken few url's of IDRBT in order to gather enough text for processing. 
I had created a small function which is used to get the required text out of the page. First i send a GET request to the specified url(parameter of the function) then i parsed the content in the url using BeautifulSoup lxml parser(default) . The data to be extracted is in the div tag with attributes 'class'= 'col-md-8' as all the pages are in same format no need to worry about changing the attributes and finally the function returns the text in it using get_text() method. I had stored all the url's in a list and gathered the text in all the url's by iterating throught the list. 

**TextBlob**
Textblob is a library for processing textual data. It provides a simple API with which we can tag parts of speech of each word in text on the basis of definition and context. So we create a textblob object and pass our text with it and we call function of textblob in order to do a parts of speech tagging, then we sepearte noun if the tags are 'NN' , 'NNS', 'NNP' OR 'NNPS' and similarly for verbs there would be different tagging.
I had downloaded two images one is image of 5 and the other is image of G **please remove background in both the images** 

**Wordcloud Mask**

So we use external images as a mask to give a specific shape to our workcloud. We need to have the image in our current directory and give it to the wordcloud function. A wordcloud function displays a list of words, the importance of each being shown with font size or color. This format is useful for quickly perceiving the most prominent terms. 
So i created two masks maskarray, maskarray2 to specific the shape. In order to plot this i had used matplotlib.pyplot along with subplots for each cloud. Then create wordcloud functions with mask parameter in it and generate the cloud for both noun and verb.

