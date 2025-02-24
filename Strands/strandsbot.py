import itertools

# Height = 8 letters
# Width = 6 letters

# Read words from a scrabble_words.csv into a hashmap using hash()
wordlist = {}
with open("scrab_words.csv") as f:
    for line in f:
        word = line.strip()
        wordlist[word] = hash(word)

# Put wordlist into a dictionary by length
wordlist_by_length = {}
for word in wordlist:
    length = len(word)
    if length not in wordlist_by_length:
        wordlist_by_length[length] = [word]
    else:
        wordlist_by_length[length].append(word)

def filter_words_by_length(wordlist, target_length):
    return [word for word in wordlist if len(word) == target_length]

def make_grid():
    grid = []
    for i in range(1, 9):  # Loop through 8 rows
        row = input(f"Enter row {i}: ").strip().upper()  # Convert to uppercase immediately
        grid.append(list(row))  # Convert string to list
    return grid
def is_spangram(coords, grid):
    rows = len(grid)
    cols = len(grid[0])
    top_edge = bottom_edge = left_edge = right_edge = False
    for x, y in coords:
        if x == 0:
            top_edge = True
        if x == rows - 1:
            bottom_edge = True
        if y == 0:
            left_edge = True
        if y == cols - 1:
            right_edge = True
        if (top_edge and bottom_edge) or (left_edge and right_edge):
            return True
    return False



def is_valid_arrangement(grid, words):
    used_coordinates = set()  # Set to track used coordinates across all words
    for word in words:
        if not find_word_in_grid(word, grid, used_coordinates):
            return False
        if not is_spangram(used_coordinates):
            return False
    return True

