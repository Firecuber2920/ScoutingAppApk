import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder



class MyGridLayout(Widget):

    teamNum = ObjectProperty(None)
    pointsScored = ObjectProperty(None)
    thoughts = ObjectProperty(None)

    def press(self):
        teamNum = self.teamNum.text
        pointsScored = self.pointsScored.text
        thoughts = self.thoughts.text

        print(f"Team {teamNum}, you scored {pointsScored} therefore we think {thoughts} about yous")

        self.teamNum.text=""
        self.pointsScored.text=""
        self.thoughts.text=""


class ScoutingApp(App):
    def build(self):
        return MyGridLayout()


ScoutingApp().run()
