"""
CP1404/CP5632 Practical - Suggested Solution
Cleanup inconsistent song lyrics file names

Note: A complete solution for this exercise is NOT provided.
It's a very good thinking exercise and is less about the patterns we usually focus on
and more of a "tricky" problem to solve.
"""
import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # No solution is provided, but you may want to consider the patterns to look out for and fix
    # E.g. a lowercase letter followed by a capital, like "tN" should become "t_N"
    # Try doing this on paper first and then see if you can systematise it

    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    # return new_name
    new_name1 = ""
    for i in range(1, len(filename)):
        if (filename[i-1].islower() and filename[i].isupper()) \
                or (filename[i-1].isupper() and filename[i].isspace() and filename[i+1].isupper()) \
                or (filename[i].isupper() and filename[i-1].isupper())\
                or (filename[i].isupper() and filename[i-1].isspace() and filename[i-2].islower()
                or (filename[i-1].islower() and filename[i].isspace() and filename[i+1].islower())):
            new_name1 = new_name1+"_"+filename[i]
        else:
            new_name1 += filename[i]

    return filename[0]+new_name1


main()
