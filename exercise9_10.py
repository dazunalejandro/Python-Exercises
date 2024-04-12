'''
Produce statistics about the text file, including:
    * the total word count
    * the total character count
    * the average word length
    * the average sentence length
    * Word distribution containing frequency counts of all words
    * Top 10 longest words
'''
import numpy as np
import matplotlib.pyplot as plt

def create_dict():
    dict = {}
    with open('book.txt', 'r', encoding="utf8") as book:
        for line in book:
            for word in line.strip().split(" "):
                word.lower()
                if word != '':
                    if word not in dict:
                            dict[word] = 1
                    else:
                        dict[word] += 1


    return dict

def plot_word_distribution(dict):
    fig, axs = plt.subplots(2,2)
    bar_width = 0.5

    words, frequencies = zip(*dict.items())
    sort_index = np.argsort(frequencies)[::-1]
    words = np.array(words)[sort_index]
    frequencies = np.array(frequencies)[sort_index]
    indexes = np.arange(len(words))

    axs[0,0].bar(indexes[:18], frequencies[:18], width=bar_width)
    axs[0,0].set_xticks(indexes[:18])
    axs[0,0].set_xticklabels(words[:18], rotation=90)

    axs[0,1].bar(indexes[18:36], frequencies[18:36], width=bar_width)
    axs[0,1].set_xticks(indexes[18:36])
    axs[0,1].set_xticklabels(words[18:36], rotation=90)

    axs[1,0].bar(indexes[36:54], frequencies[36:54], width=bar_width)
    axs[1,0].set_xticks(indexes[36:54])
    axs[1,0].set_xticklabels(words[36:54], rotation=90)

    axs[1,1].bar(indexes[54:76], frequencies[54:76], width=bar_width)
    axs[1,1].set_xticks(indexes[54:76])
    axs[1,1].set_xticklabels(words[54:76], rotation=90)

    for ax in axs.flat:
        ax.set(xlabel='words', ylabel='frequency')
    plt.suptitle("Word Frequency Distribution")
    plt.show()

def get_text_stats():
    try:
        with open('book.txt', 'r', encoding="utf8") as book:
            word_count = 0
            ch_count = 0
            line_count = 0
            total_word_length = 0
            for line in book:
                word_count += len(line.split(" "))
                ch_count += len(line)
                line_count += 1
                total_word_length += sum([len(word) for word in line if word != ' '])
            
        print("Total number of words: ", word_count)
        print("The total number of characters: ", ch_count)
        print("The average word length: ", total_word_length / word_count)
        print("The average sentence length: ", ch_count / line_count) 

    except FileNotFoundError:
        print("File not found!")
        
def get_top10_longest_words(dict):
    lengths = [len(word) for word in dict.keys()]
    sort_index = np.argsort(lengths)[::-1]
    words = np.array(list(dict.keys()))[sort_index]
    print("The 10 longest words are: ")
    print(words[0:10], end='\n\n')

def main():
    dict = create_dict()
    get_top10_longest_words(dict)
    get_text_stats()
    plot_word_distribution(dict)



if __name__ == "__main__":
    main()