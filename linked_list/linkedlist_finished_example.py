'''
The goal of this program is to use a linked list similarly to a queue.
The list will store songs, and the user will be able to add songs and play next song.
The user can also remove a song at an index, or add a new song at an index.
'''

from collections import deque

class Playlist:
    def __init__(self):
        '''
        Initialize an empty linked list.
        '''
        self.queue = deque()

    def add_song(self, song):
        '''
        Add new song to the queue.
        '''
        self.queue.append(song)

    def play_next(self) -> str:
        '''
        Return the next song in the queue.
        '''
        return self.queue.popleft()

    def remove_song(self, index):
        '''
        Remove a song from the queue.
        Remember that the performance of this method is O(n), not O(1).
        '''
        del self.queue[index]

    def add_song_at(self, index, song):
        '''
        Add a song at a specific index.
        Remember that the performance of this method is O(n), not O(1).
        '''
        self.queue.insert(index, song)


# Test code ===============================================================

# Create playlist
playlist = Playlist()

# Add some songs
playlist.add_song("Bohemian Rhapsody")
playlist.add_song("Stairway to Heaven")

# Play next song
print(playlist.play_next()) # Bohemian Rhapsody

# Add some more songs
playlist.add_song("Beethoven Symphony No. 5")
playlist.add_song("Star Wars: Imperial March")
playlist.add_song("Radioactive")

# Play next song
print(playlist.play_next()) # Stairway to Heaven

# Remove a song. Remember that the performance of this method is O(n), not O(1).
playlist.remove_song(1) # Remove Star Wars: Imperial March

# Add a song at a specific index. Remember that the performance of this method is O(n), not O(1).
playlist.add_song_at(1, "Star Wars Main Theme") # Add Star Wars Main Theme at index 1, replacing Star Wars: Imperial March

# Play the rest of the songs
print(playlist.play_next()) # Beethoven Symphony No. 5
print(playlist.play_next()) # Star Wars Main Theme
print(playlist.play_next()) # Radioactive

# Once the program has run, this should be the output:
# Bohemian Rhapsody
# Stairway to Heaven
# Beethoven Symphony No. 5
# Star Wars Main Theme
# Radioactive