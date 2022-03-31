def get_file_name():
    """Get user input for fasta file without .fasta extension"""
    return input('Please enter fasta file name: ') + '.fasta'


def parse_file(file):
    """Function that takes in fasta file as parameter and returns a list of nucleotides per sequence"""
    result = []
    with open(file) as infile:
        sequence = ''
        for line in infile:
            stripped_line = line.strip()
            if '>' in stripped_line:
                if sequence != '':
                    result.append(sequence)
                sequence = ''
            else:
                sequence += stripped_line
        result.append(sequence)
    print(len(result))
    return result


def calculate_nucl(data):
    """function that takes in a list of string sequence and returns a dictionary of length and nucleotides per
    sequence """
    result = {'Length': [], 'A': [], 'C': [], 'G': [], 'T': []}
    length = []
    a_len = []
    c_len = []
    g_len = []
    t_len = []
    for seq in data:
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        length.append(len(seq))
        for nucl in seq:
            if nucl.capitalize() == 'A':
                a_count += 1
            if nucl.capitalize() == 'C':
                c_count += 1
            if nucl.capitalize() == 'G':
                g_count += 1
            if nucl.capitalize() == 'T':
                t_count += 1
        a_len.append(a_count)
        c_len.append(c_count)
        g_len.append(g_count)
        t_len.append(t_count)
    result['Length'] = length
    result['A'] = a_len
    result['C'] = c_len
    result['G'] = g_len
    result['T'] = t_len
    return result


def calculate_gc(data):
    """function takes in nucleotide dictionary and returns a list gc ratio for respective sequence"""
    result = []
    all_seq_len = data['Length']
    all_c_len = data['C']
    all_g_len = data['G']
    for i in range(len(all_seq_len)):
        percentage = ((all_c_len[i] + all_g_len[i]) / all_seq_len[i]) * 100
        result.append(round(percentage, 1))
    return result


def print_output(nucl, gc):
    """function that prints formatted table"""
    nucl['%GC'] = gc
    print('Total number of sequences in fasta file: ' + str(len(nucl['Length'])))
    print('{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format('Length', 'A', 'C', 'G', 'T', '%GC'))
    for i in range(len(nucl['Length'])):
        print('{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'
              .format(nucl['Length'][i], nucl['A'][i], nucl['C'][i], nucl['G'][i], nucl['T'][i], nucl['%GC'][i]))


if __name__ == '__main__':
    """main function that calls all the necessary functions for program"""
    file = get_file_name()
    parsed_data = parse_file(file)
    nucl_dict = calculate_nucl(parsed_data)
    gc_ratio = calculate_gc(nucl_dict)
    print_output(nucl_dict, gc_ratio)