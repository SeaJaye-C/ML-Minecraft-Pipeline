# Import the Minecraft API and block module
from mcpi import minecraft
from mcpi import block
import time

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# Dictionary to map block names to block types in the Minecraft API
block_map = {
    'stone': block.STONE,
    'glass': block.GLASS,
    'dirt': block.DIRT,
    'wood': block.WOOD,
    'diamond_ore': block.DIAMOND_ORE
}

# Function to read the file and place blocks
def place_blocks_from_file(filename):
    # Get the player's current position
    player_pos = mc.player.getTilePos()
    print(f"Player's current position: {player_pos.x}, {player_pos.y}, {player_pos.z}")

    # Open the text file with block data
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into parts: x, y, z, block_type
            parts = line.strip().split(',')
            if len(parts) == 4:
                x, y, z, block_type = parts
                try:
                    # Convert coordinates to integers and get the block type from the dictionary
                    x = int(x) + player_pos.x  # Adjust coordinates to be relative to the player
                    y = int(y) + player_pos.y  # Adjust coordinates to be relative to the player
                    z = int(z) + player_pos.z  # Adjust coordinates to be relative to the player

                    # Debugging: Print out the block coordinates and block type
                    print(f"Placing block {block_type} at ({x}, {y}, {z})")

                    # Look up the block type, defaulting to STONE if not found
                    block_type = block_map.get(block_type.strip(), block.STONE)

                    # Place the block at the given coordinates
                    mc.setBlock(x, y, z, block_type)
                    time.sleep(0.1)  # Small delay to allow Minecraft to update the world
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

# Call the function to place blocks from the file
place_blocks_from_file("blocks.txt")
