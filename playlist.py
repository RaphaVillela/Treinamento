def write_liked_songs_to_file(songs, file_name):
  with open(file_name, 'w') as file:
    file.write('Liked Songs:\n')
    for song, artist in songs.items():
      file.write(f' {song} by {artist}\n')


liked_songs = {
  'Bad Habits': 'Ed Sheeran',
  'I\'m Just Ken': 'Ryan Gosling',
  'Mastermind': 'Taylor Swift',
  'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
  'Ghost': 'Justin Bieber',
}

arquivo = 'arquivo.txt'

if __name__ == "__main__":

  write_liked_songs_to_file(liked_songs, arquivo)