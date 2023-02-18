import os
import socket
from collections import Counter

def get_my_ip_address():
    """Get the IP address of the current machine"""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def count_words(file_path, counter):
    """
    Count the number of words in the file and update the Counter object with the counts of each word
    :param file_path: The path of the file to be read
    :param counter: The Counter object to be updated with the counts of each word
    :return: The total number of words in the file
    """
    total_word_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                if file.name.endswith("IF.txt"):
                    counter.update(line.replace("Â", "").split())
                total_word_count += len(line.replace("Â", "").split())
    return total_word_count

def main():
    # Set the path of the directory containing the text files
    dir_path = "/home/data"

    # Initialize a Counter object to keep track of the word counts
    counter = Counter()

    # Remove the result.txt file if it already exists
    result_file_path = os.path.join(dir_path, "result.txt")
    if os.path.exists(result_file_path):
        os.remove(result_file_path)

    # Create a string to hold the output
    output_string = "****|| Text files at location: {} ||****\n".format(dir_path)

    # Loop through each file in the directory and count the number of words
    text_files_word_counts = {}
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(dir_path, file_name)
            text_files_word_counts[file_name] = count_words(file_path, counter)
            output_string += "{}\n".format(file_name)

    # Calculate the total word count for each file and the grand total word count
    grand_total_word_count = sum(text_files_word_counts.values())
    output_string += "\n****|| Total number of words in each file ||****\n"
    for file_name, word_count in text_files_word_counts.items():
        output_string += "Total number of words in [{}]: {}\n".format(file_name, word_count)
    output_string += "\n****|| Grand total (total number of words in both files) ||****\n"
    output_string += "Total number of words in both files [{}]: {}\n".format(
        ", ".join(text_files_word_counts.keys()), grand_total_word_count)

    # Get the top 3 words with the highest counts in the IF.txt file
    if "IF.txt" in text_files_word_counts:
        top_words = counter.most_common(3)
        output_string += "\n****|| Top 3 words with maximum number of counts in IF.txt ||****\n"
        output_string += "{}\n".format(top_words)

    # Get the IP address of the current machine
    ip_address = get_my_ip_address()
    output_string += "\n****|| IP address ||****\n"
    output_string += "Your Computer IP Address is: {}\n".format(ip_address)

    # Write the output string to the result.txt file and print it to the console
    with open(result_file_path, "w") as result_file:
        result_file.write(output_string)
    print(output_string.strip())

if __name__ == '__main__':
    main()
