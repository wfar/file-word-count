'''Script asks for a .txt file with words, names, cities,
etc that need to be counted and returns a dictionary
with information'''


def file_reader(file_name):
    #Opens file with word/names to be counted; creates tuple.
    with open(file_name, 'r') as f_obj:
        name = f_obj.read().strip()
        x = name.split('\n')
        name_tup = tuple(x)

    return name_tup
        
    
def word_dict(name_tup):
    #Makes dictionary of words/name as key and count as value.
    name_dict = {}
    for name in name_tup:     
        name_dict[name] = name_tup.count(name)
    
    print(name_dict)

def main():
    #Runs program
    filename = input('Enter the name of file: ')
    name_tup = file_reader(filename)
    word_dict(name_tup)

main()
    




