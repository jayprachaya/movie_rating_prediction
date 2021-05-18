from wordcloud import WordCloud # STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


def make_wordcloud(text):
    wordcloud = WordCloud(max_font_size=100, max_words=100, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    # plt.show()
    # Save the image in the img folder:
    wordcloud.to_file("img/wordcloud.png")
    return wordcloud