import os
import shutil as myshutil 
import sqlite3
import tkinter as tk
from tkinter import filedialog, simpledialog 
import pygame
import zipfile

# SongStorageGUI class for the graphical user interface
class SongStorageGUI:
    def __init__(self, master):
        
        # Initialize the GUI
        
        self.master = master
        master.title("Song Storage GUI")
        
        # Initialize the SongStorage instance

        self.storage = SongStorage("Storage", "song_database.db")
        
        # Create GUI elements

        self.label = tk.Label(master, text="File Path:")
        self.label.pack()

        self.file_path_entry = tk.Entry(master, width=60)
        self.file_path_entry.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.artist_entry = tk.Entry(master, width=30)
        self.artist_entry.pack()
        self.artist_entry.insert(tk.END, "Artist Name")

        self.song_name_entry = tk.Entry(master, width=30)
        self.song_name_entry.pack()
        self.song_name_entry.insert(tk.END, "Song Name")

        self.release_date_entry = tk.Entry(master, width=30)
        self.release_date_entry.pack()
        self.release_date_entry.insert(tk.END, "2022-01-01")

        self.tags_entry = tk.Entry(master, width=30)
        self.tags_entry.pack()
        self.tags_entry.insert(tk.END, "tag1, tag2")
        
        self.add_song_button = tk.Button(master, text="Add Song", command=self.add_song)
        self.add_song_button.pack()

        self.modify_data_button = tk.Button(master, text="Modify Data", command=self.modify_data)
        self.modify_data_button.pack()

        # Initialize pygame mixer
        pygame.mixer.init()



    def browse_file(self):
        # Open a file dialog to select a file and update the file path entry
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All Files", "*.*")])
    
        if file_path.lower().endswith(('.mp3', '.wav')):
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(tk.END, file_path)
        else:
            print("Please select a valid MP3 or WAV file.")
            
    def add_song(self):
        # Add a new song to the database and copy the file to the storage folder
        file_path = self.file_path_entry.get()
        artist = self.artist_entry.get()
        song_name = self.song_name_entry.get()
        release_date = self.release_date_entry.get()
        tags = self.tags_entry.get()

        song_id = self.storage.add_song(file_path, artist, song_name, release_date, tags)
        print(f"Song added with ID: {song_id}")
        
    def modify_data(self):
        # Modify the data of an existing song based on user input
        song_id = self.get_song_id_from_user()
        if song_id is not None:
            artist = self.artist_entry.get()
            song_name = self.song_name_entry.get()
            release_date = self.release_date_entry.get()
            tags = self.tags_entry.get()

            self.storage.modify_data(song_id, artist, song_name, release_date, tags)
            print(f"Song with ID {song_id} modified.")

    def get_song_id_from_user(self):
        # Prompt the user to enter a song ID
        song_id = simpledialog.askinteger("Input", "Enter Song ID:")
        return song_id
       



# SongStorage class for managing song data and storage         
class SongStorage:
    def __init__(self, storage_folder, database_path):
        # Initialize the SongStorage instance and create a database table if it doesn't exist
        self.storage_folder = storage_folder
        self.database_path = database_path
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Create the 'songs' table in the database if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                artist TEXT,
                song_name TEXT,
                release_date TEXT,
                tags TEXT
            )
        ''')
        self.connection.commit()

    def add_song(self, file_path, artist, song_name, release_date, tags):
        filename = os.path.basename(file_path)
        destination_path = os.path.join(self.storage_folder, filename)

        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        myshutil.copy(file_path, destination_path)

        self.cursor.execute('''
            INSERT INTO songs (filename, artist, song_name, release_date, tags)
            VALUES (?, ?, ?, ?, ?)
        ''', (filename, artist, song_name, release_date, tags))

        self.connection.commit()
        return self.cursor.lastrowid
        
    def modify_data(self, song_id, artist=None, song_name=None, release_date=None, tags=None):
        # Modify the data of an existing song in the database
        update_query = 'UPDATE songs SET '
        update_values = []

        if artist is not None:
            update_query += 'artist=?, '
            update_values.append(artist)

        if song_name is not None:
            update_query += 'song_name=?, '
            update_values.append(song_name)

        if release_date is not None:
            update_query += 'release_date=?, '
            update_values.append(release_date)

        if tags is not None:
            update_query += 'tags=?, '
            update_values.append(tags)

        if not update_values:
            print("No changes specified.")
            return

        update_query = update_query.rstrip(', ') + ' WHERE id=?'
        update_values.append(song_id)

        self.cursor.execute(update_query, tuple(update_values))
        self.connection.commit()
        print(f"Song with ID {song_id} updated.")

                
    def get_file_path(self, song_id):
        # Get the file path of a song based on its ID
        self.cursor.execute('SELECT filename FROM songs WHERE id=?', (song_id,))
        result = self.cursor.fetchone()
        if result:
            filename = result[0]
            return os.path.join(self.storage_folder, filename)
        else:
            print(f"Song with ID {song_id} not found.")
            return None

# Main program execution
if __name__ == "__main__":
    # Create the Tkinter root window and start the GUI application
    root = tk.Tk()
    app = SongStorageGUI(root)
    root.mainloop()

