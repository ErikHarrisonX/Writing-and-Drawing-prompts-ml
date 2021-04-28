import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox as mb
import random
import pandas as pd
from sklearn import tree
import openpyxl

RandomPrompt = random.randint(1,10)

#xlsx_data_file = r"fantasyWprompts.xlsx"
#xlsx_data_file1 = r"ApocalypseWprompts.xlsx"
#xlsx_data_file2 = r"ScifiWprompts.xlsx"

#df = pd.read_excel(xlsx_data_file)
#df1 = pd.read_excel(xlsx_data_file1)
#df2 = pd.read_excel(xlsx_data_file2)

#df.head()
#df1.head()
#df2.head()


#Programmers notes:
#I wasn't able to get the program to read the dataset I created and spit out the string.
#I will have to learn how to do that -_-
#In the future I will also implement a way for people to add to the Data set


#Randomizes the prompts, However will have to close program to use.
if RandomPrompt == 1:
    SettingFw = "A huge forest"
    PromptFw = "Amongst the huge forest a guy lays on the forest floor comfortably. He suddenly he hears a voice screech for him."
    SettingFuw = "Floating City"
    PromptFuw = "In the City, it was said that everything was peaceful. However on one day there was a …."
    SettingAw = "Decrepit Downtown"
    PromptAw = "As the two peope wander through the abandoned downtown streets they see many broken in stores. One of them starts groaning about not being able to go shopping,…"
    ArtF = "Draw a fairy Garden"
    ArtH = "Draw a blood pool"
    ArtL = "Draw a heart with an arrow"
    ArtSci = "Draw a floating building"
elif RandomPrompt == 2:
    SettingFw = "A floating rock city"
    PromptFw = "In a floating rock city, *Insert name* is sleeping on a rooftop of one of the rock huts. He then drowsily sits up and looks out into the horizon…"
    SettingAw = "Sewer"
    PromptAw = "The character was very smelly since he was in the sewers for weeks. He woke up from hearing one of his traps go off and he groans. He heads over and his eyes widen with what he sees…"
    SettingFuw = "Synthetic City"
    PromptFuw = "The hooded figrure walked through the market place. Hearing children run around, with synthetic limbs attached to them. As the figure neared the inn he gave the children some coins and they scurried off.."
    ArtF = "Draw a forest village"
    ArtH = "Draw a skeleton"
    ArtL = "Draw a kiss"
    ArtSci = "Draw a lazer"
elif RandomPrompt == 3:
    SettingFw = "A lush windmill village"
    PromptFw = "On a clear sunny day in *Insert name*, the windmill was circling and flowers were blowing. *Character* walks out of his house and says…."
    SettingAw = "Underground City"
    PromptAw = "The group follow the other group through the subway and into a huge chasm, they then see a huge city that has been put together with spare parts and junk…."
    SettingFuw = "Ad city"
    PromptFuw = "As the group nears the city border, all of a sudden they are bombarded with noise and images throught their screens. The guide tells everyone to turn on their adblock and everything stops. As the get into the city they see…"
    ArtF = "Draw angel wings"
    ArtH = "Draw skull"
    ArtL = "Draw Heart"
    ArtSci = "Draw Google glass"
elif RandomPrompt == 4:
    SettingFw = "Dark Castle"
    PromptFw = "As *character* was pacing among the corridors of the dark castle, he hears a thunderous alarm. He then sees within the mirror security system that someone has entered the castle. He goes to the entrance and sees…"
    SettingAw = "Mountaintop City"
    PromptAw = "As the traveler follows the group to their base he notices that just right at the mountain top, there's a huge city that's carefully balancing on it. Welcome to our home one of the members say as they push him on…"
    SettingFuw = "*Smart* City"
    PromptFuw = "The sign said welcome to the first city where everything is smart and voice activated. The traveler looked and snickered and thought how well that worked out for the city….."
    ArtF = "Draw Demon wings"
    ArtH = "Draw Devil"
    ArtL = "Draw Character blushing"
    ArtSci = "Draw Floating city"
