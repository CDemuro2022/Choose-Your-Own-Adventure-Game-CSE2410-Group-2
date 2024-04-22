from GUI.GUIObjects import Button, TextBox, Toggle
import music.musicTimer as musicTimer  # stop music thread in this file
import chapters
import sys

from colorama import Fore
import random

import pygame
pygame.init()

class GUI:
    def __init__(self):
        self.bg_color = (128, 255, 0)
        self.space_between_text = 60
        self.music_toggle_size = 88


    def set_params_no_gui(self):
        self.run_gui = False

    def set_params(self, screen_width: int, screen_height: int, screen: pygame.Surface):
        self.run_gui = True

        # find a font that can draw emojis
        fonts = pygame.sysfont.get_fonts()
        if emojis := [font for font in fonts if "emoji" in font]:
            self.font = pygame.font.SysFont(emojis[0], 60)
            self.button_font = pygame.font.SysFont(emojis[0], 40)
            self.small_font = pygame.font.SysFont(emojis[0], 30)

        else:
            print("Didn't find font with emojis")

            self.font = pygame.font.Font(None, 60)
            self.button_font = pygame.font.Font(None, 40)
            self.small_font = pygame.font.Font(None, 30)
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()

        # Logo
        logo_width = 400

        self.logo = pygame.image.load("assets/images/logo.png")
        aspect_ratio = self.logo.get_size()[1] / self.logo.get_size()[0]
        self.logo = pygame.transform.smoothscale(self.logo, (logo_width, logo_width * aspect_ratio))

        # BG
        bg_height = self.screen_height
        self.background = pygame.transform.smoothscale(pygame.image.load("assets/images/landscape.png"), (bg_height* 1.778, bg_height))


    # private function
    def __seperate_text_to_rows(self, text: str, max_width: int, font_to_use: pygame.font.Font) -> list:
        """Takes in: text to split\n max_width allowed, example: screen width\n font to use: What font will the text be rendered in \n
        RETURNS pygame.Surface renders of the text that are split according to max_width"""

        output_text_objs = []
        words = text.split(" ")

        # The index of 'words' where the text was longer than 'max_width'
        last_overflow_index = 0

        _index_in_words = 0
        # every loop add 1 more word to sentece
        while _index_in_words < len(words) + 1:
            _index_in_words += 1

            # get words that are up to current '_index_in_words'
            _text = words[last_overflow_index : _index_in_words]
            _text_render = font_to_use.render(" ".join(_text), True, (0,0,0))


            # if the render is wider than allowed, render the things that fit in
            if _text_render.get_size()[0] > max_width:
                _out_text = " ".join(words[last_overflow_index : _index_in_words - 1])
                _final_text = font_to_use.render(_out_text, True, (0,0,0))
                output_text_objs.append(_final_text)

                last_overflow_index = _index_in_words - 1
                _index_in_words -= 1

            # if last word, add rest and break from loop
            if _index_in_words == len(words):
                _out_text = " ".join(words[last_overflow_index : _index_in_words])
                _final_text = font_to_use.render(_out_text, True, (0,0,0))
                output_text_objs.append(_final_text)
                break


        return output_text_objs

    # private function
    def __render_text_center(self, texts: list):
        """Render list of pygame text renders in the center of the screen"""
        # Get total height of text elements rendered. Sum all text heights and add the spaces between them
        total_height = sum(
            x.get_size()[1] for x in texts
        ) + self.space_between_text * (len(texts) - 1)

        #To prevent text from being too close to the buttons
        if len(texts) > 3:
            self.__render_text_general(texts, 10)
        else:
            # Loop through every text element and render it
            for _i, _text in enumerate(texts):
                _text_width, _text_height = _text.get_size()

                # Get the position to render it in the center of screen
                center_x = self.screen_width / 2 - _text_width / 2
                center_y = (self.screen_height / 2 - _text_height / 2 + 60 * _i) - total_height / 4 # make all texts centered

                self.screen.blit(_text, (center_x, center_y))

    # private function
    def __render_text_general(self, texts: list, y: int):
        """Render list of pygame text renders in the top of the screen"""

        # Loop through every text element and render it
        for _i, _text in enumerate(texts):
            _text_width, _text_height = _text.get_size()

            # Get the position to render it in the center of screen
            center_x = self.screen_width / 2 - _text_width / 2
            text_y = y + 60 * _i

            self.screen.blit(_text, (center_x, text_y))

    def ask_question(self, question: str, answer_choices: list) -> int:
        """Ask a question with two answers.\n
            RETURNS: If pressed left_button: Return True. If pressed right_button: Return False"""
        if not self.run_gui:
            print("Currently no gui is not supported for this function.")
            self.chapter_directory()

        # Initalize texts and buttons
        text_renders = self.__seperate_text_to_rows(question, self.screen_width - 50, self.font)
        
        choice_num = len(answer_choices)
        choice_button = {}
        choice_button_list = []

        for i in range(choice_num):
            #create button for each choice
            long_choice = False
            chapter_name = answer_choices[i]
            if choice_num == 2: #if there are only 2 choices, orient with a left and right button
                if i == 0:
                    choice_button[i] = Button(self.screen_width * .25, self.screen_height * .9, 200, 60, text=answer_choices[0], font=self.button_font, bg_color=(200, 200, 200), hover_color=(240, 240, 240))
                else:
                    choice_button[i] = Button(self.screen_width * .75, self.screen_height * .9, 200, 60, text=answer_choices[1], font=self.button_font, bg_color=(200, 200, 200), hover_color=(240, 240, 240))
            elif choice_num < 3:
                choice_button[i] = Button(150 + i*250, self.screen_height * .9, 200, 60, text=chapter_name, font=self.button_font, bg_color=(200, 200, 200), hover_color=(240, 240, 240))
            else:
                if i < 3:
                    choice_button[i] = Button(150 + i*250, self.screen_height * .75, 200, 60, text=chapter_name, font=self.button_font, bg_color=(200, 200, 200), hover_color=(240, 240, 240))
                else:
                    choice_button[i] = Button(150 + (i-3)*250, self.screen_height * .9, 200, 60, text=chapter_name, font=self.button_font, bg_color=(200, 200, 200), hover_color=(240, 240, 240))

            choice_button_list.append(choice_button[i])

        # Basic pygame window loop
        while True:
            self.screen.blit(self.background, (0, 0))

            # Update buttons
            for btn in choice_button_list:
                btn.draw(self.screen)
                btn.check_hover(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()

                # If left mousebutton clicked, check if clicked on a button
                if (
                    event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]
                ):
                    for i in range(choice_num):
                        if choice_button[i].check_click():
                            return i

            # Render the text
            self.__render_text_center(text_renders)
            pygame.display.update()


    def text_until_enter(self, text: str):
        """Render text in the center of the screen until enter is pressed.\n
            Includes a small text that says 'press enter to continue'"""

        # initialize texts
        text_renders = self.__seperate_text_to_rows(text, self.screen_width - 50, self.font)
        enter_text = self.small_font.render("Press Enter to continue", True, (255,255,255))

        while True:
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()

                # Return when enter pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

            # Render the center text
            self.__render_text_center(text_renders)

            # Render 'press enter to continue' text
            self.screen.blit(enter_text, (self.screen_width / 2 - enter_text.get_size()[0] / 2, 
                                          self.screen_height * .9  - enter_text.get_size()[1] / 2))
            pygame.display.update()


    def exit_func(self):
        musicTimer.musicTimerObj.cancel()  # stop music thread, make sure to call these 2 lines every time program exits
        musicTimer.musicTimerObj.join()
        sys.exit(1)

    def start_screen(self):
        if not self.run_gui: 
            self.__start_screen_no_gui()
            return

        text_box_w = 300
        text_box_h = 100
        name_text_box = TextBox((self.screen_width / 2 - text_box_w / 2, 
                                self.screen_height * .7 - text_box_h / 2, text_box_w, text_box_h), font=self.font)    

        music_toggle = Toggle(self.screen_width - self.music_toggle_size - 20, 20, "assets/images/MusicOn.png", "assets/images/MusicOff.png", (self.music_toggle_size, self.music_toggle_size))
        
        text = self.font.render("Hi! What is you name?", True, (255, 255, 255))

        got_name = False

        while not got_name:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.logo, (self.screen_width / 2 - self.logo.get_size()[0] / 2, 
                                        self.screen_height * .3 - self.logo.get_size()[1] / 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()

                name_text_box.get_event(event)
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and pygame.mouse.get_pressed()[0]
                ):
                    music_toggle.check_click(pygame.mouse.get_pos())

                    if music_toggle.get_state() == 1:
                        pygame.mixer.unpause()
                    else:
                        pygame.mixer.pause()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    player_name = "".join(name_text_box.buffer)
                    got_name = True

            self.screen.blit(text, (self.screen_width / 2 - text.get_size()[0] / 2, 
                                    self.screen_height * .85))
            music_toggle.draw(self.screen)

            name_text_box.update()
            name_text_box.draw(self.screen)
            pygame.display.update()

        self.text_until_enter(f"Welcome {player_name} to this adventure!")

    def chapter_directory(self):
        if not self.run_gui:
            print("no gui is not supported for chapter_directory")
            random.choice(chapters.chapter_list)()
        
        text_renders = self.__seperate_text_to_rows("Chapter Directory", self.screen_width - 50, self.font)

        #create buttons for each chapter in chapter_list
        chapter_num = len(chapters.chapter_list)
        chapter_button = {}
        chapter_button_list = []
        for i in range(chapter_num):
            #create button for each chapter
            chapter_name = chapters.chapter_list[i].__name__[8:].capitalize().replace("_"," ")
            chapter_button[i] = Button(self.screen_width / 2 , 275 + (i-1) * 110, 600, 60, text=chapter_name, font=self.button_font, bg_color=(200, 200, 200), hover_color=(240, 240, 240))
            chapter_button_list.append(chapter_button[i])


        #change content view size based on number of chapters available in chapter_list
        if chapter_num < 5:
            contentView = pygame.transform.smoothscale(pygame.image.load("assets/images/landscape.png"), (self.screen_height* 1.778, self.screen_height))
            CONTENT_HEIGHT = self.screen_height  # Height of content surface
        else:
            contentView = pygame.transform.smoothscale(pygame.image.load("assets/images/landscape.png"), (self.screen_height* 1.778, self.screen_height+(chapter_num-4)*110))
            CONTENT_HEIGHT = self.screen_height+(chapter_num-4)*110  # Height of content surface

        #scroll variables
        scroll_y = 0 # Initial scroll position
        SCROLL_SPEED = 30  # Speed of scrolling
        original_button_y = [btn.y for btn in chapter_button_list] #store original y positions of buttons
        
        while True:
            self.screen.blit(contentView, (0, scroll_y))

            i = 0 # index for chapter_button_list
            for btn in chapter_button_list:
                btn.set_y(original_button_y[i] + scroll_y)
                btn.draw(self.screen)
                btn.check_hover(pygame.mouse.get_pos())
                i += 1 #increment index
            i = 0 #reset index

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_func()

                if (
                    event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]
                ):
                    for i in range(chapter_num):
                        if chapter_button[i].check_click():
                            chapters.chapter_list[i]()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Scroll up
                        scroll_y = min(scroll_y + SCROLL_SPEED, 0)
                    elif event.button == 5:  # Scroll down
                        scroll_y = max(scroll_y - SCROLL_SPEED, -CONTENT_HEIGHT + self.screen_height)
            

            self.__render_text_general(text_renders,10 + scroll_y)
            pygame.display.update()
        

    def __ask_question_no_gui(self, question: str, first: str, second: str, color_before: Fore=None, color_after: Fore=None) -> bool:
        while True:
            q = ""

            if color_before:
                q += color_before

            q += question

            if color_after:
                q += color_after

            answer = input(q)
            if answer.lower() == first.lower():
                return True
            if answer.lower() == second.lower():
                return False

            print("Invalid answer, try again.")

    def __start_screen_no_gui(self):
        name = input(f"{Fore.YELLOW}Type your name: {Fore.LIGHTBLUE_EX}")
        print(f"{Fore.LIGHTGREEN_EX}Welcome", name, "to this adventure!")

        if self.__ask_question_no_gui("Do you want to play? (yes / no) ", "yes", "no", color_before=Fore.YELLOW, color_after=Fore.LIGHTBLUE_EX):
            # Yes
            print(Fore.LIGHTGREEN_EX + "Let's play! \U0001F3AE")
        else:
            # No
            print("See you later! \U0001F600")
            self.exit_func()

        random.choice(chapters.my_list)()
        # if self.__ask_question_no_gui("Do you want music? \U0001F3B5 (yes / no) ", "yes", "no", color_before=Fore.YELLOW, color_after=Fore.LIGHTBLUE_EX):
        #     # Yes
        #     music_player.music()
        #     random.choice(chapters.my_list)()
        # else:
        #     # No
        #     print(Fore.LIGHTGREEN_EX + "Okay \U0001F600")

# Use this object when calling any function from GUI class
GUIInstance = GUI()
