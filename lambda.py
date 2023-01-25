#Write a lambda function to sort a list of tuples in ascending order according to number in second position of each tuple.

subject_scores = [('English', 88), ('Science', 90), ('Maths', 97) , ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_scores)
subject_scores.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_scores)