elif RandomPrompt == 5:
    SettingFw = "Dungeon"
    PromptFw = "As the dungeon stirs with life with all the monsters traveling around. Suddenly, the dungeon doors open…."
    SettingAw = "Desert"
    PromptAw = "Ever since the apocalypse happened *character* didn't know any other lifestyle. He has to look for small animals throughout the desert for food, but usually it's berries. However one day that all changed when…"
    SettingFuw = "Autonomous City"
    PromptFuw = "The traveler gets into the city in which he is greeted by a robotic voice welcoming him. As he gets more into the city he sees.."
    ArtF = "Draw a furry"
    ArtH = "Draw void"
    ArtL = "Draw character resting on another"
    ArtSci = "Draw floating car"
elif RandomPrompt == 6:
    SettingFw = "Mountain cave"
    PromptFw = "The group of heroes go into the cave and as the group go deeper into the cave the dwarf exclaims…"
    SettingAw = "Woods"
    PromptAw = "In the woods their was a hunter who has made base in the woods after the whole apocolypse happened. Suddenly one of his silent traps shakes, looks like he caught dinner hopefully. When he gets to the source he gasps…"
    SettingFuw = "Slums"
    PromptFuw = "The figure dashes through the packed streets getting away from the shop owner. *Thief Thief!* They then run into a person and the person grabs them."
    ArtF = "Draw 3 horned goat"
    ArtH = "Draw goopy monster"
    ArtL = "Draw Heart in cage"
    ArtSci = "Draw Raygun"
elif RandomPrompt == 7:
    SettingFw = "Ruins"
    PromptFw = "As the party of warriors trudgge back to the city from the dungeon. They pass through some old ruins and as they pass a magic shield surronds them and a sillhoutte appears before them…"
    SettingAw = "Base "
    PromptAw = "As *character* was doing his chores he thought that this lifestyle was the only one that he knew especially after the apocalypse happened. However during the night as he was on keeping watch duty he came across.."
    SettingFuw = "Hotel with holograms"
    PromptFuw = "As the character steps into the hotel and walks to the desk. An image of a middle aged guy with a handlebar moustache welcomes him…"
    ArtF = "Draw Orc"
    ArtH = "Draw Taxes"
    ArtL = "Draw Dancing couple"
    ArtSci = "Draw Hologram glitching"
elif RandomPrompt == 8:
    SettingFw = "Heaven"
    PromptFw = "As the angel is doing his daily tasks throughout heaven he looks down through the clouds toward Earth as he usually does. Just as he was looking downward he notices a Dark shimmering object shoot up towards him. It barely misses him and he stumbles backward, as the angel sees what it was he gasps, it's a demon."
    SettingAw = "Free way"
    PromptAw = "As the party goes through the run down free way they are all tired and broken. They then see a…."
    SettingFuw = "Police Station"
    PromptFuw = "The officer finally has gotten to the station. As soon as the enter they hear a booming voice reprimand them,…."
    ArtF = "Draw dragon"
    ArtH = "Draw corpse"
    ArtL = "Draw gazebo"
    ArtSci = "Draw City with hologram ads"
elif RandomPrompt == 9:
    SettingFw = "Hell"
    PromptFw = "As the demon does what he usually does in hell and torture souls giving them true torture a bright shimmering object hits him directly in the head. He looks at the object and it flashes very brightly for a second and when it fades he looks back to see…"
    SettingAw = "Tundra"
    PromptAw = "As the party of 4 makes their way through the cold wasteland they get above a hill and spot some smoke. They agree that they should avoid that especially since everyone is at eachothers throats…"
    SettingFuw = "Ai run town"
    PromptFuw = "The traveler walks through town wondering why there isn't any employees in the shops. They then decide to get something and realize that in fact that everything was done with AI's. "
    ArtF = "Draw Basilisk"
    ArtH = "Draw Spider"
    ArtL = "Draw Honey"
    ArtSci = "Draw Future glasses"
