MENU = """Songs to Learn 1.0 - by Lindsay Ward"""
MENU_1 = """Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit"""

def main():
    songs = []
    get_command = input(">>>").upper()
    while get_command != 'Q':
        if get_command == 'L':
            list_song(songs)
        elif get_command == 'A':
            add_song()
        elif get_command == 'C':
            complete_song()
        else:
            print("Your input is invalid")
            get_command = input("Enter a valid input: ").upper()
    print("{} songs saved to songs.csv\nHave a nice day :)")


def complete_song():
    c_song = int(input("Enter the number of a song to mark as learned"))
    if(c_song >= 0):
    elif(c_song > len(songs)):
        print("Invalid song number")
    else:
        print("Number must be >= 0")


def add_song():
    title = input("Title: ")
    artist = input("Artist: ")
    year = input("Year: ")
    songs.append(title,artist,year)
    print("{} by {} ({}) added to song list")

def list_song(list):
    for i in range(0,len(list)):
        print("{}. {:10} - {:2s} {}".format())
    print("{} songs learned, {} songs still to learn")
main()