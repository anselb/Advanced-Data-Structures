import time


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
    # Find an index of a word close to prefix with binary search and check if
    # the word starts with the prefix
    found_words = []
    index = binary_search_recursive(array=words, item=prefix)
    if words[index].startswith(prefix):
        found_words.append(words[index])

    # Get the indexes to the left and right of index if they are within the
    # word list bounds
    left = index
    right = index
    if left > 0:
        left -= 1
    if right < len(words) - 1:
        right += 1

    # Add words to the left and right of the found index until the words don't
    # match the prefix anymore
    while ((words[left].startswith(prefix) and words[left] not in found_words) or
            (words[right].startswith(prefix) and words[right] not in found_words)):
        if words[left].startswith(prefix):
            found_words.append(words[left])
        if words[right].startswith(prefix):
            found_words.append(words[right])

        if left > 0:
            left -= 1
        if right < len(words) - 1:
            right += 1

    return found_words

def benchmark(words, prefixes):
    # Return float: time to autocomplete all prefixes
    # Generate prefixes by selecting words from the dictionary file and slicing
    # the frst half of their letters -> word[:len(word)//2]
    start_time = time.time()
    for prefix in prefixes:
        autocomplete(words, prefix)
    finish_time = time.time()

    time_to_autocomplete_all = finish_time - start_time
    return time_to_autocomplete_all

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
    if item < array[index]:
        return binary_search_recursive(array, item, left, index)
    else:
        return binary_search_recursive(array, item, index, right)


all_words = get_words('/usr/share/dict/words')

# Test with prefix 'yab'
print(all_words[232769])
print(autocomplete(all_words, 'yab'))
# yab - ['yaba', 'yabber', 'yabbi', 'yabble', 'yabby', 'yabu']

# Test with an edge case
words = ['a', 'z']
print(autocomplete(words, 'ab'))
# Orignally printed 'z' because binary search returned the right index of 1 and
# the autocomplete function would blindly put that index in the list of matched
# words without checking to make sure it matches the prefix

# Test with a lot of prefixes
all_prefixes = set([word[:len(word)//2] for word in all_words])
all_prefixes.remove('')
time = benchmark(all_words, all_prefixes)
print('Took {} seconds to benchmark {} prefixes on {} words'.format(time, len(all_prefixes), len(all_words)))