elif RandomPrompt == 10:
    SettingFw = "Dragon city"
    PromptFw = "The prince hurrys over to the dragon stables where all the children who are at the age of adulthood get their dragon. He really shouldn't have stayed up all night researching about dragons.. Again. He finally gets there…"
    SettingAw = "Military Camp"
    PromptAw = "*character* is panting and suddenly a zombie is ontop of them almost eating them. They then wake up from their nightmare, and hear their seargent ordering everyone to get up…"
    SettingFuw = "Small Spaceship"
    PromptFuw = "As the space ranger wakes up from a very tiresome dream with a crick in their neck they get an alarm saying that some random debris is heading their way."
    ArtF = "Draw Troll"
    ArtH = "Draw bloodied blade"
    ArtL = "Draw Characters hugging"
    ArtSci = "Draw future computer/phone"

class Prompts(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Writing, Drawing):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
##This is to give the user a message prompt for a prompt
    def onClick():
        tkinter.messagebox.showinfo()
        
    

class StartPage(tk.Frame):
#Starting page that works pretty well
    #Shows 2 options that you can chose from then you can choose a category.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #Instructions
        label = tk.Label(self, text="Choose what type of prompt you would like ^w^\nIf you want a different prompt please restart program.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
#lambda is making in be in line with the gui
        button1 = tk.Button(self, text="Go to Writing prompts",
                            command=lambda: controller.show_frame("Writing"))
        button2 = tk.Button(self, text="Go to Drawing prompts",
                            command=lambda: controller.show_frame("Drawing"))
        button1.pack()
        button2.pack()


class Writing(tk.Frame):

    def __init__(self, parent, controller):

        
#Writing prompts
        #I just have 3 for now but plan on putting in more.
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose a category or go back to main page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        apocalypticbutton = tk.Button(self, text="Apocalyptic",
                                      command=lambda: tk.messagebox.showinfo("Apocalypse Scene", "Setting: " + SettingAw + "\nPrompt: \n" + PromptAw))
        Scifibutton = tk.Button(self, text="Scifi", command=lambda: tk.messagebox.showinfo("Futuristic writing", "Setting: " + SettingFuw + "\nPrompt: \n" + PromptFuw))
        Fantasybutton = tk.Button(self, text="fantasy", command=lambda: tk.messagebox.showinfo("Fantasy Scene", "Setting: " + SettingFw + "\nPrompt: \n" + PromptFw))
        menubutton = tk.Button(self, text="Go to the main page",
                           command=lambda: controller.show_frame("StartPage"))
        menubutton.pack()
        Fantasybutton.pack()
        apocalypticbutton.pack()
        Scifibutton.pack()


class Drawing(tk.Frame):
#This is the drawing frame which has 4 options to choose from
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please select an art category", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        fantasybutton = tk.Button(self, text="Fantasy", command=lambda: tk.messagebox.showinfo("Draw a fairy garden", "Prompt: \n" + ArtF))
        Horrorbutton = tk.Button(self, text="Horror", command=lambda: tk.messagebox.showinfo("Draw a horror scene", "Prompt: \n" + ArtH))
        Futurebutton = tk.Button(self, text="Future", command=lambda: tk.messagebox.showinfo("Draw a Futuristic scene", "Prompt: \n" + ArtSci))
        Lovebutton = tk.Button(self, text="Love", command=lambda: tk.messagebox.showinfo("Draw a love scene", "Prompt: \n" + ArtL))
        menubutton = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        menubutton.pack()
        fantasybutton.pack()
        Horrorbutton.pack()
        Futurebutton.pack()
        Lovebutton.pack()

if __name__ == "__main__":
    app = Prompts()
    app.mainloop()
