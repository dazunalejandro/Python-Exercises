'''
Create a word cloud to visualize 
top most frequent 200 words in the
book 'Pride and Prejudice"
'''
from exercise9_10 import create_dict
from wordcloud import WordCloud

def main():

    frequencies_200 = dict(sorted(create_dict().items(), reverse=True, key=lambda x:x[1])[:200])
    
    wordcloud = WordCloud(colormap='prism', background_color='white')
    wordcloud = wordcloud.fit_words(frequencies_200)
    wordcloud = wordcloud.to_file('PrideAndPrejudice.png')

if __name__ == "__main__":
    main()