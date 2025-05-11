import functions
import random

print("Welcome to Savel's Mad Libs Generator!")

if not functions.ALL_STORIES_DATA:
    print("It seems there are no stories loaded. Please check the stories.json file or error messages.")
else:
    print(f"Loaded {len(functions.ALL_STORIES_DATA)} stories successfully!")

while True:
    story_data = functions.select_random_story() 
    
    if not story_data:
        print("No more stories to play or an error occurred loading them. Goodbye!")
        break

  # --- Accessing data using dot notation for namedtuple ---
    story_template = story_data.template         
    required_placeholders = story_data.placeholders 
    story_title = story_data.title                

    user_words = functions.get_user_inputs_for_story(required_placeholders, story_title)
    
    completed_story_text = functions.build_and_display_story(story_template, user_words, story_title)
    
    functions.handle_save_story(completed_story_text, story_title)

    print("\nThanks for playing!")
    
    play_again = input("Would you like to play again? (Y/N): ").upper()
    if play_again != 'Y':
        print("Goodbye!")
        break
    
    print("\n" + "=" * 40)
    print("Okay, let's play again!")
    print("=" * 40 + "\n")