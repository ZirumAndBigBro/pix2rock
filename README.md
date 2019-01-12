# pix2rock
Python script to build in Aion on the basis of the existing game objects 

this file converst pixel (black) position from result.bmp file to npc coordinates (result.txt) for AION online game.
example result in result.txt
<spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
for integration in \AC-Game\data\static_data\spawns\Npcs\New\location.xml file.

1. Modificate result.bmp in paint. Note: python needs only black pixels.
2. Put coordinates from your bottem left start point and item size in pix2rock.py and run it.
3. copy coordinates from result.txt and put it in \AC-Game\data\static_data\spawns\Npcs\New\location.xml file.

Maze:
if you need an random and correct maze, use maze.py.
Width and height for your maze you can change in line 99 in maze.py.
As result you wil get result.bmp
