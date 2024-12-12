# Create a new Word document for the report
doc = Document()

# Add the title of the report
doc.add_heading('Project Report: Adding AI to Space Invaders', level=1)

# Add the Executive Summary section
doc.add_heading('Executive Summary', level=2)
doc.add_paragraph(
    "This project involves creating an enhanced version of the classic arcade game Space Invaders. "
    "The primary goal was to implement basic AI functionality using a Finite State Machine (FSM) to "
    "control enemy behavior. This approach increases the game's interactivity and provides a dynamic "
    "challenge for players."
)

# Add the Motivation section
doc.add_heading('Motivation', level=2)
doc.add_paragraph(
    "The goal of this project was to explore the application of AI techniques in game development. By "
    "integrating FSM logic into enemy ships, we aimed to:"
)
doc.add_paragraph("Simulate varied enemy behaviors.", style='List Bullet')
doc.add_paragraph("Enhance player engagement with dynamic and intelligent challenges.", style='List Bullet')
doc.add_paragraph("Learn and apply practical AI concepts in a gaming scenario.", style='List Bullet')

# Add the Technical Requirements section
doc.add_heading('Technical Requirements', level=2)
doc.add_paragraph("Development Environment:", style='Heading 3')
doc.add_paragraph("Programming Language: Python", style='List Bullet')
doc.add_paragraph("Library: Pygame (for game development)", style='List Bullet')
doc.add_paragraph("Tools:", style='Heading 3')
doc.add_paragraph("Code Editor: Visual Studio Code or PyCharm", style='List Bullet')
doc.add_paragraph("Version Control: GitHub", style='List Bullet')
doc.add_paragraph("System Requirements:", style='Heading 3')
doc.add_paragraph("Python 3.x installed", style='List Bullet')
doc.add_paragraph("Pygame library installed", style='List Bullet')
doc.add_paragraph("Minimum 2 GB RAM", style='List Bullet')

# Add the Main Constructs section
doc.add_heading('Main Constructs', level=2)
doc.add_paragraph("Finite State Machine (FSM):", style='Heading 3')
doc.add_paragraph("Used to control the behavior of enemy ships with states such as:", style='Body Text')
doc.add_paragraph("Idle: Default state with no movement or action.", style='List Bullet 2')
doc.add_paragraph("Patrolling: Horizontal movement across the screen.", style='List Bullet 2')
doc.add_paragraph("Attacking: Shooting bullets at the player ship.", style='List Bullet 2')
doc.add_paragraph("Game Entities:", style='Heading 3')
doc.add_paragraph("Player Ship: Controlled by the player using arrow keys and the spacebar to shoot.", style='List Bullet')
doc.add_paragraph("Enemy Ships: Controlled by FSM logic.", style='List Bullet')
doc.add_paragraph("Bullets: Fired by both the player and enemies.", style='List Bullet')
doc.add_paragraph("Game Loop:", style='Heading 3')
doc.add_paragraph("Continuously updates game state, detects collisions, and renders game objects on the screen.", style='Body Text')

# Add the Implementation section
doc.add_heading('Implementation', level=2)
doc.add_paragraph("Setting Up the Game Environment:", style='Heading 3')
doc.add_paragraph("Installed Pygame and set up the game window dimensions.", style='List Bullet')
doc.add_paragraph("Initialized key entities such as the player and enemies.", style='List Bullet')
doc.add_paragraph("FSM Logic for Enemies:", style='Heading 3')
doc.add_paragraph("Developed a simple FSM to control enemy states.", style='List Bullet')
doc.add_paragraph("Implemented state transitions based on random probabilities and game events.", style='List Bullet')
doc.add_paragraph("Game Mechanics:", style='Heading 3')
doc.add_paragraph("Defined sprite-based objects for the player, enemies, and bullets.", style='List Bullet')
doc.add_paragraph("Integrated collision detection to handle interactions between bullets and ships.", style='List Bullet')
doc.add_paragraph("Enhancements:", style='Heading 3')
doc.add_paragraph("Added random behaviors to enemies for unpredictability.", style='List Bullet')
doc.add_paragraph("Ensured smooth player movement and firing mechanics.", style='List Bullet')

# Add the Code section
doc.add_heading('Code', level=2)
doc.add_paragraph(
    "The complete code for this project is included in the project files and can be provided upon request."
)

# Add the Testing and Debugging section
doc.add_heading('Testing and Debugging', level=2)
doc.add_paragraph("Unit Testing:", style='Heading 3')
doc.add_paragraph("Tested individual FSM states to ensure proper transitions and actions.", style='List Bullet')
doc.add_paragraph("Verified bullet collision detection with enemies and the player.", style='List Bullet')
doc.add_paragraph("Integration Testing:", style='Heading 3')
doc.add_paragraph("Checked smooth integration of FSM logic with the overall game loop.", style='List Bullet')
doc.add_paragraph("Performance Testing:", style='Heading 3')
doc.add_paragraph("Ran the game on various systems to ensure stable performance at 60 FPS.", style='List Bullet')
doc.add_paragraph("Debugging Tools:", style='Heading 3')
doc.add_paragraph("Used debug print statements to monitor state changes and game events.", style='List Bullet')

# Add the Limitations/Difficulties section
doc.add_heading('Limitations/Difficulties', level=2)
doc.add_paragraph("FSM logic lacks adaptability to advanced player strategies.", style='List Bullet')
doc.add_paragraph("Pygame’s basic rendering capabilities restrict visual enhancements.", style='List Bullet')
doc.add_paragraph("Debugging random behaviors required extensive testing.", style='List Bullet')

# Add the Conclusion section
doc.add_heading('Conclusion', level=2)
doc.add_paragraph(
    "This project successfully demonstrates how FSM-based AI enhances gameplay. The dynamic enemy "
    "behaviors provide a challenging and engaging experience while maintaining simplicity and clarity in implementation."
)

# Add the References section
doc.add_heading('References', level=2)
doc.add_paragraph("- Pygame Documentation: https://www.pygame.org/docs/")
doc.add_paragraph("- Finite State Machine Theory: [Insert textbook or academic source].")

# Save the document
output_path = "/mnt/data/Space_Invaders_Project_Report_Final.docx"
doc.save(output_path)
output_path