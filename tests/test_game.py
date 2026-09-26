"""Headless integration checks: assets, input mapping, rules and rendering."""
import os
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
os.environ['KOXINGA_FAST']='1'
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pygame
import koxinga as g
import presentation as ui

class GameChecks(unittest.TestCase):
    def setUp(self):
        g.random.seed(1661)
        g.map_mark=[0]*g.map_block_num
        g.treasure_card=[0]*g.treasure_num
        g.fight_group=[];g.fight_id=None;g.end_game=0
        g.turn_id=0;g.start_p=0;g.show_help=False
        g.draw_player_thread.is_night=0
        g.generate_map();g.generate_dock();g.generate_player_card()

    def test_every_asset_keeps_compatible_size(self):
        manifest=json.loads((ui.ROOT/'art/legacy-assets.json').read_text())
        self.assertEqual(len(manifest),78)
        for name,size in manifest.items():
            self.assertEqual(pygame.image.load(ui.asset('Image/'+name)).get_size(),tuple(size),name)

    def test_human_card_selection_and_confirmation(self):
        p=g.player_data[0];p.mode=4
        card=next(i for i,v in enumerate(p.marked_card) if v==2)
        g.handle_card((230,343))
        self.assertEqual(p.selected_card_value,card)
        with patch.object(g,'next_turn') as advance:
            g.handle_card((230,453))
            self.assertEqual(p.mode,6)
            advance.assert_called_once()

    def test_route_forks_and_finish(self):
        self.assertEqual(g.go_dest_id(5,1),(6,13))
        self.assertEqual(g.go_dest_id(70,1),(0,None))
        p=g.player_data[0];p.IsAI=1;p.mode=1;p.step=1;p.b_id=70;p.next_id=0
        p.x,p.y=p.loc[0]
        g.draw_player_thread.run()
        self.assertEqual(p.goal_game,1)
        self.assertEqual(p.step,0)

    def test_combat_fire_wins_and_renders(self):
        g.fight_group=[0,1];g.fight_id=0
        for p in g.player_data[:2]: p.mode=7
        with patch.object(g.random,'randint',return_value=11): g.roll_fight_dice(0,0)
        self.assertEqual(g.player_data[0].fight_score,'max')
        self.assertEqual(g.player_data[0].fight_solution,'win')
        g.player_data[0].mode=8
        g.draw_all()
        pygame.image.save(g.screen,str(ui.ROOT/'art/combat-preview.png'))

    def test_resource_and_final_score(self):
        p=g.player_data[0]
        p.dtype=[2,1,3,0,0];p.dvalue=[8,4,2,0,0]
        self.assertEqual(g.take_item(0,0,3),3)
        self.assertEqual(p.dvalue[0],5)
        p.goal_game=1;p.treasure[7]=1
        g.calc_score()
        self.assertEqual(p.final_score,27)
        g.draw_all()

    def test_scaled_mouse_and_letterbox(self):
        for size in [(1000,650),(1920,1080),(800,800)]:
            ui._window=pygame.display.set_mode(size,pygame.RESIZABLE)
            ui.present(g.screen)
            r=ui._viewport
            with patch.object(pygame.mouse,'get_pos',return_value=r.center):
                x,y=ui.mouse_pos()
                self.assertAlmostEqual(x,799.5,delta=2)
                self.assertAlmostEqual(y,430,delta=2)

    def test_help_and_board_render(self):
        g.player_data[0].mode=4;g.dice_value1=8;g.dice_value2=20
        g.draw_all();pygame.image.save(g.screen,str(ui.ROOT/'art/game-preview.png'))
        ui.help_overlay(g.screen)
        pygame.image.save(g.screen,str(ui.ROOT/'art/help-preview.png'))

    def test_help_pauses_movement(self):
        p=g.player_data[0];p.mode=1;p.step=1;p.next_id=1
        before=(p.x,p.y)
        g.show_help=True
        g.draw_all()
        self.assertEqual((p.x,p.y),before)

    def test_title_enter_starts(self):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_RETURN))
        ui.title_screen(g.screen,g.background)
        pygame.image.save(g.screen,str(ui.ROOT/'art/title-preview.png'))

if __name__=='__main__': unittest.main()
