import random
import stories

while True:

    print("Welcome to Mad Libs!")

    selected_story_data = random.choice(stories.all_stories)
    story_template = selected_story_data['template']
    required_placeholders = selected_story_data['placeholders']    

    print("Please enter the following words for the story:")
    user_inputs = {}
    for placeholder in required_placeholders:
        user_word = input(f"Enter a {placeholder}:")
        user_inputs[placeholder] = user_word

    print("\n--- Your Mad Libs Story ---")

    final_story = story_template.format(**user_inputs)

    print(final_story)

    play_again = input("Would you like to play again? (Y/N)")

    if play_again.upper() != "Y":
        print("Thanks again for playing! Goodbye.")
        break
    else:
        print("Okay, let's play again!")
