COLORS = {"AliceBlue": "#f0f8ff", "Aquamarine": "#7fffdf", "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2",
          "Chartreuse2": "76ee00", "Chocolate": "#d2691e", "DarkOliveGreen1": "#caff70", "DeepSkyBlue1": "#00bffff",
          "Firebrick": "#b22222", "ForestGreen": "#228b22"}

print(COLORS.keys())
color_name = input("Choose color name: ")
while color_name != "":
    if color_name in COLORS:
        print("{:10s} is {}".format(color_name, COLORS[color_name]))
    else:
        print("There is no such color name")
    color_name = input("Choose color name: ")
