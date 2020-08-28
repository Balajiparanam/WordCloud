# WordCloud
## Project Overview
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

