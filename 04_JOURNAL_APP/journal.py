import os

def load(name):
    """
    This method creates and loads a new journal.

    :param name: The basename of the journal to load.
    :return: A new journal data stucture populated with the file data.
    """

    data = []
    filename = get_full_path(name)
    if os.path.exists(filename):
        with open(filename) as f_input:
            for entry in f_input.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_path(name)
    print('....Saving to: {}'.format(filename)) 
    
    with open(filename, 'w') as file_out:

        for entry in journal_data:
            file_out.write(entry + '\n')

def get_full_path(name):
    filename = os.path.abspath(os.path.join('.', 'journals/', name + '.jrl'))
    return filename

def add_entry(text, journal_data):
    journal_data.append(text)