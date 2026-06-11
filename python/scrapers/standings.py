# Scrape results and standings from Wikipedia and update the JSON files

# Imports
import json
import requests
import pandas as pd

from io import StringIO
from loguru import logger
from bs4 import BeautifulSoup
from dotenv import dotenv_values

# ----------------------------------------------------------

# Load lookup tables
with open("data/groups.json", "r") as f:
    groups_data = json.load(f)
    f.close()

groups_lookup = pd.DataFrame(groups_data["groups"])
logger.success("Loaded groups lookup table")

with open("data/teams.json", "r") as f:
    teams_data = json.load(f)
    f.close()

teams_lookup = pd.DataFrame(teams_data["teams"])
logger.success("Loaded teams lookup table")

# ----------------------------------------------------------

# Scrape group standings from Wikipedia
standings = []

for group in groups_lookup["name"]:
    logger.info(f"Scraping standings for {group}")

    request = requests.get(
        f"https://en.wikipedia.org/api/rest_v1/page/html/2026_FIFA_World_Cup_{group.replace(' ', '_')}",
        headers={
            "User-Agent": f"World-Cup-2026-App/1.0 ({dotenv_values('../.env')['EMAIL']})"
        },
    )

    soup = BeautifulSoup(request.text, "html.parser")
    table = pd.read_html(StringIO(str(soup.find_all("table", {"class": "wikitable"}))))[
        1
    ]

    # Remove host tag from team name
    table["Teamvte"] = table["Teamvte"].str.replace(r"\s*\(H\)", "", regex=True)

    logger.info(f"Teams in {group}: {table['Teamvte'].tolist()}")

    # Add teamId
    team_ids = []
    for team in table["Teamvte"]:
        team_id = teams_lookup[teams_lookup["fullName"] == team]["id"]
        # General cases
        if not team_id.empty:
            team_ids.append(team_id.iloc[0] if len(team_id) > 0 else None)
        # Special cases
        else:
            # Shorten or English-translated team names
            team_id = teams_lookup[teams_lookup["shortName"] == team]["id"]
            if not team_id.empty:
                team_ids.append(team_id.iloc[0] if len(team_id) > 0 else None)
            # Different spelling
            else:
                # Wikipedia name - FIFA-recognised name
                special_cases = {
                    "Cape Verde": "Cabo Verde",
                    "DR Congo": "Congo DR",
                    "Turkey": "Türkiye",
                }
                team_id = teams_lookup[
                    teams_lookup["fullName"] == special_cases.get(team, team)
                ]["id"]
                team_ids.append(team_id.iloc[0] if len(team_id) > 0 else None)

    # Add teamId column to table
    table["id"] = pd.Series(team_ids)

    # Some pre-processing steps
    logger.info("Pre-processing standings data")
    ## Rename columns
    table.rename(
        columns={
            "Teamvte": "teamName",
            "Pos": "position",
            "Pld": "played",
            "W": "wins",
            "D": "draws",
            "L": "losses",
            "GF": "goalsScored",
            "GA": "goalsConceded",
            "GD": "goalDiff",
            "Pts": "points",
        },
        inplace=True,
    )

    ## Drop unnecessary columns
    table.drop(columns=["Qualification"], inplace=True, errors="ignore")

    ## Move id column in front of teamName
    cols = table.columns.tolist()
    cols.insert(0, cols.pop(cols.index("id")))
    table = table[cols]

    # Convert to dict and add to standings
    logger.info(f"Adding {group} standings to overall list")
    standings.append(
        {
            "id": groups_lookup[groups_lookup["name"] == group]["id"].iloc[0],
            "name": group,
            "teams": table.to_dict(orient="records"),
        }
    )

    logger.success(f"Scraped standings for {group}")

# ----------------------------------------------------------

# Write standings to JSON file
with open("data/standings.json", "w", encoding="utf-8") as f:
    json.dump({"standings": standings}, f, indent=3, ensure_ascii=False)
    f.close()

logger.success("Saved standings to data/standings.json")