def find_word_in_grid(word, grid, used_coordinates):
    rows = len(grid)
    cols = len(grid[0])
    word = word.upper()
    word_letters = list(word)
    letter_locations = get_letter_locations(grid)

    directions  = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)] 

    first_letter = word_letters[0]

    memo = {}
    def DFS(x, y, idx, path):
        if idx == len(word):
            used_coordinates.update(path)
            return True
        if (x, y, idx) in memo:  # Skip already computed paths
            return memo[(x, y, idx)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in path and grid[nx][ny] == word[idx]:
                if (nx, ny) not in used_coordinates:
                    if DFS(nx, ny, idx + 1, path + [(nx, ny)]):
                        memo[(nx, ny, idx + 1)] = True  # Cache the result
                        return True
        memo[(x, y, idx)] = False  # Cache the result if no valid path found
        return False
    
    for start in letter_locations.get(first_letter, []):
        if DFS(start[0], start[1], 1, [start]):
            return True
    return False

def widdle_dictionary(wordlist, grid):
    valid_words = {word for word in wordlist if len(word) >= 4 and find_word_in_grid(word, grid, set())}
    return {word: wordlist[word] for word in valid_words}

def find_n_words(wordlist, n):
    # Find n wordlengths that add up to 48
    lens = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    combs = set()

    for i in range(0, n):
        for comb in itertools.combinations(lens, i):
            if sum(comb) == 48:
                combs.add(tuple(sorted(comb)))  # Ensure unique combinations by sorting
    return list(combs)

def get_letter_locations(grid):
    locations = {}
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    I = []
    J = []
    K = []
    L = []
    M = []
    N = []
    O = []
    P = []
    Q = []
    R = []
    S = []
    T = []
    U = []
    V = []
    W = []
    X = []
    Y = []
    Z = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            letter = grid[i][j]
            if letter == 'A':
                A.append((i, j))
            elif letter == 'B':
                B.append((i, j))
            elif letter == 'C':
                C.append((i, j))
            elif letter == 'D':
                D.append((i, j))
            elif letter == 'E':
                E.append((i, j))
            elif letter == 'F':
                F.append((i, j))
            elif letter == 'G':
                G.append((i, j))
            elif letter == 'H':
                H.append((i, j))
            elif letter == 'I':
                I.append((i, j))
            elif letter == 'J':
                J.append((i, j))
            elif letter == 'K':
                K.append((i, j))
            elif letter == 'L':
                L.append((i, j))
            elif letter == 'M':
                M.append((i, j))
            elif letter == 'N':
                N.append((i, j))
            elif letter == 'O':
                O.append((i, j))
            elif letter == 'P':
                P.append((i, j))
            elif letter == 'Q':
                Q.append((i, j))
            elif letter == 'R':
                R.append((i, j))
            elif letter == 'S':
                S.append((i, j))
            elif letter == 'T':
                T.append((i, j))
            elif letter == 'U':
                U.append((i, j))
            elif letter == 'V':
                V.append((i, j))
            elif letter == 'W':
                W.append((i, j))
            elif letter == 'X':
                X.append((i, j))
            elif letter == 'Y':
                Y.append((i, j))
            elif letter == 'Z':
                Z.append((i, j))
    return {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 'K': K, 'L': L, 'M': M,
            'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}

def find_word_combos(wordlist, grid, n, spangram):
    length_combos = [(6, 8, 8, 8, 9, 9)]  # Example hardcoded length combo
    valid_combos = []

    for combo in length_combos:
        valid_combos = [filter_words_by_length(wordlist, length) for length in combo]
        for words in itertools.product(*valid_combos):
            # Ensure the provided spangram is included in the set of words
            if spangram not in words:
                continue
            # Ensure there are no repeated words
            if len(set(words)) != len(words):
                continue
            # Check if the word arrangement is valid (including a spangram covering the grid)
            if is_valid_arrangement(grid, words):
                return words
    return None
def find_word_path(word, grid):
    rows = len(grid)
    cols = len(grid[0])
    word = word.upper()
    word_letters = list(word)
    letter_locations = get_letter_locations(grid)
    
    directions = [(0, 1), (1, 0), (1, 1), (1, -1),
                  (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    
    memo = {}
    def DFS(x, y, idx, path):
        if idx == len(word):
            return path
        if (x, y, idx) in memo:
            return None
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in path:
                if grid[nx][ny] == word[idx]:
                    result = DFS(nx, ny, idx + 1, path + [(nx, ny)])
                    if result is not None:
                        return result
        memo[(x, y, idx)] = None
        return None
    
    for start in letter_locations.get(word_letters[0], []):
        result = DFS(start[0], start[1], 1, [start])
        if result is not None:
            return result
    return None

def find_all_valid_spangrams(wordlist, grid):
    valid_spangrams = []
    for word in wordlist:
        if len(word) < 4:  # Adjust word length criteria as needed
            continue
        path = find_word_path(word, grid)
        if path is not None:
            # Convert path to a set to avoid duplicate coordinates
            if is_spangram(set(path), grid):
                valid_spangrams.append(word)
    return valid_spangrams

if __name__ == '__main__':
    # g = [
    #     ['S', 'E', 'L', 'F', 'S', 'H'],
    #     ['C', 'J', 'L', 'Y', 'I', 'N'],
    #     ['O', 'R', 'P', 'I', 'O', 'S'],
    #     ['N', 'E', 'T', 'G', 'I', 'T'],
    #     ['R', 'H', 'E', 'B', 'N', 'B'],
    #     ['O', 'R', 'P', 'U', 'M', 'L'],
    #     ['S', 'L', 'Y', 'P', 'E', 'B'],
    #     ['A', 'T', 'S', 'U', 'E', 'E']
    # ]

    # t = is_valid_arrangement(g, ('ALPEEN', 'ELIGIBLE', 'EPYLLION', 'HERPTILE', 'BUMBLEBEE', 'EPYLLIONS'))
    # print(t)
    g = make_grid()
    # # # Modify the wordlist
    widdled_dict = widdle_dictionary(wordlist, g)
    # print(widdled_dict)

    # word_lengths = find_n_words(widdled_dict, 6)
    # print(word_lengths)
    # print(len(word_lengths))
    # print(is_spangram([(0, 6), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (7, 2)]))  # Example coordinates for "STINGERS"

    # words = find_word_combos(widdled_dict, g, 6, "STINGERS")
    # print(words)
    # p = find_word_path("STINGERS", grid=g)
    # print(is_spangram(p,g))
    print(find_all_valid_spangrams(widdled_dict, g))