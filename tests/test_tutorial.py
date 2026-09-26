"""Check lesson progression, menu navigation, rendering and sandbox isolation."""
import os
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
os.environ['KOXINGA_FAST']='1'
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pygame
import koxinga as g
import presentation as ui
import tutorial

TASKS=[['fleet1'],['roll'],['swap'],['card0','confirm'],['day','night'],
       ['supply'],['supply'],['pay','pay'],['inner'],['chest'],
       ['cannon','cannon','fight'],['fire'],['treasure'],['score30'],[]]

class TutorialChecks(unittest.TestCase):
    def test_all_steps_via_visible_controls(self):
        lesson=tutorial.Tutorial()
        random_state=g.random.getstate()
        players=repr([vars(p) if hasattr(p,'__dict__') else p for p in g.player_data])
        for i,actions in enumerate(TASKS):
            self.assertEqual(lesson.step,i)
            lesson.draw(g.screen,g.background)
            if i<14: self.assertNotIn('next',lesson.targets)
            for action in actions:
                self.assertIn(action,lesson.targets)
                lesson.click(lesson.targets[action].center)
                lesson.draw(g.screen,g.background)
            self.assertTrue(lesson.done,f'Lesson {i+1}')
            if i==3: pygame.image.save(g.screen,str(ui.ROOT/'art/tutorial-preview.png'))
            if i==6: pygame.image.save(g.screen,str(ui.ROOT/'art/tutorial-holds.png'))
            if i==10: pygame.image.save(g.screen,str(ui.ROOT/'art/tutorial-combat.png'))
            if i<14: lesson.click(lesson.targets['next'].center)
            else:self.assertEqual(lesson.click(lesson.targets['start'].center),'start')
        self.assertEqual(g.random.getstate(),random_state)
        self.assertEqual(repr([vars(p) if hasattr(p,'__dict__') else p for p in g.player_data]),players)

    def test_incorrect_actions_and_replay(self):
        lesson=tutorial.Tutorial();lesson.step=3;lesson.reset()
        lesson.perform('confirm');self.assertFalse(lesson.done)
        lesson.perform('card2');lesson.perform('confirm');self.assertFalse(lesson.done)
        lesson.perform('card0');lesson.perform('confirm');self.assertTrue(lesson.done)
        lesson.draw(g.screen,g.background)
        lesson.click(lesson.targets['repeat'].center)
        self.assertFalse(lesson.done);self.assertEqual(lesson.state,{})
        lesson.step=13;lesson.reset();lesson.perform('score23');self.assertFalse(lesson.done)
        lesson.perform('score30');self.assertTrue(lesson.done)

    def test_text_stays_inside_panel(self):
        for title,task,paragraphs in tutorial.LESSONS:
            y=206
            for paragraph in paragraphs:y=tutorial.wrapped(g.screen,paragraph,114,y,573)+18
            self.assertLessEqual(y,697,title)

    def test_f1_opens_menu_not_help_then_tutorial_and_start(self):
        event=pygame.event.Event(pygame.KEYDOWN,key=pygame.K_F1)
        with patch.object(pygame.event,'get',return_value=[event]), \
             patch.object(ui,'start_menu',side_effect=['tutorial','start']) as menu, \
             patch.object(tutorial,'run',return_value='menu') as learn, \
             patch.object(ui,'help_overlay') as old_help:
            ui.title_screen(g.screen,g.background)
        self.assertEqual(menu.call_count,2);learn.assert_called_once();old_help.assert_not_called()

    def test_menu_mouse_tutorial_and_escape(self):
        event=pygame.event.Event(pygame.MOUSEBUTTONDOWN,button=1)
        with patch.object(pygame.event,'get',return_value=[event]),patch.object(ui,'mouse_pos',return_value=(800,424)):
            self.assertEqual(ui.start_menu(g.screen,g.background),'tutorial')
        pygame.image.save(g.screen,str(ui.ROOT/'art/start-menu-preview.png'))
        with patch.object(pygame.event,'get',return_value=[pygame.event.Event(pygame.KEYDOWN,key=pygame.K_ESCAPE)]):
            self.assertEqual(tutorial.run(g.screen,g.background),'menu')
            self.assertEqual(ui.start_menu(g.screen,g.background),'back')

if __name__=='__main__':unittest.main()
