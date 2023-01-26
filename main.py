from data import data_list


def run_analysis(books):
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_three(books)


def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book['year'] == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book['price'])
    # Print that book's name & price to terminal
    print(f"The most expensive book in 2016 was {highest_cost_book['name']} with a price of ${highest_cost_book['price']}")


def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2018
    # Converting to a list, and saving as variable books_2018
    books_2018 = list(filter(lambda book: book['year'] == 2018, book_list))
    #Calculate the lowest number of reviews, saving that book as lowest_num_reviews
    #Using min(), with Lambda function
    lowest_num_reviews = min(books_2018, key=lambda book: book['number_of_reviews'])
    #Print that book's name to terminal 
    print(f"The book that had the lowest number of reviews in 2018 is {lowest_num_reviews['name']} with {lowest_num_reviews['number_of_reviews']} reviews!")

def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")
    #Find the top 50's list
    #Use a Lambda filter function to find the top 50's list
    #Converting to a list, and saving as variable top_fifty_list
    top_fifty_list = list(filter(lambda book: book['id'] <= 50, book_list))
    #Find which genre (fiction or non-fiction) that has appeared the most in the top 50's list
    #Find how many "fiction" books there are in the top 50 list, saving as list_fiction
    #Find how many "non-fiction" books there are in the top 50 list, saving as list_non_fiction
    list_fiction = len(list(filter(lambda book: book ['genre'] == "Fiction", book_list)))
    list_non_fiction = len(list(filter(lambda book: book ['genre'] == "Non Fiction", book_list)))
    print(f"Top Genre: Non Fiction      Frequency: {list_non_fiction}")

def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the top 50's list, and how many times it has appeared")
    #Which book has appeared the most in the top 50's list?
    #How many times has it appeared?
    #Create a list of all the titles that appeared the most in the top 50's list, saving it as list_of_book_names 
    list_of_book_names = [book['name'] for book in book_list]
    #print(list_of_book_names)
    #create some form of loop to iterate through the set(list_of_book_names)
    #[print(list_of_book_names.count(book), book) for book in set(list_of_book_names)]
    #Set up a Lambda function in order to count each occurrence
    most_pop_book_name = ""
    num_of_occurrences = 0
    for book in set(list_of_book_names):
        matching_books = list(filter(lambda name: name == book, list_of_book_names))
        current_books_num_occurrences = len(matching_books)
        if current_books_num_occurrences >= num_of_occurrences:
            most_pop_book_name = book
            num_of_occurrences = len(matching_books)

    print(f"The book that appeared the most in the top 50's list is: {most_pop_book_name} with {num_of_occurrences} appearances.")

     


# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")

def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)
