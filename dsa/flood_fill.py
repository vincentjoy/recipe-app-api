# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

def floodFill(self, image, sr, sc, color):
    # Get dimensions of image
    rows = len(image)
    cols = len(image[0])

    # Store the original color
    starting_color = image[sr][sc]

    # If starting pixel is already the target color, return original image
    if starting_color == color:
            return image

    def dfs(r, c):
        # Check if current position is within bounds and has starting color
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            image[r][c] != starting_color):
            return

        # Change current pixel color
        image[r][c] = color

        # Recursively fill all 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    # Start DFS from the given starting position
    dfs(sr, sc)
    return image