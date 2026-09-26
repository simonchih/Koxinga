"""Exercise the real event/state loop through a complete six-AI game.

For speed, render every 90th frame; movement and the main loop always run.
"""
import os
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
os.environ['KOXINGA_FAST']='1'
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import koxinga as g

seed=int(sys.argv[1]) if len(sys.argv)>1 else 42
g.random.seed(seed)
g.start_p=seed%6;g.turn_id=g.start_p
original=g.draw_all
frames=0
def sampled_draw():
    global frames
    frames+=1
    if frames%90==0 or g.end_game:
        original()
    else:
        g.draw_player_thread.run()
g.draw_all=sampled_draw
g.main(argparse.Namespace(autoplay=True,skip_title=True,frames=60000,screenshot=str(g.ui.ROOT/'art/autoplay-result.png')))
assert g.end_game==1, 'Full game failed to reach scoring'
assert any(p.final_win=='Winner' for p in g.player_data)
for p in g.player_data:
    assert p.final_score==p.final_gold+p.final_location+p.final_treasure
    assert all(v>=0 for v in p.dvalue)
print('PASS full game seed',seed,'scores',[p.final_score for p in g.player_data])
