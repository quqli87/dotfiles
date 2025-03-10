# Set a custom session root path. Default is `$HOME`.
# Must be called before `initialize_session`.
session_root "~/Documents/sql/mag/dyplomowanie/"


# Create session with specified name if it does not already exist. If no
# argument is given, session name will be based on layout file name.
if initialize_session "mag"; then

  new_window "ssh"
  split_v 20
  split_h 50

  new_window "projekt"
  run_cmd "cd projekt"
  split_v 20
  run_cmd "cd projekt"
  split_h 50
  run_cmd "cd projekt"

  # Create another window at the bottom and change directory
  new_window "word"
  run_cmd "cd word"
  split_v 20
  run_cmd "cd word"
  split_h 50
  run_cmd "cd word"

  new_window "ebooks"
  run_cmd "cd ~/Documents/ebookss/code"
  split_v 20
  run_cmd "cd ~/Documents/ebookss/code"
  split_h 50
  run_cmd "cd ~/Documents/ebookss/code"

  # Create a new window inline within session layout definition.
  #new_window "misc"

  # Load a defined window layout.
  #load_window "example"

  # Select the default active window on session creation.
  #select_window 1

fi

# Finalize session creation and switch/attach to it.
finalize_and_go_to_session

