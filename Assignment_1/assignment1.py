"""Name: Kay_Zin_Phone
Date: 06/12/2018
Detail: This is a simple program for tracking song list. User can load all the
songs. User can also add a new song for learning. User can change the status of the song to mark the song as learned
or not.
Link: https://github.com/JCUS-CP1404/a1--KayZinPhone"""

MENU = """Songs To Learn 1.0 - by Kay Zin Phone"""
MENU_1 = """MENU:
L - List songs
A - Add new song
C - Complete a song
Q - Quit"""

"""
Loading all the song and display in list from song.csv file
"""
"""
Pseudocode: 
count = -1
for song in songs:
    count = count+1
    if the index of songs list is inputted as 'y'
        do increase the count of 'y'
        print output
    else if the index of song list is inputted as 'n'
        do increase the count of 'n'
        print output
print output

"""


def list_song(songs):
    count = -1
    y_count = 0
    n_count = 0
    for song in songs:
        count += 1
        # count the number of learned songs in list
        if 'y' in song.strip().split(",")[3]:
            print("{}. {:2s} {:30} - {:25} ({})".format(count, " ", song.strip().split(",")[0],
                                                        song.strip().split(",")[1], song.strip().split(",")[2]))
            y_count += 1
        # count the number of unlearned songs in list
        elif 'n' in song.strip().split(",")[3]:
            print("{}. {:2s} {:30} - {:25} ({})".format(count, "*", song.strip().split(",")[0],
                                                        song.strip().split(",")[1], song.strip().split(",")[2]))
            n_count += 1
    print("{} songs learned, {} songs still to learn".format(y_count, n_count))


"""
Adding a new song to songs.csv file with the name of title, artist and year
"""


def add_new_song(song_list):
    songs = []
    for song in song_list:
        songs.append(song.strip())

    # The input should not be blank in the title, artist and year. The year input should be greater than 0 and the
    # input should not be character.
    title = input("Title: ")
    while title == "":
        print("Title cannot be blank")
        title = input("Title: ")
    artist = input("Artist: ")
    while artist == "":
        print("Artist cannot be blank")
        artist = input("Artist: ")

    year = 0
    while not year > 0:
        try:
            year = int(input("Year: "))
            if int(year) < 0:
                print("Number must be >= 0")
        except ValueError:
            print("Invalid Input")
    new_song = "{},{},{},{}".format(title, artist, year, "n")
    print("New Song: ", new_song)
    songs.append(new_song)
    print(songs)
    print("{} by {} ({}) added to song list".format(title, artist, year))
    return songs


"""Change the status of the song when the user have learned it"""

"""
Pseudocode:
songs = the list of all song tracks
for song in song_list:
    strip the song content and append to the new list songs
set get_song_index as -1
while get_song_index < 0 OR get_song_index > the length of song list
    try:
       
       input the song number that the user want to learn
       if the input is less than 0:
            print the error message
        elif the input is greater the length of song list
            print the error message
    except ValueError:
       print the error if user inputs the string or blank
    
    for the content in song_list:
        if the index of content is equal to 'y'
            print the message that the song is already learned
        elif the index of content is not equal to 'y'
            the index of content is change to 'y'
            update to the song list
    return the song list
    
"""


def complete_song(song_list):
    songs = []
    for song in song_list:
        songs.append(song.strip())
    print(songs)
    get_song_index = -1

    # Check the input data that is valid or not, the input data must be between 0 and the length of song list. The input should not be character
    while get_song_index < 0 or get_song_index > len(songs):
        try:
            get_song_index = int(input("Enter the number of a song to mark as learned\n>>>"))
            if get_song_index < 0:
                print("Number must be >= 0")
            elif get_song_index >= len(songs):
                print("The invalid song number")
                get_song_index = int(input("Enter the number of a song to mark as learned\n>>>"))

        except ValueError:
            print("The input is invalid")

    songs = change_status(songs, get_song_index)
    return songs


"""Check the all the songs have been already learned or not"""


def is_learned(song_list):
    print("song_list in is_learned", song_list)
    status = False
    count = 0
    songs = song_list

    for song in songs:
        if song.strip().split(",")[3] == "y":
            count += 1

    if count == len(songs):
        status = True
    return status


"""The changing method  of the song status"""


def change_status(song_list, get_index):
    songs = song_list

    for index in range(0, len(songs)+1):
        if get_index == index and songs[index].strip().split(",")[3] != 'y':
            temp = songs[index].strip()
            # print("Your input is same here but this song have not learned")
            temp_list = temp.split(",")
            print("Temp list1: -----------------\n", temp_list)
            temp_list[3] = 'y'
            print("Temp list2: -----------------\n", temp_list)
            temp_song = ",".join(temp_list)
            songs[index] = temp_song

            print("{} by {} learned".format(songs[0], songs[1]))
            # return songs

        elif get_index == index and songs[index].strip().split(",")[3] == 'y':
            print("You have already learned {}".format(songs[get_index].strip().split(",")[0]))

    return songs


"""Read all the songs file in the csv file"""


def read_song():
    read_file = open("songs.csv", "r")
    return read_file.readlines()


"""Write the changed data to csv file"""


def write_song(song_list):

    write_file = open("songs.csv", "w")
    write_file.write("\n".join(song_list))


def main():
    songs = read_song()
    all_song_list = songs

    print("Song list in main method: ", all_song_list)
    print(MENU)
    print("{} songs loaded".format(len(all_song_list)))
    print(MENU_1)
    choice = input(">>>").upper()

    # The program will ask for the input until user inputs 'Q'.If the user inputs other character except the require characters
    # the error message will be shown and the program will ask the input again
    while choice != 'Q':
        if choice == 'L':
            list_song(all_song_list)
        elif choice == 'A':
            all_song_list = add_new_song(all_song_list)
        elif choice == 'C':
            if is_learned(all_song_list):
                print("No more songs to learn")
            else:
                all_song_list = complete_song(all_song_list)
        else:
            print("Your input is invalid")

        print(MENU_1)
        choice = input(">>>").upper()

    write_song(all_song_list)
    print("{} songs saved to songs.csv\nHave a nice day :)".format(len(all_song_list)))

if __name__ == '__main__':
    main()