import itertools
first_list =[['a','b','','','e'],['','3','g'],['']]
# esto sirve para reducir la lista a un solo nivel
flatted_list = list(itertools.chain.from_iterable(first_list))
cleaned_list = [item for item in flatted_list if item]
print(cleaned_list)