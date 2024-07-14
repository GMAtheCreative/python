for row in range(10):
    for loop_num in range(5):  # Iterate for each shape pattern


      if loop_num == 0:  # Solid Square
        for _ in range(10):
          print("*", end=" ")


      elif loop_num == 1:  # Right Triangle
        for col in range(row + 1):
          print("*", end=" ")


      elif loop_num == 2:  # Left Triangle
        for col in range(row, 10):
          print("*", end=" ")


      elif loop_num == 3:  # Inverted Right Pyramid
        for _ in range(row + 1):
          print(" ", end=" ")
        for col in range(row, 10):
          print("*", end=" ")


      else:  # Right Pyramid
        for _ in range(row, 10):
          print(" ", end=" ")
        for col in range(row + 1):
          print("*", end=" ")
      print("  ", end="")  # Add two spaces for separation
    print()  # Move to the next line after all shapes are printed

print_shapes()