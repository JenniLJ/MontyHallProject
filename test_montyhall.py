import unittest
from montyhall import initialize_doors, reveal_goat, final_choice

class TestMontyHall(unittest.TestCase):

    def test_initialize_doors(self):
        doors = initialize_doors()
        self.assertEqual(sum(doors), 1)
        self.assertEqual(len(doors), 3)

    def test_reveal_goat(self):
        doors = [0, 0, 1] 
        player_choice = 2  
        goat_door = reveal_goat(doors, player_choice)
        self.assertIn(goat_door, [0, 1]) 
        self.assertEqual(doors[goat_door], 0)  

    def test_final_choice_stick(self):
        """player sticks with the initial choice."""
        doors = [0, 1, 0]  
        initial_choice = 1 
        win, _ = final_choice(doors, initial_choice, False)  
        self.assertTrue(win)  

    def test_final_choice_switch(self):
        """player switches their choice."""
        doors = [0, 1, 0]  
        initial_choice = 0  
        win, _ = final_choice(doors, initial_choice, True)  
        self.assertTrue(win) 

    def test_prize_behind_any_door(self):
        """Test over multiple initializations."""
        prize_positions = {0: 0, 1: 0, 2: 0}
        for _ in range(1000):  
            doors = initialize_doors()
            prize_position = doors.index(1)
            prize_positions[prize_position] += 1

        for prize_position, count in prize_positions.items():
            self.assertGreater(count, 0)
    
    def test_invalid_player_choices(self):
        doors = initialize_doors()
        for invalid_choice in [-1, 3, 100, "a"]:
            with self.assertRaises(ValueError):
                reveal_goat(doors, invalid_choice)
                final_choice(doors, invalid_choice, True)


if __name__ == '__main__':
    unittest.main()