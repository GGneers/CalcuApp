from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.toolbar import MDTopAppBar 
from kivy.core.clipboard import Clipboard
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import MDSnackbar

# Define Screens
class HomeScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

# Main App
class MyApp(MDApp): 
    def build(self):
        return Builder.load_file("main.kv")

    def calculate_additional(self, x1,x2,text):
        try:
            x1 = float(x1) if text.isdigit() else 0
            x2 = float(x2) if text.isdigit() else 1
            amount = float(text) if text else 0
            additional = amount * (x2/x1)
            self.root.get_screen("home").ids.additional.text = str(amount * (x2/x1))
            self.root.get_screen("home").ids.result.text = str(round(additional + amount,2))
        except:
            self.root.get_screen("home").ids.additional.text = "Invalid"

    def copy_to_clipboard(self):
        amount = self.root.get_screen("home").ids.result.text
        Clipboard.copy(amount)

        # Notification after copy
        MDSnackbar(
            MDLabel(
                text=f"Copied \"{amount}\" to clipboard.",
                halign="center",  # Center the text inside the snackbar
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),  # White text
            ),
            size_hint_x=1,  # ✅ Makes it full-width
            pos_hint={"center_x": 0.5},  # ✅ Centers the Snackbar
            md_bg_color=(0.5, 0.5, 0.5, 1),  # Gray background
        ).open()

# Run the app
MyApp().run()
