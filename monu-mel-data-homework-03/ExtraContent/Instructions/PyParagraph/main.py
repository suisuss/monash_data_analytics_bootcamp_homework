import re
import os


file_paths = [os.path.join('raw_data', 'paragraph_1.txt'), os.path.join('raw_data', 'paragraph_2.txt')] # Input
analysis_file_path = os.path.join("analysis", "analysis.txt") # Output.

test = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold."

analysis_file = open(analysis_file_path, "a")

passage_count = 0
for file_path in file_paths:
    with open(file_path) as file:
        paragraph = file.read()
        sentences = re.split("(?<=[.!?]) +", paragraph)
        
        word_count = 0
        sentence_lengths = []
        letter_count_per_word = []
        for sentence in sentences:
            sentence_split = sentence.split(" ")
            sentence_lengths.append(len(sentence_split))

            for word in sentence_split:
                word_count += 1
                letter_count_per_word.append(len(word))

        num_of_sentences = len(sentence_lengths)
        average_sentence_length = sum(sentence_lengths)/len(sentence_lengths)
        average_letter_count = sum(letter_count_per_word)/len(letter_count_per_word)

        passage_count += 1

        output = f'''
        Paragraph Analysis: {passage_count}
        -----------------
        Approximate Word Count: {word_count}
        Approximate Sentence Count: {num_of_sentences}
        Average Letter Count: {round(average_letter_count, 1)}
        Average Sentence Length: {average_sentence_length}
        '''

        analysis_file.write(output)

analysis_file.close()


        

            

