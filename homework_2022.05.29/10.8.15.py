def GetPossibleStates(cols_to_keep):
    all_states = ['S', 'I0']
    for i in range(len(cols_to_keep)):
        all_states.append('M' + str(i + 1))
        all_states.append('D' + str(i + 1))
        all_states.append('I' + str(i + 1))
    all_states.append('E')
    return all_states

def Transition_matrix(num_transitions):
    transition_matrix = {}
    for state1, row in num_transitions.items():
        row_total = sum(row.values())
        transition_matrix[state1] = {}
        for state2, val in row.items():
            if row_total != 0:
                transition_matrix[state1][state2] = val / row_total
            else:
                transition_matrix[state1][state2] = val
    return transition_matrix

def NumEmissions(alphabet, all_states):
    num_emissions = {}
    for state in all_states:
        num_emissions[state] = {}
        for symbol in alphabet:
            num_emissions[state][symbol] = 0
    return num_emissions

def GetEmissionMatrix(num_emissions):
    emission_matrix = {}
    for state, row in num_emissions.items():
        row_total = sum(row.values())
        emission_matrix[state] = {}
        for symbol, val in row.items():
            if row_total != 0:
                emission_matrix[state][symbol] = val / row_total
            else:
                emission_matrix[state][symbol] = val
    return emission_matrix

def TransitionProbabilities(all_states, alignment, cols_to_keep):
    num_transitions = {}
    for state1 in all_states:
        num_transitions[state1] = {}
        for state2 in all_states:
            num_transitions[state1][state2] = 0
    for current_seq in alignment:
        current_state = 'S'
        col_idx = 0
        while current_state != 'E':
            if current_state == 'S':
                current_state_idx = 0
            else:
                current_state_idx = int(''.join(x for x in current_state if x.isdigit()))
            if col_idx == len(current_seq):
                next_state = 'E'
            elif col_idx in cols_to_keep:
                if current_seq[col_idx] != '-':
                    next_state = 'M' + str(current_state_idx + 1)
                else:
                    next_state = 'D' + str(current_state_idx + 1)
            elif col_idx not in cols_to_keep and current_seq[col_idx] != '-':
                next_state = 'I' + str(current_state_idx)
            if next_state != current_state or (current_state.startswith('I') and current_seq[col_idx] != '-'):
                num_transitions[current_state][next_state] += 1
                current_state = next_state

            col_idx += 1
            
    return num_transitions
  
def GetColsToKeep(alignment, insertion_threshold):
    cols_to_keep = []
    num_cols = len(alignment[0])
    for j in range(num_cols):
        col = []
        for i in range(len(alignment)):
            col.append(alignment[i][j])
        if sum(x == '-' for x in col) / len(col) <= insertion_threshold:
            cols_to_keep.append(j)
    return cols_to_keep

def ProfileHMM(alignment, alphabet, insertion_threshold):
    cols_to_keep = GetColsToKeep(alignment, insertion_threshold)
    all_states = GetPossibleStates(cols_to_keep)
    num_transitions = TransitionProbabilities(all_states, alignment, cols_to_keep)
    transition_matrix = Transition_matrix(num_transitions)
    num_emissions = NumEmissions(alphabet, all_states)
    
    for current_seq in alignment:
        current_state = 'S'
        col_idx = 0
        while current_state != 'E':
            if current_state == 'S':
                current_state_idx = 0
            else:
                current_state_idx = int(''.join(x for x in current_state if x.isdigit()))
            if col_idx == len(current_seq):
                next_state = 'E'
            elif col_idx in cols_to_keep:
                if current_seq[col_idx] != '-':
                    next_state = 'M' + str(current_state_idx + 1)
                else:
                    next_state = 'D' + str(current_state_idx + 1)
            elif col_idx not in cols_to_keep and current_seq[col_idx] != '-':
                next_state = 'I' + str(current_state_idx)
            if next_state != 'E':
                sym = current_seq[col_idx]
                if next_state != current_state or (current_state.startswith('I') and sym != '-'):
                    if sym != '-':
                        num_emissions[next_state][sym] += 1
            current_state = next_state
            col_idx += 1
            
    emission_matrix = GetEmissionMatrix(num_emissions)
    return transition_matrix, emission_matrix


def PrintAns(*argv, delim="\t", separator="--------"):
    for idx, matrix in enumerate(argv):
        row_labels = list(matrix.keys())
        col_labels = list(matrix[row_labels[0]].keys())
        if idx == 0:
            to_print = delim + delim.join(col_labels) + '\t\n'
        else:
            to_print = delim + delim.join(col_labels) + '\n'
        for r_label in row_labels:
            tmp = [r_label]
            for c_label in col_labels:
                val = matrix[r_label][c_label]
                if val == 0:
                    val_str = '0'
                elif val == int(val):
                    val_str = '{:.1f}'.format(val)
                else:
                    val_str = '{:.3f}'.format(val).rstrip('0')
                tmp.append(val_str)
            to_print += delim.join(tmp)
            if r_label != row_labels[-1]:
                to_print += '\n'
        print(to_print)
        if idx != len(argv) - 1:
            print(separator)


if __name__ == "__main__":
    f = open('input.txt', 'r')
    tmp = f.read().splitlines()
    insertion_threshold = float(tmp[0])
    alphabet = tmp[2].split()
    alignment = []
    for i in range(4, len(tmp)):
        alignment.append(tmp[i])
    transition_matrix, emission_matrix = ProfileHMM(alignment, alphabet, insertion_threshold)
    PrintAns(transition_matrix, emission_matrix)
