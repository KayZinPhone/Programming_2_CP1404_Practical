class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        if self.reflection == True:
            return self.name

    def __str__(self):
        return "{}, {}, Reflection ={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

languages = []
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
java = ProgrammingLanguage("Java","Static", True, 1995)

languages.append(ruby)
languages.append(python)
languages.append(visual_basic)
languages.append(java)
print("The dynamically typed languages are:")
for language in languages:
    print(ProgrammingLanguage.is_dynamic(language))

print("This is for Ruby language: \n", ruby)
print("This is for Java language: \n", java)
print("This is for Python language: \n", python)
print("This is for Visual Basic language: \n", visual_basic)



