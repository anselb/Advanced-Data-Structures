def get_words(filename):
    # Return list: all words in filename
    with open(filename) as f:
        read_data = f.read()
    words = read_data.lower().split()
    words = list(set(words))
    words.sort()
    return words

def autocomplete(words, prefix):
    # Return list: all words given a prefix
    index = binary_search_recursive(array=words, item=prefix)
    left = index - 1
    right = index + 1
    found_words = []
    found_words.append(words[index])

    while words[left].startswith(prefix) or words[right].startswith(prefix):
        if words[left].startswith(prefix):
            found_words.append(words[left])
        if words[right].startswith(prefix):
            found_words.append(words[right])
        left -= 1
        right += 1

    return found_words

def benchmark(num_prefixes):
    # Return float: time to autocomplete all prefixes
    # Generate prefixes by selecting words from the dictionary file and slicing
    # the frst half of their letters -> word[:len(word)//2]
    pass

def binary_search_recursive(array, item, left=None, right=None):
    # Starting recursive loop using passed in array to calculate 'right'
    if left is None:
        return binary_search_recursive(array, item, 0, len(array) - 1)

    if array[left] == item:
        return left
    elif array[right] == item:
        return right
    elif right - left == 1:
        # binary search doesn't work with alphabetically sorted words with
        # capital letters
        # print((left, array[left]), (right, array[right]))

        # Use an index insted of None to get closely indexed words with prefix
        return right

    index = (right + left) // 2
    print(index, array[index], (left, right))
    if item < array[index]:
        return binary_search_recursive(array, item, left, index)
    else:
        return binary_search_recursive(array, item, index, right)


words = get_words('/usr/share/dict/words')
print(words[232769])
# yab - ['yaba', 'yabber', 'yabbi', 'yabble', 'yabby', 'yabu']
print(autocomplete(words, 'yab'))
