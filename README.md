# World Cup Anything & Everything app

(Because I can't come up with a better name)

- Develop in TypeScript/Svelte
- Basically an extension of the MAT v2.0 and a playground for me to build football-related features using TypeScript
- Only use publicly available sources (scrape Wikipedia, potential for GitHub Actions jobs) so I can make the app public, and me manually recording data and results via Fotmob/Opta data
- Will need to use Claude to assist with coming up with ideas, but all codes are written by me and me only

Three pages:

- **Schedule** (basically a digital tournament wall calendar):
  - Show all groups (short country name + flag), each group in detail (full country name + flag, group schedule + results), knockout bracket (update in real time after I record the results)
  - Show all matches happen on a specific date and the time (matches my local timezone, though timezone can be manually changed), order them by time (cause my brain needs them to be in order, or else it can't process it)
- **Pre-match** (basically a match preview page with info that I wanna know):
  - Each match has a separate page that uses random generated uuid to display, can also be accessed from the schedule tab, use a slug like `/preview`
  - Show previous results (if there are any) + top goal scorers + xG recorded from previous matches
  - Show all players in squad (shirt no + position + full name + parent club) + overall stats so far (matches/minutes played, goals scored, assists)
- **Live match** (a page where I can take notes while watching matches):
  - Only show all matches that are happening on that day (also uses the same uuid, but different slug like `/live`)
  - Show a tactics board with preset formations
    - Three modes: starting formations, Home In Possession v Away Out of Possession, Home Out of Possession v Away In Possession
      - _Stretch goal_: IP and OOP can have its own three phases as well (IP: Build Up, Progression, Final Third; OOP: Pressing, Mid Block, Low Block)
      - _Stretch goal_: Interactive tactics boards with moveable player dots and arrows and shits
    - Have preset positions and a dropdown box to choose players playing in that position (use data from already collected squads)
    - Each position can turn into a popup text box that uses Markdown for me to take notes
  - Different sections and fields for me to record stats and shit from Fotmob/Opta

Storing data:

- JSON files, cause I can't be bothered to create an AWS account and have a proper MySQL database
- Though, I will still draw a database schema so I can reference during development and building out json files
